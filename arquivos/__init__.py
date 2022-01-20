def arquivoExiste(nome):
    try:
        a = open(nome, 'rt+')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('erro na criação do arquivo')

def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
         t = 0
    else:
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]}'.rjust(39),f'               {dado[1]}')
