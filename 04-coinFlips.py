# This program does 10000 trials of 100 coin flips, counting how many times
# a streak of 6 or more occurs in each trial. Then it displays the percentage
# of trials where a streak of 6 or more heads/tails occured

import random, sys
numberOfStreaks = 0
headsFlipped = 0
tailsFlipped = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    myFlips = []
    for i in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            myFlips.append('H')
        elif flip == 1:
            myFlips.append('T')
        else:
            print('Error')
            sys.exit()

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(100):
        if myFlips[i] == 'H':
            tailsFlipped = 0
            headsFlipped += 1
            if headsFlipped % 6 == 0:
                numberOfStreaks += 1
                break
        elif myFlips[i] == 'T':
            headsFlipped = 0
            tailsFlipped += 1
            if tailsFlipped % 6 == 0:
                numberOfStreaks += 1
                break

print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
