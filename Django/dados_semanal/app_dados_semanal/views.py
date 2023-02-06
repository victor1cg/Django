from django.shortcuts import render
from django.shortcuts import HttpResponse
import os
# Create your views here.


def pagina_inicial(request):
    return HttpResponse('Pronto para input de dados')

def contato(request):
    return HttpResponse('Entre em contato com Victor')

#utilizar o template de dentro da pasta
def novo_input (request):
    return render(request,'Django/dados_semanal/templates/novo_input.html')

#confirmar o input dos dados,
#e salvar as variáveis 
def input_realizado (request):
    tipo_input = {
        'tipo_input': request.POST.get('TipoInput')
    }
    return render(request,'Django/dados_semanal/templates/input_realizado.html',tipo_input)

def check_path ():
    path = 'Django/dados_semanal/templates/novo_input.html'
    return os.path.exists(path)

check_path()