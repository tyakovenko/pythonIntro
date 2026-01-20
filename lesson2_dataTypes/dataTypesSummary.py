#4 Collection Data Types
#Lists, tuples, sets, and dictionaries
#Coffee Shop Example
#Use a list to keep track of the customers waiting
queue = ["Alice", "Bob", "Charlie", "Alice"] #<- order of items here matters; values can repeat so here we have two different customers names Alice
queue.append("David") # We can add more people

#Use a tuple for a menu item
latte_recipe = ("Espresso", "Steamed Milk", "Foam") #the receipe CAN NOT be changed once it is created

#Use set to keep inventory of everything at the shop
inventory = {"Milk", "Beans", "Sugar", "Beans"} #TODO: what happens if we have duplicates here?

#use a dictionary to combine all of the information
order = {
    "customer": "Alice",
    "drink": "Latte",
    "price": 4.50
}