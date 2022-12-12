from random import randint as RI

take_sweet = 0
total_sweet = 150
player = 0
bot = 0

def start_game():
    print('На столе лежит 150 конфет. Победит тот, кто заберет последние конфеты. За раз можно взять не более 28 конфет.')
    print()
    who_s_first()

def who_s_first():
    random_number = RI(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()

def player_turn():
    global take_sweet
    global total_sweet
    global player
    print(f'Ваш ход. На столе сейчас {total_sweet} конфет')
    take_sweet = int(input('Сколько конфет вы возьмете? '))
    while take_sweet > 28 or take_sweet< 0 or take_sweet > total_sweet:
        take_sweet = int(input('Попробуйте взять другое количество конфет: '))
    total_sweet -= take_sweet
    player += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print('Вы победили!')

def bot_turn():
    global take_sweet
    global total_sweet
    global bot
    take_sweet = total_sweet % 29 if total_sweet != 0 else RI(1, 28)
    total_sweet -= take_sweet
    bot += take_sweet
    print(f'Бот взял {take_sweet} конфет. На столе осталось {total_sweet} конфет')
    if total_sweet > 0:
        player_turn()
    else:
        print('Бот победил!')

