import argparse

def add(num1, num2):
    return num1 + num2


# print("Hello world")
# myName = input("What is your name ")
# myVar = input("Enter your number ")

# n1 = int(input("Please enter first number "))
# n2 = int(input("Please enter second number "))

# print("The sum of two numbers are " + str(add(n1, n2)))


# helloWorld(myName, myVar)

def main():
    inputLoop = True
    # parser = argparse.ArgumentParser(description='Process some integers.')
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                    help='an integer for the accumulator')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                    const=sum, default=max,
    #                    help='sum the integers (default: find the max)')

    # args = parser.parse_args()
    # print(args.accumulate(args.integers))
    while inputLoop:
        validInput = False
        while not validInput:
            try:
                n1 = int(input("Please enter the first number "))
                n2 = int(input("Please enter the second number "))
                print("The sum of two numbers are " + str(add(n1, n2)))
                validInput = True
            except:
                print("Invalid input")
        yesno = input("Do you want to enter another number, Y or N ")
        if yesno != "y" or yesno == "Y":
            inputLoop = False
main()