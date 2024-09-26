list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

#write a for loop to print the double of each number in the list 'list_data'.
for num in list_data:
    print(num+num)

#Write another for loop to print the items inside of 'embedded_lists'.
#Each item in the list should be called 'data'

for data in embedded_lists:
    print(data)

#We need to access the data within the lists, so now we need an embedded loop.
#Create another loop inside of the embedded_lists for loop to list the individual items in the lists.
print(embedded_lists[0]) #[1,2,3]
for data in embedded_lists[0]:   #1,2,3,vertically
    print(data)

print(embedded_lists[1]) #[4,5,6]
for data in embedded_lists[1]:   #4,5,6,vertically
    print(data)

#For loop keys dictionary dict_data
for key in dict_data:
    print(key)

#Write another for loop to loop through the dictionary 'dict_data'. Use to the dictionary's
# value() method to print the value for each key in the dictionary.
for v in dict_data.values():
    print(v)

#Loop to print the values of the dict.
for item in dict_data.values():
    for value in item.values():
        print(value)

#Write another for loop to loop through the dictionary 'dict_data' but this time only print out
# the money values.
for item in dict_data.values():
    print(item["money"])

#Write another loop to loop through the items in 'list_data' and include a nested (indented)
# if statement inside the loop so that when it loops it checks the number/item in list:
#if the number is less than 3, it prints 'less than 3'
#if the number equals 3, it prints 'I found three'
#if the number is greater than 3, it prints 'greater than 3'

for number in list_data:
    if number<3:
        print('less than 3')
    elif number==3:
        print('I found three')
    else:
        print('greater than 3')

