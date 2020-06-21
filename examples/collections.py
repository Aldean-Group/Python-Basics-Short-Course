#LIST OPERATIONS WE COVERED
fruit_list = ["apple", "orange", "banana"] #Declaring a list
fruit_list.append("chicken") #Adding to a list
fruit_list.insert(0, "mango") #Inserting to a given index

three_numbers = [1,2,3]
another_three = [4,5,6]
print(another_three + three_numbers) #Joining lists together
three_numbers.extend(another_three) #Extending a list with another
print(three_numbers)

#TUPLE OPERATIONS WE COVERED
fruit_tuple = ("tomato", "lemon", "lime") #Declaring a tuple

#COMMON OPERATIONS
print(fruit_list[0]) #Accessing a collections index
print(fruit_tuple[0:2]) #Accessing a collections range
print(fruit_tuple[-1]) #Accessing using a negative index (count from the end)
print(len(fruit_tuple)) #Find number of element

#DELETING LIST DATA
fruit_list.remove("mango") #Remove a given element
fruit_list.pop(0) #Remove a given index ("mango" has been removed so this removes "apple")
fruit_list.pop() #Remove the final element in the list
del fruit_list[1] #Delete a given index ("banana" in this case)
fruit_list.clear() #Clear a lists data (make list empty but the list still exists)
del fruit_list #Delete a list definition entirely (make variable empty)

#DICTIONARY OPERATIONS
#Declare a new dictionary
computer = {
    "make": "Lenovo",
    "series": "Thinkpad",
    "model": "X1 Extreme Gen2",
    "release_year": 2019,
    "price": 1721
}

computer["condition"] = "used" #Declare a new key-value pair

print(computer["condition"]) #Print value of a given 
print(len(computer)) #Number of items in a dictionary

computer.pop("condition") #Remove a given key-value pair
computer.popitem() #Remove the most last added key-value pair (in this case price, as condition has been removed)
computer.clear() #Empty the dictionary of all key-value pairs
del computer #Delete the dictionary definition entirely (make variable empty)

#Declare nested dictionary using an existing one
the_fountainhead = {
    "title": "The Fountainhead",
    "author": "Ayn Rand",
    "ISBN":  9780847969739
}
books = {
    "book1": the_fountainhead
}

#Access/removal from a nested dictionary
books["book1"]["genre"] = "Philosophical fiction"
books.get("book1").pop("author")
print(books.get("book1").get("genre"))