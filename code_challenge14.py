#continue to ask user for a number
#enter a number
#enter a number
#enter a number
#enter a number
#loop has terminated
#the sum of all the numbers given is it

tuloy = True
total = 0

while tuloy == True:
    num = eval(input("\nenter a number: "))

    if num ==0:
        print("\n\tProgram Terminated")
        print(f"\nThe total of your numbers are {total}")
        break

    else:
        total += num
        continue