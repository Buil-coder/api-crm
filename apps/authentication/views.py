# apps/authentication/views.py
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.party.models import Staff
from apps.party.serializers import onget_staff_serializer

class auth_login_viewset(ObtainAuthToken):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        tenant = request.GET.get("tenant")

        if not tenant:
            return Response({"error": "Tenant parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.using(tenant).get(username=request.data['username'])
        except User.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

        if user.check_password(request.data['password']):
            token, created = Token.objects.db_manager(tenant).get_or_create(user=user)
            token.delete(using=tenant)
            token.key = token.generate_key()
            token.save(using=tenant)

            return Response(
                {
                    "id": user.id,
                    "token": token.key,
                    "staff": onget_staff_serializer(
                        Staff.objects.using(tenant).get(user=user.id),
                        context={"tenant": tenant}
                    ).data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
