#Snake water gun
import random
def game(Comp, you):
    if Comp == you:
        return None
    elif Comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif Comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
            
Comp = input("Comp turn: Snake(s), Water(w), Gun(g)?")
Randr = random.randint(1,3)
if Randr ==1:
    Comp = 's'
elif Randr ==2:
    Comp = 'w'
elif Randr ==3:
    Comp = 'g'


you = input ("Player turn: Snake(s), Water(w), Gun(g)?")
a = game(Comp, you)
print(f"Computer choses {Comp}")
print(f"You choose {you}")
if a == None:
    print("The game is a tie!!")
elif a :
    print("You win")
else:
    print("You lose")