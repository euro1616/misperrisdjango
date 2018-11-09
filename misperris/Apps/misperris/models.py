from django.db import models
from django.contrib.auth.models import User
import datetime
import uuid # Required for unique book instances
# Create your models here.
class Mascota(models.Model):
    adoptante = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True, help_text="Persona que adopta")
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Codigo Unico de la Mascota")
    nombre =  models.CharField(max_length=30, help_text="Nombre Mascota")
    opt=(('P', 'Pequeño'),('M','Mediano'),('G','Grande'))
    tamanio= models.CharField(max_length=1, choices=opt,default='SI', help_text="Tamaño de la Mascota")
    peso = models.DecimalField(max_digits=4, decimal_places=2, help_text="Peso en Kg de la Mascota")
    color =  models.CharField(max_length=30, help_text="Color de la Mascota")
    ope=(('Rescatado','Rescatado'),('Disponible','Disponible'),('Adoptado','Adoptado'))
    estado= models.CharField(max_length=10, choices=ope,default='Rescatado' , help_text="Seleccione estado de la Mascota")
    fecharescate = models.DateField(default=datetime.date.today)
    descripcion =  models.CharField(max_length=30, help_text="Descripcion de la Mascota")
    def __str__(self):
        return '%s %s' % ("Nombre: "+self.nombre, ", Estado: "+self.estado)

        