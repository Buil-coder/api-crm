from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView 
from rest_framework import serializers
from apps.party.models import Staff
from apps.party.serializers import onget_staff_serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterUserView(APIView):
    authentication_classes=[]
    permission_classes=[]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "username": user.username
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class auth_login_viewset(ObtainAuthToken):
    authentication_classes=[]
    permission_classes=[]

    def post(self, request, *args, **kwargs):
        tenant=request.GET["tenant"]

        try:
            try: user = User.objects.using(tenant).get(username=request.data['username'])
            except User.DoesNotExist: user = None

            if user == None: return Response(status=status.HTTP_204_NO_CONTENT)

            if(user.check_password(request.data['password'])):
                token, created = Token.objects.db_manager(tenant).get_or_create(user=user)
                token.delete(using=tenant)
                token.key = token.generate_key()
                token.save(using=tenant)

                return Response(
                    {
                        "id"    : user.id,
                        "token" : token.key,
                        "staff" : onget_staff_serializer(
                            Staff.objects.using(tenant).get(user=user.id),
                            context={"tenant": tenant}
                        ).data
                    },
                    status = status.HTTP_200_OK
                )
            else: return Response(status = status.HTTP_401_UNAUTHORIZED)
        except Exception as e: return Response(status = status.HTTP_204_NO_CONTENT)