## Nesse código irei demonstrar de forma detalhada como realizar uma conexão Python-SGBD utilizando o MySql. Será criada uma tabela em um banco de dados já existente e o mesmo será alimentado com informações geradas pela biblioteca Faker. 
O código foi executado na IDLE Shell 3.10.8. e inserida no google colab afim de facilitar a organização e o commit. 

#### Primeiro passo:
importar o conector que fará de fato a conexção entre o python e o sgbd e as demais bibliotecas que serão utilizadas;

```python 
import mysql.connector
from faker import Faker
```

### Segundo passo:
Criar a conexação utilizando uma variável, aqui chamada de '*con*', que recebe o conector e o método *connect* com os parâmetros hots, database, user e password. 

```python 
con = mysql.connector.connect(host='localhost',database='loja',user='root',password='1234')
```

### Terceiro passo:
Verificar se a conexão foi estabelecida criando uma estrutura if com o método *is_connected*. 
Ainda dentro da estrutura condicional é criado um cursor que quando executado tras a instrução sql para que seja mostrado na tela se estamos manipulando o  banco de dados selecionado anteriormente ou não. 
Após isso o resultado da execussão do cursor é armazenado na variável *linha* com o método *'Fetchone'* que busca por uma linha.
Por fim o print demonstra o nome do banco de dados.

```python 
if con.is_connected():
    info = con.get_server_info()
    print ('conectado com sucesso', info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('conectado ao banco de dados:',linha)
 ```
    
## Quarto passo
Criar uma tabela 

```python 
try:
    criar_tabela = """CREATE TABLE clientes(
                        id_cliente INT not null auto_increment,
                        nome VARCHAR(45) not null,
                        rg varchar(15) not null,
                        estado varchar(30) not null,
                        primary key (id_cliente)); """
    cursor.execute(criar_tabela)
    print ('tabela de clientes criada com sucesso!')
except mysql.connector.Error as erro:
    print ('Falha ao criar a tabela no MySq: {}'.format(erro))
```

### Quinto passo 
Inserir dados na tabela utilizando a biblioteca faker. 

Criamos uma lista com as colunas da tabela sendo alimentadas pelo faker, sempre utilizando a estrutura try except para mitigar erros. 

```python 
try:
    fake = Faker(locale='pt_BR')
    
    clientes = []
    for i in range(15):
        nome = fake.name()
        rg = fake.rg()
        estado = fake.state()
        clientes.append((nome,rg,estado))

    cursor.executemany('INSERT INTO clientes (nome, rg, estado) VALUES (%s, %s, %s)', clientes)
    con.commit()
    print('Dados inseridos com sucesso!')
        
except mysql.connector.Error as erro:
    print ('Falha ao inserir dados: {}'.format(erro))
 ```
 
 ### Sexto passo: 
Encerrar a conexão com a instrução .close

```python 
if con.is_connected():
    cursor.close()
    con.close()
    print ('conexão encerrada')
 ```


