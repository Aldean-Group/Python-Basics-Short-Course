#While loop
isHappy = False
while(not isHappy):
    ask_user = str.lower(input("Are you happy?(yes/no): "))
    if ask_user == "yes":
        isHappy = True
    else:
         isHappy = False

print("Awesome, i'm glad you're finally happy!")

#For loop(s)
names = ("John", "Rowan", "Bob", "Janet") #this can be any collection!
for name in names:
    print("Hello " + name)

for x in range(0,5):
    print(x)

for letter in "chicken":
    print(letter)


    