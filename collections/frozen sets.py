#Create a frozen set named frozen_set containing elements "hello", "world".
frozen_set=frozenset(["hello","world"])
print(frozen_set)
#Try to add "!" to frozen_set. What happens?
      #frozen_set.add("!") #no add command
      #frozen_set.append("!") #no append command

#Create a normal set named normal_set containing elements "let's", "learn".
normal_set=(["let`s","learn"])

#Try to add frozen_set to normal_set. Why does it work? Explain.
#a={normal_set,frozen_set}
#both have to be frozen set

#Print normal_set.
print(normal_set)
#Run your script half a dozen times.


# What do you notice about where frozen_set is added to normal_set?

# Hint: Look at the order of the items.


#What makes a frozen set different to a normal set? Explain.
#frozen immutable/set mutable.This means that we can add or remove elements from a set
#but not from a frozenset

