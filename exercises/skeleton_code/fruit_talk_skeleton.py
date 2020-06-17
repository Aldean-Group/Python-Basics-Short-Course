import random  # this line will be explained in the course

fruits = ["banana", "apple", "pineapple", "pear", "berries"]

name = str(input("Hello, what's your name?: "))

random_fruit = random.choice(fruits)
print("I like " + random_fruit + "!")