from django.http import HttpResponse
from django.template import Template, Context


def hola_mundo(request): # primera vista
    return HttpResponse("Sansanidad") #funcion, devolver una respuesta con el texto

def despedida (request):    
    return  HttpResponse("Bye")

def mapas(request):
    arch= open("C:/Users/joaqu/Desktop/Proyecto django/ProyectoIntro/ProyectoIntro/Plantillas/plantillanew.html")
    plt= Template(arch.read())
    arch.close()
    cxt=Context()
    documento=plt.render(cxt)
    return HttpResponse(documento)
def home(request):
    archi=open("C:/Users/joaqu/Desktop/Proyecto django/ProyectoIntro/ProyectoIntro/Plantillas/plantilla_home.html")
    plt=Template(archi.read())
    archi.close()
    cxt=Context()
    casa=plt.render(cxt)
    return HttpResponse(casa)
