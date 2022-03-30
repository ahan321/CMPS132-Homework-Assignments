import random


class Bear:
    def __init__(self):
        self.type = "Bear"


class Fish:
    def __init__(self):
        self.type = "Fish"


# Constructing the river with 100 elements.

def create_animal(river):
    for x in range(999):
        ticker = random.randint(0, 2)
        if ticker == 0:
            new_animal = Bear()
        elif 1:
            new_animal = Fish()
        else:
            new_animal = None
        river.append(new_animal)


river = []
create_animal(river)

while True:
    for i in range(len(river) - 1):
        print(river[i].type)
        ticker = random.randint(0, 1)
        if ticker == 0:
            ticker2 = random.randint(0, 1)
            if ticker2 == 0:
                if type(river[i]) == type(river[i - 1]):
                    checker = False
                    while checker == False:
                        ticker = random.randint(0, len(river))
                        if river[ticker] == None:
                            river[ticker] = river[i]
                elif river[i - 1] == None:
                    temp = river[i]
                    river[i] = None
                    river[i - 1] = river[i]
                else:
                    if river[i - 1].type() == "fish":
                        river[i - 1] = None
                    else:
                        river[i - 1] = None
            else:
                if type(river[i]) == type(river[i + 1]):
                    checker = False
                    while checker == False:
                        ticker = random.randint(len(river))
                        if river[ticker] == None:
                            river[ticker] = river[i]
                elif river[i + 1] == None:
                    temp = river[i]
                    river[i] = None
                    river[i + 1] = river[i]
                else:
                    if river[i + 1].type() == "fish":
                        river[i + 1] = None
                    else:
                        river[i + 1] = None