import random

x = "r"
print("---------DICE ROLLINGR GAME----------")
while x == "r":
    randNum = random.randint(1,6)
    user = input("Press r to Roll the Dice : ")
    print("\n")
    if randNum == 1:
        print("-------")
        print("       ")
        print("   o   ")
        print("       ")
        print("-------")
    
    elif randNum == 2:
        print("-------")
        print(" o     ")
        print("       ")
        print("     o ")
        print("-------")

    elif randNum == 3:
        print("-------")
        print(" o     ")
        print("   o   ")
        print("     o ")
        print("-------")

    elif randNum == 4:
        print("-------")
        print(" o   o ")
        print("       ")
        print(" o   o ")
        print("-------")
    elif randNum == 5:
        print("-------")
        print(" o   o ")
        print("   o   ")
        print(" o   o ")
        print("-------") 
    else:
        print("-------")
        print(" o o o ")
        print("       ")
        print(" o o o ")
        print("-------")

   
    
