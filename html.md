    
### HTML ESTUDOS
-----


Boa pratica é a pagina inicial chamar ```index.html```

Digitar html5 + TAB.

p>Lorem - texto aleatorio padrão de html. 

```html
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
                                                                     ```
<body>
*FORMULARIO*
    <form action="arquivo.py" method="POST">
        <label for="input_nome">Nome:</label>
#Text 
        <input type="text" name="input_nome" id="input_nome" placeholder="Digite o nome" required> <br><br>
#Number  
        <label for="idade">Idade:</label>
        <input type="number" name="input_idade" id="idade" placeholder="Digite a idade" required><br><br>
#Email
        <label for="idade">Email:</label>
        <input type="email" name="input_idade" id="email" placeholder="Digite o email" required>
#Password
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

```
