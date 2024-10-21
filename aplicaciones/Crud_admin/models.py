from django.db import models


# Create your models here.
class Rol(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre

class User(models.Model):
    documento = models.CharField(max_length=60, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    password = models.CharField(max_length=60)  # Consider using Django's built-in password hashing
    contacto = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

