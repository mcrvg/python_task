#Define a dictionary called story1. It should have the following keys:
story1={
    'start':"once upon a time",
    'middle':"he was fighting ..." ,
    'end':"and that is how he save the wordl"
}
print(story1)

#Print only the keys
print(story1.keys())
#Print only the values
print(story1.values())

#Print the individual values using the keys (individually, lots of print commands)


#Now, let's add a new key:value pair:
#'hero': yourSuperHero
story1.update({'hero': "yourSuperHero"})
print(story1)

#Improve the program. For example, can you make it a "Choose your own adventure" story?
