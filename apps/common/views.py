from django.db.models           import Q
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from .models                    import Document
from .serializers               import document_serializer

from .models import (
    Persona,
    Empresa,
    Proyecto,
    Unidad,
    FichaDatosCliente,
    CronogramaPagos,
    Cuota,
    Observaciones,
    Grupo
)
from .serializers import (
    PersonaSerializer,
    EmpresaSerializer,
    ProyectoSerializer,
    UnidadSerializer,
    FichaDatosClienteSerializer,
    CronogramaPagosSerializer,
    CuotaSerializer,
    ObservacionesSerializer,
    GrupoSerializer
)

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


class PersonaViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmpresaViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProyectoViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        proyectos = Proyecto.objects.all()
        serializer = ProyectoSerializer(proyectos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProyectoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnidadViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        unidades = Unidad.objects.all()
        serializer = UnidadSerializer(unidades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UnidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FichaDatosClienteViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        fichas = FichaDatosCliente.objects.all()
        serializer = FichaDatosClienteSerializer(fichas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FichaDatosClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CronogramaPagosViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        cronogramas = CronogramaPagos.objects.all()
        serializer = CronogramaPagosSerializer(cronogramas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CronogramaPagosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CuotaViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        cuotas = Cuota.objects.all()
        serializer = CuotaSerializer(cuotas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CuotaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObservacionesViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        observaciones = Observaciones.objects.all()
        serializer = ObservacionesSerializer(observaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ObservacionesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GrupoViewSet(APIView):
    authentication_classes=[]
    permission_classes=[]
    def get(self, request):
        grupos = Grupo.objects.all()
        serializer = GrupoSerializer(grupos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GrupoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)