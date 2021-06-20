from utilidades import br, clear, Colors, Hr
from random import choice
from time import sleep


cor = Colors()
linha = Hr()


def username():
    clear()
    print(cor.yellowBold)
    name = str(input(f'Qual seu nome? {cor.reset}').title())
    return name


def start(name):
    clear()
    print(linha.yellow)
    br()
    print(cor.cyanBold + f'Olá, {cor.yellowBold}{name}{cor.cyanBold}!'.center(60) + cor.reset)
    print(cor.cyanBold + 'SEJA BEM VINDO AO JOGO DE PEDRA, PAPEL E TESOURA!'.center(50) + cor.reset)
    br()
    print(f'{cor.green}PEDRA {cor.reset}vence de {cor.green}TESOURA'.center(61))
    print(f'{cor.green}TESOURA {cor.reset}vence de {cor.green}PAPEL'.center(58))
    print(f'{cor.green}PAPEL {cor.reset}vence de {cor.green}PEDRA'.center(60))
    br()
    print(linha.yellow)
    br()


def rules():
    print(f'{cor.reset}DIGITE'.center(52))
    print(f'{cor.yellowBold}[1] {cor.reset}para {cor.yellowBold}PEDRA'.center(63))
    print(f'{cor.yellowBold}[2] {cor.reset}para {cor.yellowBold}PAPEL'.center(63))
    print(f'{cor.yellowBold}[3] {cor.reset}para {cor.yellowBold}TESOURA'.center(65) + cor.reset)
    br()


def user():
    player = 0
    while True:
        try:
            print(cor.greenBold)
            player = int(input(f'Sua opção: {cor.reset}'))
        except ValueError:
            br()
            print(cor.redBgBold + 'ERRO!'.center(50) + cor.reset)
            print(cor.redBold + 'Digite apenas 1, 2 ou 3'.center(50) + cor.reset)
            br()
        break
    return player


def main(user):
    bot = choice([1,2,3])
    
    choices =  {1:'PEDRA',
                2:'PAPEL',
                3:'TESOURA'}
    
    if (user == 1 and bot == 3) or (user == 2 and bot == 1) or (user == 3 and bot == 2):
        br()
        print(linha.green)
        br()
        print(f'Eu escolhi{cor.cyanBold} {choices[bot]}{cor.reset}, você escolheu{cor.cyanBold} {choices[user]}'.center(65))
        br()
        print(cor.greenBold + 'Parabéns, você me venceu!'.center(50))
        br()
        print(linha.green)
        
    elif user == bot:
        br()
        print(linha.yellow)
        br()
        print(f'Eu escolhi{cor.greenBold} {choices[bot]}{cor.reset}, você escolheu{cor.greenBold} {choices[user]}'.center(65))
        br()
        print(cor.yellowBold + 'Eita! Empatamos!'.center(50))
        br()
        print(linha.yellow)
    
    elif (user == 1 and bot == 2) or (user == 2 and bot == 3) or (user == 3 and bot == 1):
        br()
        print(linha.red)
        br()
        print(f'Eu escolhi{cor.purpleBold} {choices[bot]}{cor.reset}, você escolheu{cor.purpleBold} {choices[user]}'.center(65))
        br()
        print(cor.redBold + 'Que pena, você perdeu!'.center(50) + cor.reset)
        br()
        print(linha.red)
    
    elif user > 3:
        br()
        print(cor.redBgBold + 'ERRO!'.center(50) + cor.reset)
        print(cor.redBold + 'Digite apenas 1, 2 ou 3'.center(50) + cor.reset)
        br()
        

def play_again(name):
    while True:
        br()
        your_choice = str(input(f'{cor.yellow}Você quer jogar novamente? {cor.yellow}[S para sim / N para não] {cor.reset}')).lower()
        if (your_choice == 's') or (your_choice == 'n'):
            break
        else:
            br()
            print(cor.redBgBold + 'ERRO!'.center(50) + cor.reset)
            print(cor.redBold + 'Responda apenas com S ou N'.center(50) + cor.reset)
            br()
            
    if your_choice == 's':
        br()
        print(linha.green)
        br()
        sleep(0.5)
        print(cor.greenBold + f'Ok! Vamos continuar,{cor.cyanBold} {name}{cor.green}!'.center(58) + cor.reset)
        sleep(0.5)
        print(cor.greenBold + 'Carregando...'.center(50) + cor.reset)
        br()
        print(linha.green)
        sleep(1.5)
        return True
    else:
        br()
        print(linha.red)
        br()
        sleep(0.5)
        print(cor.redBold + f'Ah, que pena...'.center(50) + cor.reset)
        sleep(0.5)
        print(cor.redBold + f'Até a próxima,{cor.cyanBold} {name}{cor.redBold}!'.center(62) + cor.reset)
        br()
        print(linha.red)
        sleep(2)
        return False