from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the cita index.")

def detail(request, cita_id):
    return HttpResponse("You're looking at cita %s." % cita_id)