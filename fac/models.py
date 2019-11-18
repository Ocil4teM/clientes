from django.db import models
from bases.models import ClaseModelo

# Create your models here.

class Cliente(ClaseModelo):

    NAT='Natural'
    JUR='Jurídica'
    TIPO_CLIENTE = [(NAT,'Natural'),(JUR,'Jurídica')]

    identificacion = models.CharField(max_length=13, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    celular = models.CharField(max_length=20,null=True,blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)

    tipo=models.CharField(max_length=10, choices=TIPO_CLIENTE, default=NAT)

    def __str__(self):
        return '{} {}'.format(self.apellidos,self.nombres)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        super(Cliente, self).save()

    class Meta:
        verbose_name_plural = "Clientes"