#Basic Conditions
number1 = 500
number2 = 230

#Short one line if statement
if number1 > number2: print("Oh cool!")

#Short one line if, else statement (ternary conditional)
print("Oh that is impressive!") if number1 > 3000 else print("Oh so it isn't greater than 3000!")

#Regular if, elif, else statements
if number1 > number2:
    print("Damn " + str(number1) + " is greater than " + str(number2))
elif number1 > 1000:
    print("Damn " + str(number1) + " is greater than 1000!")
#remember here you can add as many elif clauses as you want!
else:
    print(str(number1) + " isn't that mighty! haha!")