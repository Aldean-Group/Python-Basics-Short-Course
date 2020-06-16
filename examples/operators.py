#Arithmetic operators
num_one = 10 + 20
num_two = 100 - 80
num_three = 50 * 2
num_four = 103 / 4
num_five = 10 % 3 #modulus returns the remainder (in this case num_five is 1)
num_six = 2**2
num_seven = 103 // 4

print(num_four) #normal division
print(num_seven) #floor division

#Membership operators
fruits_tuple = ("orange", "banana", "kiwi")
fruit = "banana"
#in
print("\n" + "in: ")
print(fruit in fruits_tuple) #prints True

#not in
print("not in: ")
print(fruit not in fruits_tuple) #prints False because it is present

#Assignment operators (print x in the correct place to see their impact)
x = 5
x += 1
x -= 3
x *= 2
x /= 3
x %= 1
#this just a few of the assignment operators

#Logical operators (try changing what a/b's values are to see how it impacts the conditions)
a = 5
b = 10
c = a

#and
if a == 5 and b == 10:
    print("\n" + "Nice use of 'and'")

#or
if a == 5 or a == 20:
    print("Nice use of 'or'")

#not (reverse the result of the brackets)
if not(a == 10):
    print("Nice use of 'not'")

#combining operators
if not(a==2) and not(a==4 or a==7):
    print("Awesome combo!" + "\n")

#Membership operators
#is
print(a is c) #prints True
c = 5.0
print(a is c) #prints False as it isn't a, it is just the same data
print(a == c) #prints True still

#is not
print(a is not b) #prints True