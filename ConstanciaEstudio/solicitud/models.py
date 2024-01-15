from django.db import models
# Create your models here.
"""Se crea un modelo de base de datos para trabajar la informacion requerida
para generar la constancia de estudio, toda esta informacion es necesaria y se puede actualizar y migrar
a la base de datos que se utilice"""

class DataForm(models.Model):
    
    nombres = models.CharField(max_length=100, verbose_name='Nombre')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    edad = models.IntegerField(verbose_name='Edad')
    pnf = models.CharField(max_length=100, verbose_name='PNF')
    seccion = models.CharField(max_length=100, verbose_name='Seccion')
    semestre = models.IntegerField(verbose_name='Semestre')
    cedula = models.IntegerField(verbose_name='Cedula')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envio')