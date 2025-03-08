import mysql.connector
import os

class Conexao:
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'nãosei',
        database = 'crudpython'
    )

def cria_banco(database):
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        password = 'nãosei',
        user = 'root'
    )
    cursor = conexao.cursor()

    cursor.execute(f'create database {database}')
    print(f'Banco {database} criado com sucesso!')

    conexao.commit()

def cria_tabela_usuario():
    conexao = Conexao.conexao
    cursor = conexao.cursor()

    cursor.execute(f'''Create table if not exists usuario(
                   id_usuario int primary key not null auto_increment,
                   nome varchar(50),
                   idade char(2) not null,
                   senha varchar(20)
                   )''')
    conexao.commit()
    conexao.close()


def adiciona_usuario():

    nome = input('Digite um nome para usuário: ')
    os.system('cls')
    idade = int(input('Digite a sua idade: '))
    os.system('cls')
    senha = input('Digite uma senha: ')
    os.system('cls')

    if nome and idade and senha:
        conexao = Conexao.conexao
        cursor = conexao.cursor()

        cursor.execute("select * from usuario where nome = %s", (nome,))

        usuario = cursor.fetchone()

        if usuario:
            print(f'Usuário "{nome}" já está sendo utilizado!\n')
        else:
            cursor.execute("insert into usuario (nome,idade,senha) values (%s,%s,%s)",(nome,idade,senha))
            conexao.commit()
            print(f'Usuário "{nome}" adicionado com sucesso!')
            
        

    else:
        print('Preencha todos os campos!')


def procura_usuario(nome):
    conexao = Conexao.conexao

    cursor = conexao.cursor()

    cursor.execute("select * from usuario where nome = %s", (nome,))
    
    usuario = cursor.fetchone()

    if usuario:
        print(f'Usuário encontrado! \n ID - NOME - IDADE - SENHA \n{usuario}')
    else:
        print('Usuário não encontrado!')

    conexao.commit()

def apaga_usuarios(id):
    conexao = Conexao.conexao

    cursor = conexao.cursor()

    cursor.execute('select nome from usuario where id_usuario = %s', (id,))

    usuario = cursor.fetchone()

    if usuario:
        cursor.execute('delete from usuario where id_usuario = %s', (id,))
        print(f'Usuário {usuario} deletado com sucesso!')
    else:
        print('Não foi possível deletar esse usuário!')
    conexao.commit()



