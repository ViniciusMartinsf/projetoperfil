from funções import *
from time import sleep
import pygame
arq = 'Cadastros.txt'
if not arquivoExiste(arq):
      criarArquivo(arq)
print(f'{r}INICIANDO...{c}')
pygame.init()
pygame.mixer.music.load('musicaintro.mp3')
sleep(2)
pygame.mixer.music.play()
linhas(100)
print(f'{arte()}')
linhas(100)
sleep(2)
print(f'Criado por {b}Vinicius Martins de Freitas!{c}')
sleep(1.7)
print('Linkedin -> https://www.linkedin.com/in/vin%C3%ADcius-martins-60a7b1226/ \n'
      'GitHub -> https://github.com/ViniciusMartinsf/ \n'
      'Whatsapp -> https://api.whatsapp.com/send?phone=553399433524&text=sua%20mensagem')
linhas(100)
instrucões()
sleep(2)
linhas(100)
while True:
      menu()
      try:
            escolha_opcão = int(input('Digite a opção: '.rjust(52)))
            linhas(100)
            if escolha_opcão == 3:
                  print(f'{r}Encerrando o jogo...{c}')
                  sleep(3)
                  break
            if escolha_opcão == 2:
                  pontuação()

            if escolha_opcão == 1:
                  print(f'{b} EMBARALHANDO AS CARTAS {c}'.center(100))
                  linhas(100)
                  jogo()
      except: print(f'{r}Opção inválida{c}')