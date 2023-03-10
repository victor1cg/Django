"""dados_semanal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_dados_semanal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.pagina_inicial) modificar a pagina inicial para o input registrado,
    path('', views.input_registrado,name= 'input_registrado'),
    path('contato/', views.contato),
    path('minha_historia/', views.minha_historia),
    path('novo_input/', views.criar,name='novo_input'),
    path('novo_input/<int:id>/', views.editar,name='editar_input'),
    path('input_realizado/', views.input_realizado,name='input_realizado'),
    path('<int:id>/', views.detalhe,name='detalhe'),
    path('confirmar_excluir_input/<int:id>/', views.excluir,name='confirmar_excluir_input'),

    
]
