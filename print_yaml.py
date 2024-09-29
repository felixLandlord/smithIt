import yaml
from pprint import pprint

# Define the path to the YAML file
yaml_file = 'smith0.yaml'

# Open and read the YAML file
with open(yaml_file, 'r') as file:
    # Load the contents of the YAML file
    yaml_content = yaml.safe_load(file)

# Print the contents of the YAML file
# print(yaml.dump(yaml_content, default_flow_style=False))
pprint(yaml_content, sort_dicts=False)