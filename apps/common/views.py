from django.db.models           import Q
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from .models                    import Document
from .serializers               import document_serializer

class panel_common_document_viewset(APIView):
    authentication_classes=[]
    permission_classes=[]

    def get(self, request):
        f = Q()
        if 'enable' in request.GET: f &= Q(deleted = False)
        if 'for_client' in request.GET: f &= Q(for_client = True)
        if 'for_annex' in request.GET: f &= Q(for_annex = True)
        if 'for_transaction' in request.GET: f &= Q(for_transaction = True)

        return Response(
            document_serializer(
                Document.objects.using(request.GET["tenant"]).filter(f).order_by('-id'),
                many = True
            ).data
        )

    def post(self, request):
        serializer = document_serializer(
            data=request.data,
            context={'tenant': request.GET["tenant"]}
        )

        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        document = Document.objects.using(request.GET["tenant"]).get(id=request.data['id'])
        serializer = document_serializer(
            document,
            data=request.data,
            context={ 'tenant': request.GET["tenant"] }
        )

        if(serializer.is_valid()):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request): # Complete
        document = Document.objects.using(request.GET["tenant"]).get(id=request.data["id"])
        document.deleted = not document.deleted
        document.save(update_fields=['deleted'], using=request.GET["tenant"])

        return Response(status=status.HTTP_202_ACCEPTED)