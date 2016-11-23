from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    Ropa='Ro'
    Calzado='Ca'
    Bebidas='Be'
    MARCAS =(
        (Ropa, 'Ropa'),
        (Calzado, 'Calzado'),
        (Bebidas, 'Bebidas'),
    )
    codigo = models.CharField(max_length=7)
    nombre = models.CharField(max_length=30)
    imagen = models.ImageField(blank = 'True',upload_to='imagen/')
    marca = models.CharField(max_length=2,choices=MARCAS,default=Ropa,)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    existencia = models.IntegerField()

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    dpi = models.CharField(max_length=15)
    nombre = models.CharField(max_length=60)
    productos   = models.ManyToManyField(Producto, through='Compra')

    def __str__(self):
        return self.nombre

class Compra (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
