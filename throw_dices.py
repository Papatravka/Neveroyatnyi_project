import random

def throw_dices():
    first_dice = range(1, 7)
    second_dice = range(1, 7)
    counter = 0
    while True:
        counter = counter + 1
        elem , elem2 = random.choice(first_dice), random.choice(second_dice)
        summ_elem = elem + elem2
        if summ_elem == 8:
            print(elem, elem2, counter)
            break

throw_dices()