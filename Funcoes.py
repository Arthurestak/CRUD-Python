import mysql.connector
import os

class Conexao:
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'ceub123456',
        database = 'arthur'
    )

def cria_banco():
    conexao = mysql.connector.connect(
        host = '127.0.0.1',
        password = 'ceub123456',
        user = 'root'
    )
    cursor = conexao.cursor()

    banco = input('Digite o nome do banco que você quer criar: ')

    cursor.execute(f'create database {banco}')
    print(f'Banco {banco} criado com sucesso!')

    conexao.commit()

def cria_tabela():
    conexao = Conexao.conexao
    cursor = conexao.cursor()
    while True:

        
        nomeTabela = input('Digite o nome da tabela que deseja criar: ')    # Nome da tabela que será criada

        cursor.execute(f'create table {nomeTabela} (id_{nomeTabela} int primary key not null auto_increment)')  # Tabela criada com Sucesso
        os.system('cls')
        print(f'Tabela \'{nomeTabela}\' criada com sucesso!')

        while True:
            coluna = input('Digite o nome da coluna: ')
            tipo = input('Digite o tipo: ')

            os.system('cls')
            print(f'Tipo: {tipo}')

            verificacao_colunas = input('\nVerifique se os tipos foram digitados corretamente! [S], [N] ').lower()  # Verificação do tipo

            if verificacao_colunas.startswith('s'):
                try:
                    cursor.execute(f'alter table {nomeTabela} add column {coluna} {tipo}')  # Adicionando coluna
                    os.system('cls')
                    print(f'\nColuna "{coluna}" adicionada com sucesso!')
                except:
                    os.system('cls')
                    print('Ocorreu algum erro! ')   # Verificação de erros
                    continue
            else:
                os.system('cls')
                print('Digite novamente corretamente!')
                continue

            maisColunas = input('\nDeseja adicionar mais colunas? [S],[N] ').lower()    # Se desejar adicionar mais colunas
            if maisColunas.startswith('s'):
                os.system('cls')
                continue
            else:
                os.system('cls')
                break

        reiniciar = input('Deseja criar outra tabela? [S], [N] ').lower()   # Se desejar adicionar outra tabela
        if reiniciar.startswith('s'):
            os.system('cls')
            continue
        break
    os.system('cls')
    print('Muito obrigado pela preferência!')   
    conexao.commit()
    conexao.close()


def adiciona_usuario():

    nome = input('Digite um nome para usuário: ')
    os.system('cls')
    idade = int(input('Digite a sua idade: '))
    os.system('cls')
    senha = input('Defina uma senha: ')
    os.system('cls')

    if nome and idade and senha:
        conexao = Conexao.conexao
        cursor = conexao.cursor()

        cursor.execute("select * from usuario where nome = %s", (nome,))

        usuario = cursor.fetchone()

        if usuario:                                                                 # Verifica se o usuário já está em uso
            print(f'Usuário "{nome}" já está sendo utilizado!\n')
        else:
            cursor.execute("insert into usuario (nome,idade,senha) values (%s,%s,%s)",(nome,idade,senha))   # Adiciona usuário
            conexao.commit()
            print(f'Usuário "{nome}" adicionado com sucesso!')
    else:
        print('Preencha todos os campos!')

def apaga_usuarios():
    conexao = Conexao.conexao

    id = input('Digite o ID que será apagado: ')

    cursor = conexao.cursor()

    cursor.execute('select nome from usuario where id_usuario = %s', (id,))

    usuario = cursor.fetchone()

    if usuario:
        cursor.execute('delete from usuario where id_usuario = %s', (id,))
        print(f'Usuário {usuario} deletado com sucesso!')
    else:
        print('Não foi possível deletar esse usuário!')
    conexao.commit()

def update_usuario():
    conexao = Conexao.conexao
    cursor = conexao.cursor()

    id = input('Digite o ID do usuário que será atualizado!: ')

    while True:
        nome = input('Deseja alterar o seu nome? [S],[N] ').lower()
        if nome.startswith('s'):
            mudancaNome = input('Para qual nome deseja alterar? ')
            cursor.execute('update usuario set nome = %s where id_usuario = %s', (mudancaNome,id))
        os.system('cls')

        idade = input('Deseja alterar a sua idade? [S], [N] ').lower()
        if idade.startswith('s'):
            mudancaIdade = input('Para qual idade deseja alterar? ')
            cursor.execute('update usuario set idade = %s where id_usuario = %s', (mudancaIdade,id))
        os.system('cls')

        senhaInput = input('Deseja alterar a sua senha? [S], [N] ').lower()
        if senhaInput.startswith('s'):
            mudancaSenha = input('Para qual senha deseja alterar? ')
        os.system('cls')

        verificacao_senha = input('Para seguir com as mudanças informe a sua senha antiga: ')
        
        cursor.execute('Select * from usuario where id_usuario = %s', (id,))

        usuario = cursor.fetchone()

        if usuario and verificacao_senha == usuario[3]:
            try:
                cursor.execute('update usuario set senha = %s where id_usuario = %s', (mudancaSenha,id))
                conexao.commit()
                os.system('cls')
                print('Sucesso!!')
            except:
                conexao.commit()
                print('Senha não foi alterada! Mudanças feitas com sucesso!')
                break
        else:
            print('Senha incorreta! Voltando ao início...')
            continue
        break

def procura():
    conexao = Conexao.conexao

    cursor = conexao.cursor()

    tabela = input('Tabela: ')
    coluna = input('Coluna: ')
    nome = input('Nome: ')
    try:
        cursor.execute(f'select * from {tabela} where {coluna} like %s', ('%'+nome+'%',))
        usuario = cursor.fetchall()
        if usuario:
            os.system('cls')
            print(f'Usuário encontrado! \n\n ID - NOME - IDADE - SENHA \n{usuario}')
        else:
            print('Usuário não encontrado!')
    except:
        print('Erro! Verifique se preencheu os campos corretamente!')
    

    
