# bull and cow


import random


class game:
    table = []
    times = 0
    player = []

    def creat():
        nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(4):
            game.table.append(random.choice(nums))

        #print(game.table)

    def guess():
        repetition = ['first', 'seceond', 'third', 'fourth']
        print('guess:')

        while True:
            for i in repetition:
                play = int(input(f'''{i} number: '''))
                game.player.append(play)

            game.times += 1

            if (game.table == game.player) == True:
                print(f'''You win
    You tried for {game.times} times''')
                break

            else:
                for j in range(len(game.player)):
                    for i in range(len(game.table)):
                        if j == i:
                            if game.table[i] == game.player[j]:
                                print('You have a cow')

                        elif i != j:
                            if game.table[i] == game.player[j]:
                                print('You have a bull')
            game.player.clear()
            print()


print('Let`s play hero!!!')
game.creat()
game.guess()

while True:
    if (game.table == game.player) == True:
        a = input('Do you wanna play again?  (yes-> y) or (no-> n) : ')
        a = a.lower()

    if a == 'y':
        game.table.clear()
        game.player.clear()
        game.creat()
        game.guess()
    else:
        print('Good bye!')
        break
