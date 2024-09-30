# parsing/converting YAML to a dictionary
# As example to understand the code and the steps:
# convert.yaml to a new file convert_dict.py

import yaml
# convert.yaml to a dictionary
with open('convert.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)
print(data)

# Save dictionary in a new file convert_dict.py

with open('convert_dict.py', 'w') as python_file:
    convert_dict = data
#This open a new file convert_dict, but is empty



# Print the dictionary in the new file
print(config_data)

#Create version of validate_yaml_file.py: see another file:
#GitHub\python_tasks\json_yaml>validate_yaml_file

#Create a YAML to JSON file conversion script
#From covert.yaml file create a new file convert.json
import json
import yaml

with open('convert.yaml', 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

with open('convert.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


#Create a script that check if an entire folders contents is valid YAML (will need loops to check each file)
import os
import yaml

def validate_yaml_files(directory):
    """
    Validates all YAML files within a given directory.

    Args:
        directory (str): The path to the directory to check.

    Returns:
        list: A list of filenames that are invalid YAML files.
    """

    invalid_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.yaml'):
            file_path = os.path.join(directory, filename)
            if not validate_yaml_file(file_path):
                invalid_files.append(filename)
    return invalid_files

def validate_yaml_file(filename):
    """
    Validates a single YAML file.

    Args:
        filename (str): The path to the YAML file.

    Returns:
        bool: True if the YAML file is valid, False otherwise.
    """

    try:
        with open(filename, 'r') as f:
            yaml.safe_load(f)
        return True
    except yaml.YAMLError as exc:
        print(f"Error: YAML syntax error in '{filename}': {exc}")
        return False

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    invalid_files = validate_yaml_files(directory_path)

    if invalid_files:
        print("Invalid YAML files:")
        for filename in invalid_files:
            print(f"  - {filename}")
    else:
        print("All YAML files are valid.")