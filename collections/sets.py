#USING SETS
#Explain 2 main ways that sets are different to lists and tuples
#Lists and tuples are standard Python data types that store values in a sequence.
# Sets are another standard Python data type that also store values.
# The major difference is that sets, unlike lists or tuples, cannot have
# multiple occurrences of the same element and store unordered values.
#NO INDEX

#Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits=set(["apple","banana","cherry"])

#Print the set 'fruits'
print(fruits)

#Add "orange" to the fruits set using one of the set's methods.
fruits.add("orange")

#Print the set 'fruits' - check it's added
print(fruits)

#Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana") #also use discard

#Print the set 'fruits' - check it's removed
print(fruits)
#Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple")

#Print the final fruits set.
print(fruits) #Don´t add apple.sets do not accept duplicates

#Print the 2nd item in the set. If there is any problem doing this, explain.
#sets do not have index
#loop the values
#unordered

for a in fruits:
    if a=="cherry":
       print(a)
