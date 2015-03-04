from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
# Create your models here.


class autor(models.Model):
    nombre = models.CharField(max_length=60)
    def __unicode__(self):
        return self.nombre
    class Meta:
    	verbose_name_plural = 'autores'

class libro(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_pub = models.DateField('fecha publicacion')
    autor = models.ForeignKey(autor)
    sinopsis = models.CharField(max_length=1500)
    def __unicode__(self):
        return self.nombre


class voto(models.Model):
	libro = models.ForeignKey(libro)
	#usuario = user.ForeignKey(user)
	voto = models.IntegerField()
#	class Meta:
#		unique_together = (('libro','usuario'),)

#    def __unicode__(self):
#        return self.publicaciones
#class publicacion(models.Model):
#    libro = models.ForeignKey(libro)
#   autor = models.ForeignKey(autor)
#  fecha = models.DateTimeField
# class Meta:
#	verbose_name_plural = 'publicaciones'

admin.site.register(libro)
admin.site.register(autor)
admin.site.register(voto)
