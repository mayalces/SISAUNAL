from citas.models import Cita
from citas.models import Profesional
from citas.models import Paciente
from citas.models import Especialidad
from django.contrib import admin

admin.site.register(Cita)
admin.site.register(Profesional)
admin.site.register(Paciente)
admin.site.register(Especialidad)
