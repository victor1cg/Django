from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def pagina_inicial(request):
    return HttpResponse('Pronto para input de dados')

def contato(request):
    return HttpResponse('Entre em contato com Victor')

# def minha