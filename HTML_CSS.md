    
### HTML ESTUDOS
-----


Boa pratica é a pagina inicial chamar ```index.html```

Digitar html5 + TAB.

p>Lorem - texto aleatorio padrão de html. 


<!doctype html> - navegador entender que é um arquivo html;

<html lang="en"> - vem por padrão;
    
> <head> - Cabecalho do navegador;
    <meta> tag = são lidos somente por navegadores, meta dados. Key words, tipo de caracter.  
    <meta charset = 'UTF-8'> compatibilidade com acentuação;
    <meta name = 'viewport' content='width=device-width', initial-scale=1.0"> a tela ira se adaptar ao dispositivo da pessoa.
    <meta name = "description" conten ...
    <meta name = "keywords" conten...
    <meta name = "author" content...
    <title> - titulo do site na aba;

> <body> - conteudo que o usuario irá ver;
    <p>
        <b> - bold 
        <strong> - bold
        <hr> - linha de divisão
        <br> - quebra de linha
        <del> - tachar a palavra
        <sup> - elevado a x
        <sub> - base x
        <mark - marca texto.
        
> <a (anchor/ancora) href = "htttps//:google.com" target = "_blank"> Ir para o google </a> - Criar link absoluto, _blank é para abrir em nova aba.
    <a href = "../index.html"> Voltar pagina inicial </a> - Criar link relativo. Usamos ".." no href

# TABELAS
                                                                                            
    <BR></BR>
    <table width = '50%' border="1" style="align=center">
        <th>NOME</th>
        <th>ENDEREÇO</th>
        <th>MATRICULA</th>
    <tr> 
        <td>Victor</td>
        <td>Paulista</td>
        <td>12345</td>
    </tr>
    </table>
    <!-- 
        th - table header
        tr - table row
        td - table data
        hr - cria uma linha para separação
       -->
    <br>
    <hr>
    <h2>LISTAS NÃO ORDENADAS</h2>
        <ul>
            <li>Celular</li>
            <li>MWO</li>
            <li>TV</li>
        </ul>

    <h2>LISTAS ORDENADAS </h2>
        <ol>
            <li>Celular</li>
            <li>MWO</li>
            <li>TV</li>
        </ol>
    <!--
        ul - unordered list
        li - list item
        ol - ordered list
     -->
     <br>
     <a href="formulario.html">FORMULARIO</a>
    <hr>
                              
## IFRAME
                              
    <!-- Consigo incorporar outras paginas e videos.-->
    <!-- OUTRA Pagina  -->
     <iframe src="https://programacaoweb.com.br/" frameborder="0" width = "100%" height="600"></iframe>
     <br>
     <br>
    <!-- VIDEO YOUTUBE-->
     <iframe width="560" height="315" src="https://www.youtube.com/embed/BKiUFFwr_Zs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    
     <!-- OUTRO HTML da mesma pasta renderizar no iframe  -->
    <a href="sobre_nos.html" target="sobre_nos_iframe">Sobre Nós</a>

    <iframe src="" frameborder="0" name="sobre_nos_iframe" title = "Iframe Exemplo"></iframe>
    
</body>
                                                                                            ```
<body>
## FORMULARIO
                                                                                   
    <form action="arquivo.py" method="POST">
        <label for="input_nome">Nome:</label>
>Text 
        <input type="text" name="input_nome" id="input_nome" placeholder="Digite o nome" required> <br><br>
>Number  
        <label for="idade">Idade:</label>
        <input type="number" name="input_idade" id="idade" placeholder="Digite a idade" required><br><br>
>Email
        <label for="idade">Email:</label>
        <input type="email" name="input_idade" id="email" placeholder="Digite o email" required>
>Password
        <br><br>
        <label for="senha">Senha:</label>
        <input type="password" name="input_senha" id="senha" required>
        
        <br><br>
>DATE
        <input type="date" min="2020-01-01" required>
         
        <br><br>
        <input type="submit" value="Enviar dados">

        <hr>
        <h2>Escolha um animal (radio)</h2>
        <br>
            <input type="radio" id="dog" name="animal" value="Dog">
            <label for="dog">Dog</label>
            <input type="radio" id="cat" name="animal" value="Cat">
            <label for="cat">Cat</label>
            <input type="radio" id="fish" name="animal" value="Fish">
            <label for="fish">Fish</label>

            <!-- type checkbox deixa selecionar varios campos  -->
        <br>
            <h2>Escolha uma cor (combobox) </h2>
            <select name="" id="">
                <option value="vermelho">Vermelho</option>
                <option value="azul">Azul</option>
            </select>

    </FORM>
 </body> 

## CSS
                                    
> TAG - Colocamos diretamente dentro do elemento <h1 style = ...
    
> Interno - Escolhemos o elemento que ira receber as propriedades. 
    <head>...
        <style>
            { backgorund : darkblue;
              font-size : 24px 
            }
        </style>
                                    
> **Externo** - Para termos o mesmo css em comum para todas as paginas.[PROFISSIONAL]
   Criar uma pasta CSS, e dentro criar um arquivo chamado *estilo.css*
    <head>...
        <link rel="stylesheet" href="css/estilo.css">
    </head>

#### estilo.css
body {
    background: darkblue;
}
h1 { 
    color : wheat;
    font-size: 42px;    
}
