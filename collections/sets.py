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

""" Creating frozen sets:

Frozen sets are created using the frozenset() constructor, which takes an iterable (like a list, tuple, or another set) as input:

Python
my_frozen_set = frozenset([1, 2, 3, 4])
print(my_frozen_set)  # Output: frozenset({1, 2, 3, 4})
Usa el código con precaución.

Operations on frozen sets:

Frozen sets support various set operations, including:

Union: Combines elements from two sets, removing duplicates.
Python
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 4, 5])
union_set = set1 | set2
print(union_set)  # Output: frozenset({1, 2, 3, 4, 5})
Usa el código con precaución.

Intersection: Returns elements that are present in both sets.
Python
intersection_set = set1 & set2
print(intersection_set)  # Output: frozenset({3})
Usa el código con precaución.

Difference: Returns elements that are present in the first set but not in the second.
Python
difference_set = set1 - set2
print(difference_set)  # Output: frozenset({1, 2})
Usa el código con precaución.

Symmetric difference: Returns elements that are present in either set but not in both.
Python
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: frozenset({1, 2, 4, 5})

"""