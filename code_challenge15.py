import os
isContinue = True
no = 0
while isContinue == True:
    ask = input("\ndo u want triangle? (yes/no): ")

    if ask.lower()== "no":
        os.system("cls")
        print("\tProgram Terminated")
        break
        isContinue = False

    elif ask.lower()== "yes":
        os.system('cls')
        no += 1
        for a in range (1,6):
            for d in range (1,no + 1):
                for b in range (1, a + 1):
                    print ("*", end=" ")

                for c in range ( 6, a, -1):
                    print(" ", end=" ")
            print()
        continue
    else:
        os.system("cls")
        print("invalid input, please try again!")
        continues