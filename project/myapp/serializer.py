from rest_framework import serializers
from .models import Project 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'titulo', 'descripcion', 'tecnologia', 'fecha_creacion')
        read_only_fields = ('fecha_creacion',)   
        
        # Esto asegura que el campo fecha_creacion no se pueda modificar al crear o actualizar un proyecto.
        # Solo se puede leer, no se puede modificar.
        # Esto es útil para mantener un registro de cuándo se creó el proyecto sin permitir que el usuario lo cambie.