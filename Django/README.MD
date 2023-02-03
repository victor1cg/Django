## PROJETO UTILIZANDO DJANGO

Feito : Victor Gonçalves  
Data : 02/02/2023

-----  
No Terminal (Shell)
```
django-admin - Traz todos os comando disponiveis
django-admin startproject 'nome projeto' - começar um projeto
cd no projeto
ls - para verificar se realmente criou
python manage.py runserver      - criar um servidor local utilizando a porta 8000
python manage.py runserver 5000 - utilizando a porta 5000

```
### Arquivos Projeto

> manage.py  
Não mexer. Parametros standard para rodar a aplicação.

> db.sqlite3  
Banco de dados padrão.

> _pycache_  
Não mexer. Arquivos temporarios. 

> __init__  
Parametros iniciais de modularização.

> asgi.py e wsgi.py  
Modulos que permitem deixar a aplicação online.

> settings.py  
Configurações especificas.

### Projeto vs APP

Um projeto pode conter um ou mais aplicativos.  
```
python manage.py startapp 'nome_app'
```
Dentro do *settings.py (PROJ) > INSTALLED_APPS*, devemos adicionar o app criado.  

### ROTAS  
Ciclo de app WEB: 
1. Navegação ate a pagina; 
2. Django busca o mapeamento da pagina em *urls.py*;
3. Direciona a função que cria a pagina *views.py*;
4. Retorna os dados/funções ao front end;

Para criar as rotas (URLS) devemos acessar o *urls.py(PROJ)*.  
Por padrão somente temos o /admin.

*urls.py* aqui é possivel definir as rotas de acordo com a função criada em views.py
```
from dados_semanal import views  
#views retornar alguma resposta dado o link direcionado abaixo.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial),
    path('contato/', views.contato),
]

```

*views.py* Aqui é possivel montar a visualização de cada pagina.
```

```

