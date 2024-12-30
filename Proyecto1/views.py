from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):  #Primera vista

    doc_externo=open("C:/Users/jfcasco/Desktop/INVAP/Programación/2024 Django - Pildoras Inf/Proyecto1/Proyecto1/Plantillas/1-saludo.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse('Hasta luego')

def dameFecha(request):

    fecha_actual=datetime.datetime.now()
    documento="Fecha y hora actuales %s" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, edad, agno):
    periodo=agno-2023
    edadFutura=edad+periodo
    documento="En el año %s tendrás %s años" %(agno, edadFutura)
    
    return HttpResponse(documento)