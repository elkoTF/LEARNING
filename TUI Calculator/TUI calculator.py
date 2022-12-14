# Calculator program using text interface

def add(intToAdd):
    inpAdd = float(input("Enter next number: "))
    intInput = intToAdd + inpAdd
    mainMenu(intInput)
    return intInput

def subtract(intToSub):
    inpSub = float(input("Enter next number: "))
    intInput = intToSub - inpSub
    mainMenu(intInput)
    return intInput

def multiply(intToTimes):
    inpTimes = float(input("Enter next number: "))
    intInput = intToTimes * inpTimes
    mainMenu(intInput)
    return intInput

def divide(intToDivide):
    inpDivide = float(input("Enter next number: "))
    if inpDivide == 0:
        print("Error")
    intInput = intToDivide / inpDivide
    mainMenu(intInput)
    return intInput

def clear(intToClear):
    intInput = intToClear * 0
    mainMenu(intInput)
    return intInput
    
def equals(intToOutput):
    print(intToOutput)


def mainMenu(intm):
    print("1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Clear\n6 - Equals...\n7 - Quit\n")
    x = round(intm, 3)
    print(x)
    option = int(input("Choose your operation: "))
    if option == 1:
        add(intm)
    elif option == 2:
        subtract(intm)
    elif option == 3:
        multiply(intm)
    elif option == 4:
        divide(intm)
    elif option == 5:
        clear(intm)
    elif option == 6:
        equals(intm)
    elif option == 7:
        quit()
    else:
        print("Error")
        mainMenu(intm)

def mainOp():
    intInput = float(input("Enter your number: "))
    mainMenu(intInput)
    return intInput

run = True
while run == True:
    intInput = 0
    mainOp()
