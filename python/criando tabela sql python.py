import mysql.connector
import random
from faker import Faker

con = mysql.connector.connect(host='localhost',database='loja',user='root',password='1234')

if con.is_connected():
    info = con.get_server_info()
    print ('conectado com sucesso', info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('conectado ao banco de dados:',linha)

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


if con.is_connected():
    cursor.close()
    con.close()
    print ('conexão encerrada')


    
    

