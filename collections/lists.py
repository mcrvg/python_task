from ctypes.wintypes import SHORT

#Create a list called 'shopping_list' with the following items:
shopping_list=["eggs","bread","bananas","biscuits","milk"]

#Print the list to the screen
print(shopping_list)

#Print the data type of 'shopping_list'
print(type(shopping_list))

#Print the first item in the list
print(shopping_list[0])
#Print the last item in the list
print(shopping_list[4]) #index for item5
print(shopping_list[-1])
#Change the second item in the list (i.e. 'bread') to 'rice'
shopping_list[1]="rice"
print(shopping_list)
#Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list at same time
shopping_list.extend(["toffee","coffee"])
print(shopping_list)
#Remove "bananas" from 'shopping_list'
shopping_list.remove("bananas")
print(shopping_list)
#Remove the last item ('coffee') from 'shopping_list' using the pop method.
shopping_list.pop()
print(shopping_list)