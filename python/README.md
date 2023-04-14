#  Exercicios SQL 

Especificação fictícia:  
A Softblue (www.softblue.com.br) está contratando você como DBA (Database Administrator) para que você crie um banco de dados para gerenciar as matrículas dos alunos da Softblue. Neste banco de dados deverá estar armazenado as informações dos cursos disponibilizados pela Softblue, como nome, tipo (se é de banco de dados, programação ou outro), preço e os dados do instrutor responsável pelo curso (nome e telefone). 
Neste mesmo banco de dados deve ser armazenado as informações dos alunos da Softblue (nome, endereço e e-mail) bem como todos os cursos que o aluno já se matriculou. 
Leve em consideração que todas as informações dos alunos, cursos e instrutores poderão ser alteradas a qualquer tempo. Popule as tabelas criadas com alguns exemplos fictícios. Todas as chaves estrangeiras apresentadas neste exemplo são consideradas índices.  

## *Exercicio 1 

### Programe o código SQL necessário para gerar a estrutura do banco de dados.

```sql
create table aluno(
aluno_id int unique not null auto_increment,
nome varchar (20) not null,
sobrenome varchar (20) not null,
email varchar (30) not null,
curso_id int not null,
primary key (aluno_id),
constraint fk_aluno_cursos foreign key (curso_id) references curso (curso_id)
);

create table cursos(
curso_id int unique not null auto_increment,
nome varchar (20) not null,
carga int not null, 
valor double not null,
instrutor_id int,
tipo_id not null,
primary key (curso_id),
constraint fk_cursos_instrutor foreign key (instrutor_id) references instrutor(instrutor_id),
constraint fk_cursos_tipo foreign key (tipo_id) references tipo(tipo_id)
);

create table tipo(
tipo_id int unique not null auto_increment,
tipo varchar (20) not null,
primary key (tipo_id)
);
 
create table cursos(
curso_id int unique not null auto_increment,
nome varchar (20) not null,
carga varchar (20) not null,
valor DOUBLE not null,
tipo_id int not null,
instrutor_id int not null,
primary key (curso_id)
);

create table instrutor(
instrutor_id int unique not null auto_increment,
nome varchar (20) not null,
telefone varchar (20) not null,
primary key (instrutor_id)
);
```
### Inclua a coluna DATA_NASCIMENTO na tabela ALUNO do tipo string, de tamanho 10 caracteres; 

```sql 
ALTER TABLE aluno ADD data_nascimento varchar (10);
```

### Altere a coluna DATA_NASCIMENTO para NASCIMENTO e seu tipo de dado para DATE; 
```sql
ALTER TABLE aluno MODIFY data_nascimento DATE; 
```

### Crie um novo índice na tabela ALUNO, para o campo ALUNO; 
```sql 
create index nome on aluno (nome);
```

### Inclua o campo EMAIL na tabela INSTRUTOR, com tamanho de 100 caracteres; 
```sql
ALTER TABLE instrutor ADD email varchar (100);
```

### Remova o campo EMAIL da tabela INSTRUTOR  
```sql
ALTER TABLE instrutor DROP COLUMN email;
```

## *Exercicio 2

### Alimente as tabelas com informações 
```sql
INSERT into tipo (tipo) values ('banco de dados'),('programação'),('modelagem de dados');

insert into instrutor (nome, telefone) values ('André Milani', '1111-1111'),('Carlos Tosin', '1212-1212');

insert into cursos (nome, carga, valor, tipo_id,instrutor_id) values ('Java Fundamentos', 60, 689.87,2,2), ('SQL completo', 20, 689.87,1,2),('Java avançado', 60, 289.89,1,2), ('PHP básico', 50, 322.50,1,1);

insert into aluno (nome, sobrenome, email,curso_id, data_nascimento) values ('José', 'Moraes', 'jose@softblue.com.br',3, '1997-10-25'),
('Emílio', 'Rodrigues', 'emilio@softblue.com.br',2, '1987-11-25'),
('Cristian', 'Marques', 'CrisMarques@softblue.com.br',4, '1998-10-29'),
('Regina', 'Joyce', 'regininha@softblue.com.br',1, '1988-07-15'),
('Fernando', 'Ursuly', 'Fefeury@softblue.com.br',4, '1999-04-10');
```
### Exibir somente o título de cada curso da Softblue;
```sql
select nome from cursos;
``` 
#### Exibir somente o título e valor de cada curso cujo preço seja maior que 300;
```sql
select nome, valor 
from cursos
where valor > 300;
```
### Exibir somente o título e valor de cada curso da Softblue cujo preço seja maior que 300 e menor que 600;
```sql
select nome, valor 
from cursos
where valor > 300 and valor < 600;
```
### Altere o e-mail do aluno Cristian para 'cristinin@gmail.com';
```
UPDATE aluno SET email = 'cristinin@gmail.com' WHERE aluno_id = 3;
```
### Aumente em 10% o valor dos cursos abaixo de 300;
```sql
UPDATE cursos SET valor = valor * 0.1 
where valor < 300;
``` 
### Altere o nome do curso de Php Básico para Php Fundamentos;
```sql
UPDATE cursos SET nome = 'PHP fundamentos' where curso_id = 4;
```

