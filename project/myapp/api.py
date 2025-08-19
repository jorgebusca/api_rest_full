from myapp.models import Project
from rest_framework import viewsets, permissions
from .serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permisions_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    # Este viewset maneja las operaciones CRUD para el modelo Project.
    # Utiliza el ProjectSerializer para serializar los datos del modelo.    
    