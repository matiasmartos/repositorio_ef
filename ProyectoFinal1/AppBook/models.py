from django.db import models

# Create your models here.

class Libro(models.Model):

    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    anio = models.DateField()
    reservado = models.BooleanField()

class Sucursal(models.Model):

    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nro_socio = models.IntegerField()
    email = models.EmailField()

class Empleado(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
      
