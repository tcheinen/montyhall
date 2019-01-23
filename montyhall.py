import random

NUMBER_TO_SIMULATE = 100000

shuffled = [[False, False, True] for x in list(range(NUMBER_TO_SIMULATE))]
[random.shuffle(x) for x in shuffled]


def pick_dont_repick(list):
    count = 0
    for i in list:
        if i[random.randint(0,2)] == True:
            count += 1
    return count

def pick_with_repick(list):
    count = 0
    for i in list:
        choice = random.randint(0,2)
        removed = 0
        if i[0] == False:
            i[0] = None
        else:
            i[1] = None
            removed = 1
        possible = [0, 1, 2]
        if choice == removed:
            possible.remove(removed)
            choice = random.choice(possible)
        else:
            possible.remove(removed)
            possible.remove(choice)
            choice = possible[0]
        if(i[choice] == True):
            count += 1
    return count
print("Monty Hall problem was simulated using a sample of size: {}".format(NUMBER_TO_SIMULATE))
print("Without repick, {0:.0%} were correct".format(pick_dont_repick(shuffled)/NUMBER_TO_SIMULATE))
print("With repick, {0:.0%} were correct".format(pick_with_repick(shuffled)/NUMBER_TO_SIMULATE))
