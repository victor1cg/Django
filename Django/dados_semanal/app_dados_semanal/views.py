from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import Semanal
from .forms import SemanalForm
import time
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

def criar(request):
    print('\nNovo input criado \n')
    if request.method == 'POST':
        semanal_form = SemanalForm(request.POST)
        if semanal_form.is_valid():             #verificar se os dados são validos
            semanal_form.save()                 #salvar os dados no banco
        time.sleep(3)                 
        return redirect('input_registrado')     #redirecionar a pagina input registrado
    
    else:                                       #quando clicar o botão vai ser request=POST, quando acessar a pagina sera esse else
        semanal_form = SemanalForm()
        formulario = {
            'formulario': semanal_form
        }
        return render(request,'novo_input.html', context = formulario)

#Editar: 1- Traz os campos ja preenchidos . 2 - Editar os dados e salvar.
def editar(request, id):
    input_ = Semanal.objects.get(pk=id)     #instanciar o object

    #ao acessar a url novo_input/id --> request = GET ;  Com isso teremos uma requisição GET e iremos popular o forms com os dados do banco;
    if request.method == 'GET':
        formulario = SemanalForm(instance = input_)
        #retornar uma pagina com o template
        return render(request,'novo_input.html',{'formulario': formulario})

    #ao clicar em SALVAR no button --> request = POST;
    else:
        formulario = SemanalForm(request.POST,instance=input_)
        if formulario.is_valid():
            formulario.save()
        return redirect('input_registrado')


def excluir (request,id):
    dados = {'dados': Semanal.objects.get(pk = id)}
    
    if request == 'POST':                   #solicitação de delete
        dados.delete()
        return redirect('input_registrado')
    else:                                   #solicitação get de acesso a pagina
        return render(request,'confirmar_excluir_input.html',dados)