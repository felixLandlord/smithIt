import os
import yaml
import sys

def create_project(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    project_name = config.get('project_name', 'MyProject')
    structure = config.get('structure', {})

    if not os.path.exists(project_name):
        os.makedirs(project_name)

    def create_structure(base_path, structure):
        for key, value in structure.items():
            path = os.path.join(base_path, key)
            print(f"Processing: {path}")  # Debug print
            if isinstance(value, dict):
                os.makedirs(path, exist_ok=True)
                create_structure(path, value)
            elif isinstance(value, list):
                os.makedirs(path, exist_ok=True)
                for item in value:
                    if isinstance(item, dict):
                        create_structure(path, item)
                    else:
                        item_path = os.path.join(path, item)
                        print(f"Creating file: {item_path}")  # Debug print
                        with open(item_path, 'w') as f:
                            f.write('')
            else:
                print(f"Creating file: {path}")  # Debug print
                with open(path, 'w') as f:
                    f.write(value)

    create_structure(project_name, structure)
    print(f"Project '{project_name}' created successfully.")

def main():
    if len(sys.argv) != 2:
        print("Usage: create_project <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    create_project(config_file)

if __name__ == "__main__":
    main()