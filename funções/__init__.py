from random import choice
from time import sleep
# cores
r = '\033[31m'
y = '\033[33m'
g = '\033[32m'
b = '\033[34m'
c = '\033[m'
#Funções de arquivos
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

arq = 'Cadastros.txt'
if not arquivoExiste(arq):
      criarArquivo(arq)

#Interface
def arte():
    return(f'             {b}||||||||     |||||||||    ||||||||     |||||||||    ||||    ||||\n'
          f'             |||   |||    |||||||||    |||   |||    |||||||||    ||||    ||||\n'
          f'             |||   |||    |||          |||   ||     |||          ||||    ||||\n'  
          f'             ||||||||     ||||||||     |||||||      ||||||||     ||||    ||||\n' 
          f'             ||||         |||          || ||        |||          ||||    ||||\n'
          f'             ||||         |||||||||    ||   ||      |||          ||||    ||||\n'
          f'             ||||         |||||||||    ||    |||    |||          ||||    ||||||||||{c}')


def linhas(msg):
    linha = print('-' * msg)


def instrucões():
    sleep(2)
    print(f'{b}INSTRUÇÕES BÁSICAS{c}'.center(100))
    linhas(100)
    print(f'Bem vindo ao {b}PERFIL{c}, um divertido jogo que testa seus conhecimentos e sua capacidade de dedução.\n'
          'A cada rodada, uma carta com um perfil secreto é sorteada, depois, o jogador receberá dicas sobre o \n'
          'perfil secreto em questão durante a sua rodada.\n'
          f'Iniciando o jogo, sortearei 1 modelo de carta dizendo que posso ser uma{b} "Pessoa, Coisa, Lugar ou Ano"{c}.\n'
          'Cada carta terá 8 dicas para você tentar adivinhar a resposta.\n'
          'Quanto menos dicas você precisar, maior será a sua pontuação.\n'
          'Ao acertar 4 dicas, você entrará no ranking do jogo.\n'
          'De quantas dicas você precisa? Divirta-se.')
    print(f'{b}Carregando menu principal{c}',end='')
    ponto = ('.')
    sleep(13)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto, end='')
    sleep(1)
    print(ponto)


def menu():
    print(f'{b}MENU{c}'.center(100))
    print(f'{g}1{c} - Iniciar'.center(83))
    print(f'{g}2{c} - Ranking de pontuações'.center(98))
    print(f'{g}3{c} - Sair'.center(80))


# Cartas
# Pessoas
Neymar = (('Nasci em 5 de fevereiro de 1992'),
          ('Iniciei na minha profissão quando era criança'),
          ('Já estrelei inúmeras propagandas na TV.'),
          ('Sou Júnior, mas apenas no nome.'),
          ('Os meninos adoram imitar meus cortes de cabelo.'),
          ('Sou o pai do Davi Lucca.'),
          ('Em 2013, fui para o Barcelona.'),
          ('Meu namoro com a atriz Bruna Marquezine causou frenesi na imprensa.'),
          ('Neymar').upper())
Harry_Potter = (('Na vida real tambem sou britânico'),
                ('Meus filmes renderam 8 grandes sucessos do cinema.'),
                ('Morei meus primeiros 10 anos de vida com meus tios "Dursleys"'),
                ('Passei minha infância domindo de baixo de uma escada.'),
                ('Rony e Hermione são meus melhores amigos.'),
                ('O Lord das trevas é meu inimigo'),
                ('Minha casa é Grifinória'),
                ('Lílian e James são meus pais'),
                ('HARRY_POTTER'))
Pessoa = ((Neymar), (Harry_Potter))
#COISAS
EstatuadaLiberdade = (('Sou patrimônio mundial da UNESCO nos Estados Unidos'),
                      ('Sou um dos marcos históricos da engenharia civil'),
                      ('já apareci em centenas de filmes norte americanos'),
                      ('Fui concluída em julho de 1884. Após ser desmontada em 350 peças,\n'
                       ' e embalada em 214 caixas para transporte'),
                      ('fui colocada a bordo da fragata francesa Isere, que a transportou me até os Estados Unidos.'
                       'Cheguei em Nova York um ano depois'),
                      ('Frédéric Auguste Bartholdi foi meu arquiteto'),
                      ('Fui um presente dado aos Estados Unidos pelo povo da França'),
                      ('Eu represento a liberdade'),
                      ('ESTATUA_DA_LIBERDADE'))
