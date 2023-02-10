from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Semanal
# Create your views here.


def pagina_inicial(request):
    return HttpResponse('Pronto para input de dados')

def contato(request):
    return HttpResponse('Entre em contato com Victor')


def minha_historia(request):
    path = r'minha_historia.html'
    pessoa = {
        'Nome':'Victor',
        'Age': 31
    }
    return render(request,path,pessoa)

#utilizar o template de dentro da pasta
def novo_input (request):
    path = r'novo_input.html'
    return render(request,path)

#confirmar o input dos dados,
#e salvar as variáveis 
def input_realizado (request):
    path = r'input_realizado.html'
    tipo_input = {
        'tipo_input': request.POST.get('TipoInput')
    }
    return render(request,path,tipo_input)


def input_registrado(request):
    dados = {
        'dados': Semanal.objects.all()            #ir até a tabela Semanal, e traga todos os registros.
    }
    return render (request,'input_registrado.html', context = dados)


def detalhe(request,id):
    dados = {
        'dados': Semanal.objects.get(pk=id)
    }
    return render(request,'detalhe.html',dados)