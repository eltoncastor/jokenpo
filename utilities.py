from os import system, name


class Colors():
    yellow = '\033[33m'
    yellowBold = '\033[33;1m'
    yellowBgBold = '\033[1;30;43m'
    cyan = '\033[36m'
    cyanBold = '\033[36;1m'
    cyanBgBold = '\033[1;30;46m'
    green = '\033[32m'
    greenBold = '\033[32;1m'
    greenBgBold = '\033[1;30;42m'
    red = '\033[31m'
    redBold = '\033[31;1m'
    redBgBold = '\033[1;41m'
    purple = '\033[35m'
    purpleBold = '\033[35;1m'
    purpleBgBold = '\033[1;30;45m'
    
    reset = '\033[m' ###

cor = Colors()


class Hr():
    yellow = cor.yellowBgBold + ('='*50) + cor.reset
    green = cor.greenBgBold + ('='*50) + cor.reset
    cyan = cor.cyanBgBold + ('='*50) + cor.reset
    red = cor.redBgBold + ('='*50) + cor.reset
    purple = cor.purpleBgBold + ('='*50) + cor.reset


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def br():
    print()



    
        
        