Mineirão = (('Sou o maior estádio do sudeste fora do eixo RJ-SP'),
            ('Aqui, já foram conquistadas 3 Libertadores da américa'),
            ('Em 2014 Mancharam a minha história de belas partidas de futebool'),
            ('Sou conhecida pelo excelente feijão "Tropeiro"'),
            ('Da pampulha, todos conseguem aprenciar a minha beleza'),
            ('Sou homenageada pelo Governador Magalhães Pinto'),
            ('Sou moderna por dentro, e antiga por fora'),
            ('Passei por uma grande reforma concluída em 2012'),
            ('MINEIRAO'))
Coisas = (EstatuadaLiberdade, Mineirão)
#ANO
A1945 = (('Em 12 de abril O Presidente dos Estados Unidos Franklin Delano Roosevelt\n'
          ' morre em decorrência de uma hemorragia cerebral.'),
        ('Eurico Gaspar Dutra é eleito presidente do Brasil.'),
        ('A Organização das Nações Unidas é fundada.'),
        ('As cidades de Hiroshima e Nagasaki foram bombardeadas'),
        ('Declarada independência da Indonésia, mas só é reconhecida em 27 de dezembro de 1949.'),
        ('Termina a Segunda Guerra Mundial.'),
        ('Nasce o cantor e compositor Raul Seixas'),
        ('Sou um ano comum do século XX'),
        ('1945'))
A2000 = (('A Sony lança seu videogame, Playstation 2 no Japão.'),
         ('Avião Concorde da Air France cai, nas proximidades de Gonesse, deixando 113 mortos.'),
         ('George Bush é eleito presidente dos Estados Unidos, vencendo o candidato democrata Al Gore.'),
         ('Sport Club Corinthians Paulista se conssagra campeão Mundial de Clubes FIFA'),
         ('Indiana Lara Dutta é eleita Miss Universo.'),
         ('Sequestro do ônibus 174, no Rio de Janeiro.'),
         ('Lançamento do jogo virtual de interação online Habbo Hotel.'),
         ('Nascia o jogador de futebol brasileiro Vinicius Junior.'),
         ('2000'))
Ano = ((A1945), (A2000))
#LUGAR
Australia = (('um país do hemisfério sul, localizado na Oceania'),
             ('Sou um páis semiárido ou desértico.'),
             ('Aqui, Sydney nao é uma pessoa.'),
             ('Hugh Jackman nasceu aqui.'),
             ('Tenho a maior população costeira do mundo'),
             ('Tenho como patrimônio o filme "Canguru Jack"'),
             ('Fui a primeira nação independente a permitir o voto feminino'),
             ('A minha fauna é única, 80% das minhas espécies somente são encontradas aqui.'),
             ('AUSTRALIA'))
Vaticano = (('Sou o único país inteiro a ser reconhecido como Patrimônio Mundial da Humanidade pela UNESCO.'),
            ('Sou o menos país do mundo'),
            ('apenas 44 hectares e 800 habitantes'),
            ('Nascer aqui não garante cidadania a ninguém. Para isso, é preciso trabalhar aqui.'),
            ('Meus habitantes consomem  54,26 litros de vinho por ano'),
            ('Sou considerada a cidade com maior criminalidade do mundo'),
            ('Minha lingua oficial é o Italiano'),
            ('A Menor estrada ferroviária do mundo se encontra aqui, são 900 metros construidos e funcionais.'),
            ('VATICANO'))
Lugar = (Vaticano, Australia)
Opções = (('COISA'), ('PESSOA'), ('ANO'), ('LUGAR'))

def pontuação():
    print(f'{b}NOME{c}              {y}PONTUAÇÃO{c}'.center(112))
    lerAquivo(arq)
    linhas(100)
    voltar = input(f'{b}Enter para voltar{c}'.rjust(63))
    linhas(100)


