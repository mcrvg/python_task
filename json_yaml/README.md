# What does it stand for?
JSON stands for JavaScript Object Notation. 
It's a lightweight data-interchange format that is easy for humans to read and write, 
and easy for machines to parse 1  and generate. It's often used to transmit data between a 2  
web server and a web application, or between a web application and a database.

# What is it used for?
JSON is widely used in various applications and domains due to its simplicity, flexibility
and efficiency.
JSON is widely used in various applications and domains due to its simplicity, flexibility, and efficiency. Here are some of its primary use cases:

example: Store data
NoSQL Databases: Many NoSQL databases, such as MongoDB, CouchDB, and Cassandra, use JSON as their native data format. This allows for flexible and dynamic data structures that can evolve over time.
Configuration Files

# What is it written in?

Include a simple example of JSON
# Advantages of using it?

# What data types can it store/use?


## JSON Syntax:
a) Name-value pairs:
In JSON, name-value pairs are separated by a colon (:) and enclosed within curly braces {}. 
The name (or key) is always a string enclosed in double quotes, and the value can be any of the supported data types 
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
b) Objects:
Objects in JSON are collections of name-value pairs. They are enclosed within curly braces {}.
Example:
````
JSON
{
    "person": {
        "name": "Alice",
        "age": 25
    }
}
````
c) How to separate data (key/value pairs) from one another?
Name-value pairs: Within an object, name-value pairs are separated by commas (,).
Objects and arrays: Objects and arrays can be nested within each other, and they are also separated by commas.
Example:
````
JSON
{
    "person": {
        "name": "Alice",
        "age": 25,
        "hobbies": ["reading", "coding"]
    }
}
 ````

d) JSON arrays: (like list in python)
JSON arrays are ordered collections of values enclosed in square brackets []. 
Each value in an array can be any of the supported data types.
Example:
````
JSON
{
    "fruits": ["apple", "banana", "orange"]
}
````

 # Convert a Python dictionary into a JSON-formatted string and a JSON file
What is encoding vs serialising 
- Encoding is about converting data from one format to another, often for efficiency or compatibility reasons.
- Serializing is about converting data structures into a format that can be stored or transmitted and then reconstructed later.

Work out which one of them are you doing with the subtasks below
Starting code:

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
Subtasks:

- Convert this Python dictionary into a JSON-formatted string
````
json_string = json.dumps(servers_dict)
print(json_string)
````
- Convert this Python dictionary to a JSON file
````
with open("data.json", "w") as f:
    f.write(json_string)

print("JSON data written to data.json")
````

# Convert JSON file to Python dictionary
Create a new file servers.json and add this JSON to it:
{
	"server1": {
		"hostname": "web-server-1",
		"ip_address": "192.168.1.1",
		"role": "web",
		"status": "active"
	},
	"server2": {
		"hostname": "db-server-1",
		"ip_address": "192.168.1.2",
		"role": "database",
		"status": "maintenance"
	}
}

Create a file called parse_json_to_dict.py and add code to it to: 
Steps:

-Use 'with' to open the file created above

````python
import json

with open('servers.json', 'r') as f:
    data = json.load(f)
````
Parse contents the JSON file into a Python dictionary named "servers"
````
with open('servers.json', 'r') as f:
    servers = json.load(f)
````
Print out the type of "servers"
````
print(type(servers))
````
Print out the dictionary record with the key "server1"
 print(servers['server1'])
Print out the dictionary record with the key "server2"
print(servers['server2'])
Print all of the keys and values. Output should be:
````
  for server_name, server_data in servers.items():
    print(f"Server Name: {server_name}")
    for key, value in server_data.items():
      print(f"  {key}: {value}")
 ````
Key and value: 'server1' = '{'hostname': 'web-server-1', 'ip_address': '192.168.1.1', 'role': 'web', 'status': 'active'}'
  Record key and sub value: 'hostname' = 'web-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.1'
  Record key and sub value: 'role' = 'web'
  Record key and sub value: 'status' = 'active'
Key and value: 'server2' = '{'hostname': 'db-server-1', 'ip_address': '192.168.1.2', 'role': 'database', 'status': 'maintenance'}'
  Record key and sub value: 'hostname' = 'db-server-1'
  Record key and sub value: 'ip_address' = '192.168.1.2'
  Record key and sub value: 'role' = 'database'
  Record key and sub value: 'status' = 'maintenance'


# JSON to YAML

# What is yaml
YAML (Yet Another Markup Language) is a human-readable data-serialization language for all programming languages. It aims to be more readable than JSON and XML, often used for configuration files, data structures, and more.
- easy to read
- indenting necessary:to represent a list

In groups of 2-3, create a script that converts Valid JSON to Valid YAML.

Create a new Python file json2yaml.py for this task.

Valid JSON:

{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Python", "DevOps"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}

Valid YAML:

name: John Doe
age: 30
isStudent: false
courses:
  - Python
  - DevOps
address:
  street: 123 Main St
  city: Anytown

Starting code:

import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json2yaml.py <source_file.json> <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
# WRITE YOUR CODE HERE

# 2. Save the YAML into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# WRITE YOUR CODE HERE

# 2.2 Check the target file doesn't already exist
# WRITE YOUR CODE HERE

# 2.3 If previous conditions not met, then save YAML file
# WRITE YOUR CODE HERE
You need to find a way to convert the JSON object to a YAML object and then save that YAML in a new target YAML file (name of YAML file is specified as an argument by the user)

We will talk through it on xxx so be ready to present your solution!

Hints:

The method you need may involve “dumping”
Before you can import yaml, you may need to install the pyyaml module with this command: pip install pyyaml
Get the groups to let you know if they complete the task. At the 60 minute mark bring everyone back and talk through the completed code.

