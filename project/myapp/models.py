from django.db import models

# Create your models here.

class Project(models.Model):
    titulo= models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    tecnologia = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - {self.tecnologia}"