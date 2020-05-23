from models import Pessoas, Usuario


def insere_pessoas():
    pessoa = Pessoas(nome='Andressa', idade=27)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    #pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Macedo').first()
    print(pessoa.idade)

def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome=='Marçal').first()
    pessoa.nome = 'Andy'
    # pessoa.idade = 21
    pessoa.save()

def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Teste').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuario(login=login, senha=senha)
    usaurio.save()

def consulta_todos_usuarios():
    usuarios = Usuario.query.all()
    print(usuarios)


if __name__ == '__main__':
    insere_usuario('aiai', '111')
    insere_usuario('UUUUUi', '2222')
    consulta_todos_usuarios()
    #insere_pessoas()
    #consulta_pessoas()
    #altera_pessoas()
    #exclui_pessoas()