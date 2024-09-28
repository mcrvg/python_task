#Make a function with no argument
def print_something():
    print("Hello world!!")
print_something()

#One argument
def print_something2(hello):
    print(hello)

print_something2("Hello wordl!")

# one argument improve
def greet(name :str):
    print("Hello my name is "+ name +".")
greet("Susan")

# Two arguments
def addition(int1=2, int2=2):  #define arguments
  return int1 + int2
print(addition())

#No arguments:addition() missing 2 required positional arguments: 'int1' and 'int2'
#print print(addition(4,4))
# a: int= 4
# b: int= 4
print(addition(4,4)) #new values

# any number of arguments
def print_every_number(*argg):
    print(argg)
argg=(1,2,2,3,3,4,5,5)
print(type(argg))

for i in argg:
    print(i)

#number 7
#def greet(name):
    #print("Hello my name is "+ name +".")
# greet(24601) #TypeError: can only concatenate str (not "int") to str

def division(num1 : int = 2,num2 : int = 5)->float:
    return num1/num2
print(division())

def division(a : int ,b : int)->float:
    return a/b

print(division(4,6))