## *Exercicio 3

### Exiba uma lista com os títulos dos cursos e o tipo de curso ao lado;
```sql
SELECT cursos.nome, tipo.tipo
FROM cursos
INNER JOIN tipo 
ON cursos.tipo_id = tipo.tipo_id;
```

### Exiba uma lista com os títulos dos cursos, tipo do curso, nome do instrutor responsável pelo mesmo e telefone;
```sql
SELECT cursos.nome, tipo.tipo, instrutor.nome, instrutor.telefone
FROM cursos
JOIN tipo ON cursos.tipo_id = tipo.tipo_id
JOIN instrutor ON cursos.instrutor_id = instrutor.instrutor_id;
``` 

### Crie uma visão que traga o título e valor somente dos cursos de programação;
```sql
create view nome_valor as 
select nome, valor
from cursos
where tipo_id = 2;

select * from nome_valor;
```

### Crie uma visão que traga os títulos dos cursos, tipo do curso e nome do instrutor;
```sql
create view visualizacao as
SELECT cursos.nome AS nome_curso, tipo.tipo, instrutor.nome AS nome_instrutor
FROM cursos
JOIN tipo ON cursos.tipo_id = tipo.tipo_id
JOIN instrutor ON cursos.instrutor_id = instrutor.instrutor_id;

select * from visualizacao;
```

## *Exercicio 4


### Exiba a quantidade de cursos que já foram vendidos;
```sql
SELECT count(nome) FROM cursos;
```

### Exiba o valor total já arrecadado pelos cursos vendidos; 
```sql
SELECT ROUND(SUM(cursos.valor),2) AS total_arrecadado
FROM aluno
INNER JOIN cursos ON aluno.curso_id = cursos.curso_id;
```

### Exiba o valor do curso mais caro; 
```sql
SELECT MAX(valor) AS Curso_mais_caro
FROM cursos;
```

### Exiba o valor do curso mais barato;
```sql
SELECT MIN(valor) AS Curso_mais_barato
FROM cursos;
```

### Exiba os nomes dos instrutores e a quantidade de cursos que cada um tem sob sua responsabilidade; 
```sql
SELECT instrutor.nome, count(cursos.nome) 
FROM instrutor
INNER JOIN cursos ON cursos.instrutor_id = instrutor.instrutor_id
GROUP BY instrutor.nome;
```
 
### Exiba apenas os e-mails que tem dominio gmail;
```sql
SELECT nome, email
FROM aluno
WHERE email LIKE '%@gmail.com';
```

### Exiba os nomes dos cursos de Java;
```sql
SELECT nome
FROM cursos
WHERE nome LIKE 'java%';
```

### Utilizando subquery e o parâmetro IN, exiba os nomes dos cursos disponibilizados cujo tipo de curso seja 'Programação'; 
```sql
SELECT cursos.nome, tipo.tipo
FROM cursos
INNER JOIN tipo ON cursos.tipo_id = tipo.tipo_id
WHERE tipo.tipo_id IN (SELECT tipo_id FROM tipo WHERE tipo_id=2);

# usando join
SELECT cursos.nome, tipo.tipo
FROM cursos 
INNER JOIN tipo ON tipo.tipo_id = cursos.tipo_id
WHERE tipo.tipo = 'Programação';
```

### Utilizando subquery e o parâmetro EXISTS, exiba novamente os nomes dos cursos disponibilizados cujo tipo de curso seja 'Programação'; 
```sql
SELECT cursos.nome, tipo.tipo
FROM cursos
INNER JOIN tipo ON cursos.tipo_id = tipo.tipo_id
WHERE EXISTS (SELECT tipo_id FROM tipo WHERE tipo_id=2 and cursos.tipo_id = tipo.tipo_id);
```