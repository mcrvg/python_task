# Group task: Functions
1. Make a function with no argument
Name it 'print_something' and all it should do it print something to the screen
Call the function to test it works
``` python 
def print_something(): 
    print("Hello world!!")
print_something()
```

2. Make a function with one argument
Aim: Improve the last function by having it receive an argument to replace the 'hard coded' string
Make a new improved function which
Accepts a string variable as an argument
Prints the string variable received as an argument
````pyhton
def print_something2(hello):
    print(hello)

print_something2("Hello wordl!")
````
3. Make a more interesting version of a function that accepts one argument
call the function: greet("Susan")
use concatentation (ie. +) rather than an f-string.Output should be: Hello, my name is Susan.

```pyhton
def greet(name):
    print("Hello my name is "+ name +".")
greet("Susan")
```
4. Make a function with 2 arguments that returns a value of 4:
````python

def addition(int1=2, int2=2):  #define arguments
  return int1 + int2
print(addition())

print(addition(2, 2))
print(addition(4,4)) #new values
````

5. Make a function with default values
Copy your working code from the last exercise (that adds 2 and 2 together) as starting code for this exercise
Replace line of code to call the function with this:
print(addition())
Run your code - you should get an error
Modify your function so that int1 and int2 both have the default value of 2
Run your code and make sure the result is 4
Now call your function with this line of code:
print(addition(4, 4))
Explain why the answer is now 8

6. Make a function that accepts any number of arguments
def print_every_number(my_tuple):
    print(my_tuple)
my_tuple=(1,2,2,3,3,4,5,5)
print(my_tuple)
for i in my_tuple:
    print (i)

a)Print the type of the tuple that was passed in as an arguments
b)Loop through the tuple and print each item in the tuple on a separate line
After calling the function, the output should be:

Explain what character allows your function to accept multiple arguments
````python
def print_every_number(*argg):
    print(argg)
argg=(1,2,2,3,3,4,5,5)
print(type(argg))

for i in argg:
    print(i)

````

7. Make a function which gives a hint about an argument's data type

1-See what happens if you call :greeting(24601)
greeting(24601)
````pyhton
def greet(name):
    print("Hello my name is "+ name +".")
greet(24601) #TypeError: can only concatenate str (not "int") to str
````
8. The function should be named division:
have their types defined
have the default values of 2 and 5 
NEW! Define the value returned as a float for the type hint


Before calling the function, define variables a and b in Python as strongly-typed integers with the values 4 and 6
You should call the function with this line of code:
print(division(a, b))
Also check the default values work if no values are passed into the function
9. What are some good practices when it comes to functions?


# Recommended: Make a 'functions' folder inside your PyCharm project for storing learning about functions.
MVP (each of these should be in a separate function):
Can add 2 numbers 
Can subtract 2 numbers 
Can multiply 2 numbers 
Can divide 2 numbers 
Taking it to the next level:
Implement more complex operations, such as handling parentheses, exponentiation 
More advanced operations should continue to be broken into separate functions 
1. create math operations where we define all functions
2. Import to our calculator.py

#  Re-factor your calculator to use a math_operations module
Modify your calculator script so that all arithmetic functions are moved to the python file math_operations.py
In your main calculator script, import math_operations so that the functions are accessed in math_operations.py
In your main calculator script, modify the calling of the functions so they use the math_operations module.

# What JSON does it stand for?
1. What is it used for?
JSON (JavaScript Object Notation) is a lightweight, text-based format for storing and transporting data.
It is widely used in various applications due to its human-readable and easy-to-parse nature.
example:data storage, NoSQL databases, or configuration files
2. What is it written in?
JSON uses key-value pairs to represent data. The keys are strings (enclosed in double quotes),
and the values can be various data types, including strings, numbers, booleans, arrays, objects, and null.
3. Include a simple example of JSON:
````
JSON
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
````
4. Advantages of using it? 

- Human-Readable: JSON is designed to be easily read and understood by humans. Its syntax is simple and straightforward, making it easy to inspect and modify data manually.
- Lightweight: JSON is a relatively lightweight format compared to XML. It uses less space to represent the same data, making it more efficient for data transmission over networks.
- Language-Independent: JSON is not tied to any specific programming language. It can be used with various programming languages, making it a versatile format for data exchange.
- Easy to Parse: Many programming languages have built-in support for parsing JSON, making it easy to work with in different programming environments.
- Hierarchical Structure: JSON uses a hierarchical structure with key-value pairs, making it easy to represent complex data structures.
- Widely Supported: JSON is widely supported by various software applications and services, making it a common standard for data exchange.
- Flexible: JSON can represent a wide range of data types, including numbers, strings, booleans, arrays, objects, and null values.
- Efficient: JSON is relatively efficient to parse and generate, making it suitable for high-performance applications.
- Platform-Independent: JSON can be used on different platforms and operating systems without any compatibility issues.
- Easy to Learn: The syntax of JSON is relatively simple to learn, even for those who are not experienced programmers.

5. What data types can it store/use?
- Strings: Text enclosed in double quotes (e.g., "Hello, world!").
- Numbers: Integers and floating-point numbers (e.g., 123, 3.14).
- Booleans: true and false.
- Arrays: Ordered collections of values enclosed in square brackets (e.g., [1, 2, 3]).
- Objects: Unordered collections of key-value pairs enclosed in curly braces (e.g., {"name": "John", "age": 30}).
- Null: Represents the absence of a value (e.g., null).   
*Note:
- Nested structures: JSON allows for nested structures, meaning you can have arrays within objects, objects within arrays, and so on.
- Data types within arrays and objects: The values within arrays and objects can be any of the supported data types.
6. What is the JSON syntax for:

a) Name value pairs? 
In JSON, name-value pairs are separated by a colon (:) and enclosed within curly braces {}. 
The name (or key) is always a string enclosed in double quotes, and the value can be any of the supported data types,
(string, number, boolean, array, object, or null).

Example:
````
JSON
{
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
````
 