def jogo():
    encerrar = 'S'
    cont = 8
    total = 0
    tentativas = 0
    while encerrar in 'S':
        tentativas += 1
        resposta = 'n'
        sleep(1)
        print(f'{b}SORTEANDO A CARTA{c}'.center(100))
        sleep(2)
        sorteio = choice(Opções)
        linhas(100)
        print(f'SOU UM(A) {b}{sorteio}{c}'.center(100))
        linhas(100)
        sleep(1.5)
        if sorteio == Opções[1]:
            carta = choice(Pessoa)
            while True:
                dica = int(input('PEÇA UMA DICA DE 1 A 8: ').rjust(40))
                linhas(100)
                print(f'Dica de número {dica}: {b}{carta[dica - 1]}{c}')
                resposta = input('Resposta : ').replace('Á', 'A').replace('Ã', 'A').replace(' ', '_').upper()
                cont -= 1
                if resposta == carta[8]:
                    print(f'{b}PARABÉNS{c}! VOCÊ ACERTOU! Conseguiu {cont} pontos')
                    linhas(100)
                    sleep(1.5)
                    break
                else:
                    print(f'{r}Errou{c}, Tente novamente.')
                    linhas(100)
        if sorteio == Opções[0]:
            carta = choice(Coisas)
            while True:
                dica = int(input('PEÇA UMA DICA DE 1 A 8: ').rjust(40))
                linhas(100)
                print(f'Dica de número {dica}: {b}{carta[dica - 1]}{c}')
                resposta = input('Resposta: ').replace('Á', 'A').replace('Ã', 'A').replace(' ', '_').upper()
                cont -= 1
                linhas(100)
                if resposta == carta[8]:
                    print(f'{b}PARABÉNS!{c} VOCÊ ACERTOU! Conseguiu {cont} pontos')
                    linhas(100)
                    sleep(1.5)
                    break
                else:
                    print(f'{r}Errou{c}, Tente novamente.')
                    linhas(100)
        if sorteio == Opções[2]:
            carta = choice(Ano)
            while True:
                dica = int(input('PEÇA UMA DICA DE 1 A 8: ').rjust(40))
                linhas(100)
                print(f'Dica de número {dica}: {b}{carta[dica - 1]}{c}')
                resposta = input('Resposta : ').replace('Á', 'A').replace('Ã', 'A').strip().upper()
                cont -= 1
                linhas(100)
                if resposta == carta[8]:
                    print(f'{b}PARABÉNS!{c} VOCÊ ACERTOU! Conseguiu {cont} pontos')
                    linhas(100)
                    sleep(1.5)
                    break
                else:
                    print(f'{r}Errou{c}, Tente novamente.')
                    linhas(100)
        if sorteio == Opções[3]:
            carta = choice(Lugar)
            while True:
                dica = int(input('PEÇA UMA DICA DE 1 A 8: ').rjust(40))
                linhas(100)
                print(f'Dica de número {dica}: {b}{carta[dica - 1]}{c}')
                resposta = input('Resposta : ').replace('Á', 'A').replace('Ã', 'A').replace(' ', '_').upper()
                cont -= 1
                linhas(100)
                if resposta == carta[8]:
                    print(f'{b}PARABÉNS{c}! VOCÊ ACERTOU! Conseguiu {cont} pontos')
                    linhas(100)
                    sleep(1.5)
                    break
                else:
                    print(f'{r}Errou{c}, Tente novamente.')
                    linhas(100)
        total = cont + total
        cont = 8
        if tentativas == 3:
            print(f'Chegamos no final e você conseguiu {total} pontos! Parabéns.')
            linhas(35)
            sleep(2)
            print('Iremos realizar o seu cadastro')
            linhas(35)
            sleep(2)
            nome = (input('Digite seu primeiro nome: '))
            a = open(arq, 'at')
            a.write(f'{nome};{total}\n')
            a.close()
            linhas(35)
            sleep(1)
            print(f'Sua partida foi finalizada! Retornando ao {b}menu{c} principal do jogo...')
            sleep(2)
            break
        linhas(100)
    encerrar = 'S'