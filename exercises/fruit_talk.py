import random
fruits = ["banana", "apple", "pineapple", "pear", "berries"]
def main_program():
    name = str(input("Hello, what's your name?: "))
    print("Nice to meet you " + name) #CHALLENGE TASK (relay info)

    # done_asking = False

    # while(done_asking == False):
    likesFruit = str.lower(input("Do you like fruit " + name + "? "))

    #CHALLENGE TASK
        # if(likesFruit == "yes"):

        # elif(likesFruit == "no")


    print("My favourite fruit is " + randomFruit() + " and " + randomFruit())

def randomFruit():
    return random.choice(fruits)

main_program()