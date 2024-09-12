import json
from django.contrib.auth.models import User
from django.db.models           import Q
from rest_framework             import status
from rest_framework.views       import APIView
from rest_framework.response    import Response

from .socket        import client_socket
from .models        import Staff, StaffRole
from .serializers   import (
    staff_role_serializer,
    onget_staff_role_serializer,
    onget_staff_serializer,
    staff_serializer,
)

from rest_framework.pagination  import LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    default_limit = 15
    max_limit = 1000000
    min_limit = 1
    min_offset = 0
    max_offset = 1000000


class staff_role_viewset(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request):
        f = Q()
        if 'enabled' in request.GET:
            f &= Q(deleted = False)
        return Response(
            onget_staff_role_serializer(
                StaffRole.objects.using(request.GET["tenant"]).filter(f).order_by('-id'),
                many = True
            ).data
        )

    def post(self, request):
        serializer = staff_role_serializer(
            data=request.data,
            context={'tenant': request.GET["tenant"]}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        tenant=request.GET["tenant"]
        role = StaffRole.objects.using(tenant).get(id=request.data["id"])
        serializer = staff_role_serializer(
            role,
            data=request.data,
            context={'tenant': tenant}
        )

        if(serializer.is_valid()):
            serializer.save()

            client_socket.notify(
                message={"key": "value"},
                tenant=tenant
            )

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        role = StaffRole.objects.using(request.GET["tenant"]).get(id=request.data["id"])
        role.deleted = not role.deleted
        role.save(update_fields=['deleted'], using=request.GET["tenant"])

        return Response(status=status.HTTP_202_ACCEPTED)


class staff_viewset(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request):
        f = Q()

        if 'role' in request.GET:
            f = Q(role=request.GET['role'])
        if 'deleted' in request.GET:
            f = Q(deleted= False if request.GET['state'] == 'true' else True)
        if 'search' in request.GET:
            print(request.GET['search'])
            f = Q(names__icontains=request.GET['search']) | Q(lastnames__icontains=request.GET['search']) | Q(document_number__icontains=request.GET['search'])

        pagination = CustomPagination()
        return pagination.get_paginated_response(
            onget_staff_serializer(
                pagination.paginate_queryset(
                    Staff.objects.using(request.GET["tenant"]).filter(f).order_by('deleted', '-created_date'),
                    request
                ),
                many = True,
                context={'tenant': request.GET["tenant"]}
            ).data
        )

    def post(self, request, *args, **kwargs):
        tenant=request.GET["tenant"]
        try:
            if (len(User.objects.using(tenant).filter(username=request.data['username']))>0):
                return Response(status=status.HTTP_409_CONFLICT)
            else:
                user=User(
                    username=request.data['username'],
                    password=request.data['password'],
                    is_staff=True
                )
                user.set_password(request.data['password'])
                user.save(using=tenant)

                serializer=staff_serializer(
                    data=json.loads(json.dumps({
                        "names"             : request.data['names'],
                        "lastnames"         : request.data['lastnames'],
                        "document_number"   : request.data['document_number']
                    })),
                    context={
                        'user'          : user,
                        "role"          : request.data['role'],
                        "document_type" : request.data['document_type'],
                        "business"      : request.data['business'],
                        "company"       : request.data['company'],
                        "tenant"       : tenant
                    }
                )

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        tenant = request.GET["tenant"]
        try:
            if "password" in request.data:
                user = User.objects.using(request.GET["tenant"]).get(username = request.data["username"])
                user.set_password( request.data["password"])
                user.save(update_fields=['password'], using=tenant)
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                serializer = staff_serializer(
                    Staff.objects.using(tenant).get(id=request.data["id"]),
                    data=request.data,
                    context={'tenant': tenant}
                )

                if(serializer.is_valid()):
                    serializer.save()

                    return Response(status=status.HTTP_202_ACCEPTED)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request): # Complete
        staff = Staff.objects.using(request.GET["tenant"]).get(id=request.data["id"])
        staff.deleted = not staff.deleted
        staff.save(update_fields=['deleted'], using=request.GET["tenant"])

        return Response( {"status":"user deleted"} , status=status.HTTP_202_ACCEPTED)