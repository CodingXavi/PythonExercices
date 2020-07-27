import random

def loop():

    while True:

        ia = random.randint(1, 3)

        print('***************')
        print('*  by 1V4X    *')
        print('*  Choose:    *')
        print('* [1] ROCK    *')
        print('* [2] PAPER   *')
        print('* [3] SCISSOR *')
        print('  [4] EXIT    *')
        print('***************')

        user = int(input("Choose 1, 2 or 3 \n\r"))

        if user == 1:

            if ia == 1:
                print('you choose ROCK')
                print("IA select ROCK, so its draw")
                input("pres enter to restart")

            if ia == 2:
                print('you choose ROCK')
                print(" IA select PAPER, so u lose")
                input("pres enter to restart")

            if ia == 3:
                print('you choose ROCK')
                print("IA select SCISSOR, so u won")
                input("pres enter to restart")

        if user == 2:

            if ia == 1:
                print('you choose PAPER')
                print("IA select ROCK, so you won")
                input("pres enter to restart")

            if ia == 2:
                print('you choose PAPER')
                print(" IA select PAPER, so its draw")
                input("pres enter to restart")

            if ia == 3:
                print('you choose PAPER')
                print("IA select SCISSOR, so u lose")
                input("pres enter to restart")

        if user == 3:

            if ia == 1:
                print('you choose SCISSOR')
                print("IA select ROCK, so you lose")
                input("pres enter to restart")

            if ia == 2:
                print('you choose SCISSOR')
                print(" IA select PAPER, so u won")
                input("pres enter to restart")

            if ia == 3:
                print('you choose SCISSOR')
                print("IA select SCISSOR, so its draw")
                input("pres enter to restart")

        if user == 4:
            break

