from django.db import models
from django.contrib import admin
# Create your models here.


class autor(models.Model):
    nombre = models.CharField(max_length=60)
    def __unicode__(self):
        return self.nombre
    class Meta:
    	verbose_name_plural = 'autores'

class libro(models.Model):
    nombre = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=10,null=True,blank=True)
    fecha_pub = models.DateTimeField('fecha publicacion')
    autor = models.ForeignKey(autor)
    def __unicode__(self):
        return self.nombre


class voto(models.Model):
	libro = models.ForeignKey(libro)
	voto = models.IntegerField()

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