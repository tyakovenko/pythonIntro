# lists, tuples, sets, and dictionaries
fruit = ["apple", "banana", "cherry", "apple", "cherry"] # lists allow duplicates
#lists can have mixed data types
print(fruit)
print(fruit[0])
fruit[0] = "new fruit"
print(fruit)

#tuples: storage containers for multiple values in one variable -> unchangable; ordered; allow duplicates
tuple = ("apple", 1)
print(type(tuple)) #access items  by indeces


#sets: static items but you can add or remove them
#unordered; unchangable, do not allow duplicates\
#frozenset is a special type of set that is completely unchangable; you can not add or remove items once it is created
#easy to check if some item is in the set
fruitSet = {"apple", "banana", "cherry", "apple"}
print(fruitSet)
#add items to a set
fruitSet.add("new fruit")
print("banana" in fruitSet)


#example: iterate through the list and find all the duplicates; print them out
def find_duplicates_list(input_list):
    return list(set([x for x in input_list if input_list.count(x) > 1]))

def find_duplicates_set(input_list):
    seen = set()
    duplicates = set()

    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


#dictionaries - ordered 3.7 and up; changable; no duplicate keys; allow any data type for values
dict = {
  "key": "value",
  "fruit": "apple",
  "year": 1964 #TODO: what happens if we have the same key twice?
}
print(dict["key"])
