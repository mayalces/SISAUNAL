from django.db import models

# Create your models here.

class Especialidad(models.Model):
	nombre = models.CharField(max_length=200)
	def __unicode__(self):
		return self.nombre
	
#class Horario(models.Model):
#	nombre = models.CharField(max_length=200)

class Profesional(models.Model):
	nombre = models.CharField(max_length=200)
	cedula = models.CharField(max_length=20)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)
	especialidad = models.ForeignKey(Especialidad)
	def __unicode__(self):
		return self.nombre
	
class Paciente(models.Model):
	nombre = models.CharField(max_length=200)
	cedula = models.CharField(max_length=20)
	direccion = models.CharField(max_length=50)
	telefono = models.CharField(max_length=15)
	tipo_paciente = models.CharField(max_length=200)
	def __unicode__(self):
		return self.nombre

class Cita(models.Model):
	duracion = models.IntegerField()
	estado = models.CharField(max_length=20)
	tipo_cita = models.CharField(max_length=200)
	profesional = models.ForeignKey(Profesional)
	fecha = models.DateTimeField('Fecha')
	paciente = models.ForeignKey(Paciente)
	
	
	
class Multa(models.Model):
	valor = models.IntegerField()
	cita = models.ForeignKey(Cita)