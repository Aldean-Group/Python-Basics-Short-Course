import random

fruits = ["banana", "apple", "pineapple", "pear", "berries"]

def main_program():

    name = str(input("Hello, what's your name?: "))

    print("Hello " + name)

    likes_fruit = str.lower(input("Do you like fruit " + name + "?(yes/no): "))
    while(not(likes_fruit == "yes" or likes_fruit == "no")):
        likes_fruit = str.lower(
            input("Do you like fruit " + name + "?(yes/no): "))

    if(likes_fruit == "yes"):
        favourite_fruits = []
        likes_random = str()  # it's a string
        # while it isnt "stop" and the list still has choices
        while(not(likes_random == "stop") and len(fruits) > 0):
            random_fruit = randomFruit()  # get a random fruit
            likes_random = str.lower(
                input("Do you like " + random_fruit + "?(yes/no/stop): "))  # ask about it
            if likes_random == "yes":
                # add it to the list if they say yes
                favourite_fruits.append(random_fruit)

            # otherwise remove it to never ask again and loop back around to the top.
            fruits.remove(random_fruit)

        print("Ok we'll stop! Here's what you like: ")
        print(favourite_fruits)

    else:
        print("Oh, wow! I like some fruits but not all of them.")


def randomFruit():
    return random.choice(fruits)


main_program()
