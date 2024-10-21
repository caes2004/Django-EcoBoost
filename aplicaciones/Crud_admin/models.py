from django.db import models

# Modelo para los Roles
class Rol(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre


# Modelo para los Usuarios
class User(models.Model):
    documento = models.CharField(max_length=60, unique=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    password = models.CharField(max_length=60)  # Considera usar un campo de tipo 'PasswordField' para mayor seguridad
    contacto = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo para las Categorías
class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nombre


# Modelo para los Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


# Modelo para las Ventas
class Venta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.producto.nombre} por {self.usuario.nombre}"
