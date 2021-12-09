print("Welcome to Tresure Island.")
print("You mission is to find the treasure")
choice1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.").lower()

if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' tp wait for a boat."
                    "Type 'swim' to swim across").lower()
    if choice2 == "wait":
        choice3 = input(
            "escolha a casa que tu quer ir. Azul, Amarelo ou Vermelho").lower()
        if choice3 == "red":
            print("Game Over")
        elif choice3 == "yellow":
            print("Ganhou")
        elif choice3 == "blue":
            print("Game Over")
        else:
            print("Game Over")

    else:
        print(" You got attacked by an angry shark. Game Over")
else:
    print("Morreu, Game Over")
