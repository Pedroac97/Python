from time import sleep  # sleep: pausa dramaticas
from pygame import mixer  # mixer: musicas
from random import randint  # randint: sorteia numero
from datetime import date

# pacotes

print('\033[1;36;m-=-\033[m' * 20)
print('Dia:', date.today().day, '/', date.today().month, '/', date.today().year)
print('Textos em \033[1;34mazul são perguntas\n\033[mem \033[1;32mverde ACERTOS\033[m e \033[1;31mERROS em vermelho\033[m')
print('Perguntas objetivas são respondidas com \033[7;30msim\033[m ou \033[7;30mnão\033[m')
play = str(input('\033[1;34mVocê esta pronto para os desafios? ')).lower().strip()
print(play)
print('\033[1;36m-=-\033[m' * 20)
if play in 'sim s ok pode go vamos la':
    print('uma musica pra ficar mais TOP')
    mixer.init()
    mixer.music.load('audio.mp3')
    mixer.music.play()

    # Pergunta nome
    nome = str(input('\033[1;34mQual é seu nome completo? ')).strip().title()
    id = nome.split()
    pontos = 0
    nickname = str(id[0] + ' ' + id[len(id) - 1])
    a = str(input('Posso te chamar de: {}?\033[m '.format(nickname))).strip().lower()
    if a in 'sim s ok pode go vamos la':
        print('OK vamos la')
        sleep(2)
    else:
        nickname = str(input('\033[1;34mOK, como quer ser chamado?\033[m '))
        print('agora vamos la...')
    print('{} apartir de agora as perguntas valeram pontos:\n\033[1;32mAcertos:+10\n\033[1;31mErros:-5'.format(nickname))
    sleep(4)
    print('\033[1;36m-=-\033[m' * 20)

    # desafio 1 numeros aleatorios
    print('Desafio 1')
    print('\033[1;34mVou pensar em um numero entre 1 e 10 tente adivinhar!!')
    ba = randint(1, 10)
    b = tentativas = 0
    while ba == b:
        b = int(input('Em que numero eu pensei?:\033[m '))
        bb = ba == b
        print('Pensando...')
        sleep(2)
        print(
            '\033[1;32mParabéns você acertou e ganho +10 pontos' if bb else '\033[1;31mPeeeem... errou -5 pontos eu pensei em {} e você falou {}'.format(
                ba, b))
        print('\033[mpontos = {}'.format(pontos))
    if bb:
        pontos +=10
    else:
        pontos -=5

    print('\033[1;36m-=-\033[m' * 20)
    # desafio 2
    print('desafio 2')
    print('EM CONSTRUÇÃO')
    print('\033[1;36m-=-\033[m' * 20)
else:
    print('OK!! Quando quiser só dar o play')
print('Autor: Pedro alves cordeiro.')
