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
    print("Usage: json2yaml.py <source_file.json_yaml> <target_file.yaml>")
    exit(1)

# 1. Convert the JSON to YAML - use yaml library
convert_yaml = yaml.dump(source_content, default_flow_style=False)

# 2. Save the YAML into a new file with the name for it received as an argument
# 2.1 Check the target file name was specified as an argument
if len(sys.argv) > 2:
    target_file = sys.argv[2]

    # 2.2 Check the target file doesn't already exist
    if os.path.exists(target_file):
        print(f"ERROR: Target file '{target_file}' already exists.")
        exit(1)

    # 2.3 If previous conditions not met, then save YAML file
    with open(target_file, 'w') as yaml_file:
        yaml_file.write(convert_yaml)
        print(f"YAML content successfully written to '{target_file}'")
else:
    # If no target file is provided, print the YAML content to the screen
    print("No target file specified. Outputting YAML to the screen:")
    print(convert_yaml)

"""
import json
import os
import sys
import yaml
#create a JSON file :json.json with pycharm.
#Check if there is a file json.json


    # Check if the target file (json.json) exists
if os.path.exists("json.json"):
    print("The file 'json.json' already exists.")

    # Failing if the file isn't found
else:
    print("ERROR: File json.json not found")


 # 1. Convert the JSON to YAML - use yaml library
# WRITE YOUR CODE HERE
# open JSON
#####T
# 1. Convert the file json.json to YAML file name convert.yaml
with open('json.json', 'r') as json_file:
    data = json.load(json_file)

with open('convert.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

# 2. Save the YAML into a new file with the name for it received as a argument
target_file = None
if len(sys.argv) > 2:
    target_file = sys.argv[2]

# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# 2.2 Check the target file doesn't already exist
if target_file:
    with open(target_file, 'w') as yaml_file:
        yaml.dump(data, yaml_file)
elif os.path.exists("target_file"):
        print(f"ERROR: Target file '{target_file}' already exists.")
        exit(1)
else:
    print(yaml.dump(data))

"""
