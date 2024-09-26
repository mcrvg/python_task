#Make a dictionary called "student_1" containing the following information:
list1=["variables", "data_types", "set up"]
student_1={"name": "susan","stream": "tech","completed_lessons": 4,"completed_lesson_names":list1}


#Explain how a dictionary saves/structures data? Example
# #What does each value need to be accompanied/associated with?
#A diccionary is sn unordered collection of items, each value have a key value-pair.

#Print the dictionary to the screen
print(student_1)

#Print it's data type to the screen to check it's a dictionary
print(type(student_1))

#Print the value for the key-value pair having the key "stream"
print(student_1.get("stream"))

#Print the value for 'completed_lesson_names' - check you can see the list of 3 items
print(student_1.get("completed_lesson_names"))

#Print the data type for the value for 'completed_lesson_names' - check it is a list
print(type(student_1.get("completed_lesson_names")))

#Print the first element/item in the list of 'completed_lesson_names' (should output "variables")
print(list1[0])

#Change the value of "completed_lessons" to 3 (an integer not string).
#Make sure you change was successful by printing your dictionary to the screen again.


#Delete "data_types" from the list under the key 'completed_lesson_names'

#Use the keys() method on your dictionary to list all the keys
