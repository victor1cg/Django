    
```
<body>
    <h2>FORMULARIO</h2>
    <form action="arquivo.py" method="POST">
        <label for="input_nome">Nome:</label>
        
        <input type="text" name="input_nome" id="input_nome" placeholder="Digite o nome" required> <br><br>
        
        <label for="idade">Idade:</label>
        <input type="number" name="input_idade" id="idade" placeholder="Digite a idade" required><br><br>

        <label for="idade">Email:</label>
        <input type="email" name="input_idade" id="email" placeholder="Digite o email" required>

        <br><br>
        <label for="senha">Senha:</label>
        <input type="password" name="input_senha" id="senha" required>
        
        <br><br>
        
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
