from game_functions import start, rules, user, main, play_again, username
from time import sleep

again = True
your_name = username()
while again:
    start(your_name)
    sleep(0.7)
    rules()
    sleep(0.7)
    player = user()
    sleep(0.7)
    main(player)
    sleep(0.7)
    again = play_again(your_name)