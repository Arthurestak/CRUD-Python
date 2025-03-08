import Funcoes
import mysql.connector
import os
'''
FUNÇÕES:

procura_usuario(nome),
adiciona_usuario(),
apaga_usuarios(id),
cria_tabela_usuario(banco, senha)

'''


class Conexao:
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'nãosei',
        database = 'crudpython'
    )

while True:
    print('Seja Bem-Vindo! Faça o seu login!\n')
    nome = input('Usuário: ')
    senha = input('Senha: ')
    conexao = Conexao.conexao
    cursor = conexao.cursor()
    cursor.execute("select * from usuario where nome = %s and senha = %s", (nome,senha) )
    usuario = cursor.fetchone()
    if usuario != None:
        if nome in usuario and senha in usuario:
            os.system('cls')
            print(f'Usuário {nome} entrou no sistema!\n')
            break       
    else:
        os.system('cls')
        print(f'Usuário ou senha incorretos!')
        cadastroBotao = input('Deseja fazer o seu cadastro? [S] [N] ').lower()
        if cadastroBotao.startswith('s'):
            os.system('cls')
            Funcoes.adiciona_usuario()
            continue
        else:
            ...

    conexao.commit()

conexao = Conexao.conexao
cursor = conexao.cursor()
cursor.execute('Select * from usuario where nome = %s and senha = %s', (nome,senha))
usuario = cursor.fetchone()
if usuario:
    if usuario[0] <= 10:
        print(f'Seja Bem-Vindo Administrador {usuario[1]}!')
    else:
        print(f'Seja Bem-Vindo Usuário {usuario[1]}!')
else:
    print('Ocorreu algum erro!')
