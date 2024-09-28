import yaml
import sys
def validate_yaml_file(filename):
  """
  This function attempts to load a YAML file and returns True if the syntax is valid, False otherwise.

  Args:
      filename (str): The name of the YAML file to validate.

  Returns:
      bool: True if the YAML syntax is valid, False otherwise.
  """
  try:
    with open(filename, 'r') as f:
      yaml.safe_load(f)
    return True
  except yaml.YAMLError as exc:
    print(f"Error: YAML syntax error in '{filename}': {exc}")
    return False

if __name__ == "__main__":
  # Get the filename from the command line argument (optional)
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    print("Usage: validate_yaml_file.py <filename.yaml>")
    exit(1)

  # Validate the YAML file
  if validate_yaml_file(filename):
    print(f"YAML file '{filename}' is valid.")
  else:
    print(f"YAML file '{filename}' is invalid.")