
print("----------------------------------------------------------")
print("Welcome to the simple integral calculator built in Python!")
print("----------------------------------------------------------")

print("We will be using the form: ax^b")

def storeFunction():
    coefficient = int(input("What is the coefficient of your slope?: "))
    exponent = int(input("What is the exponent of your slope?: "))
    function = f"Your function is: {coefficient}x^{exponent}"
    print(function)
    return coefficient, exponent  

def findBoundaries():
    lowerX = int(input("What is the lower x boundary?: "))
    upperX = int(input("What is the upper x boundary?: "))
    boundaries = f"Your boundaries are from x = {lowerX} to x = {upperX}"
    print(boundaries)
    return lowerX, upperX  

def integrate(coefficient, exponent, lowerX, upperX):
    if exponent == -1:
        print("Integration for x^-1 involves natural log (ln) and is not supported in this calculator.")
        return

    newExponent = exponent + 1
    newCoefficient = coefficient / newExponent
    

    integralUpper = newCoefficient * (upperX ** newExponent)
    integralLower = newCoefficient * (lowerX ** newExponent)
    
    finalIntegral = integralUpper - integralLower
    finalAnswer = f"The integral of {coefficient}x^{exponent} from x = {lowerX} to x = {upperX} is {finalIntegral}."
    print(finalAnswer)

choice = str(input("Would you like to use the calculator?: ")).strip().lower()
if choice == "yes":
    c, e = storeFunction()
    l, u = findBoundaries()
    integrate(c, e, l, u) 
else:
    print("Thanks for visiting!")
