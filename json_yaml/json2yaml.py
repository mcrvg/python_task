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


