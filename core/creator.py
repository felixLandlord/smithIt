import os
import yaml
import typer
from tqdm import tqdm

app = typer.Typer()


# def create_project(config_file: str, output_dir: str = "", verbose: bool = False, force: bool = False):
#     if not config_file:
#         config_file = 'smith.yaml'
#         if not os.path.exists(config_file):
#             typer.echo(f"Config file '{config_file}' not found.")
#             config_file = typer.prompt("Please enter the path to the config file")
#             if not os.path.exists(config_file):
#                 typer.echo(f"Config file '{config_file}' not found. Exiting.")
#                 raise typer.Exit(code=1)

#     with open(config_file, 'r') as file:
#         config = yaml.safe_load(file)

#     project_name = config.get('project_name', 'MyProject')
#     structure = config.get('structure', {})

#     if output_dir:
#         project_name = os.path.join(output_dir, project_name)

#     if not os.path.exists(project_name) or force:
#         if os.path.exists(project_name) and force:
#             typer.echo(f"Removing existing project directory: {project_name}")
#             import shutil
#             shutil.rmtree(project_name)

#         os.makedirs(project_name)

#     def create_structure(base_path, structure, verbose=False, force=False):
#         for key, value in tqdm(structure.items(), desc="Creating structure", disable=not verbose):
#             path = os.path.join(base_path, key)
#             if verbose:
#                 typer.echo(f"Processing: {path}")

#             if isinstance(value, dict):
#                 if not os.path.exists(path) or force:
#                     os.makedirs(path, exist_ok=True)
#                     create_structure(path, value, verbose, force)
#                 else:
#                     typer.echo(f"Directory already exists: {path}")
#                     # Check for files and subdirectories within this directory
#                     create_structure(path, value, verbose, force)
#             elif isinstance(value, list):
#                 if not os.path.exists(path) or force:
#                     os.makedirs(path, exist_ok=True)
#                     for item in value:
#                         if isinstance(item, dict):
#                             create_structure(path, item, verbose, force)
#                         else:
#                             item_path = os.path.join(path, item)
#                             if not os.path.exists(item_path) or force:
#                                 if verbose:
#                                     typer.echo(f"Creating file: {item_path}")
#                                 with open(item_path, 'w') as f:
#                                     f.write('')
#                             else:
#                                 typer.echo(f"File already exists: {item_path}")
#                 else:
#                     typer.echo(f"Directory already exists: {path}")
#                     # Check for files and subdirectories within this directory
#                     for item in value:
#                         if isinstance(item, dict):
#                             create_structure(path, item, verbose, force)
#                         else:
#                             item_path = os.path.join(path, item)
#                             if not os.path.exists(item_path) or force:
#                                 if verbose:
#                                     typer.echo(f"Creating file: {item_path}")
#                                 with open(item_path, 'w') as f:
#                                     f.write('')
#                             else:
#                                 typer.echo(f"File already exists: {item_path}")
#             else:
#                 if not os.path.exists(path) or force:
#                     if verbose:
#                         typer.echo(f"Creating file: {path}")
#                     with open(path, 'w') as f:
#                         f.write(value)
#                 else:
#                     typer.echo(f"File already exists: {path}")

#     create_structure(project_name, structure)
#     typer.echo(f"Project '{project_name}' created successfully.")
def create_structure(base_path, structure, verbose=False, force=False):
    for key, value in tqdm(structure.items(), desc="Creating structure", disable=not verbose):
        path = os.path.join(base_path, key)
        if verbose:
            typer.echo(f"Processing: {path}")

        if isinstance(value, dict):
            if not os.path.exists(path) or force:
                os.makedirs(path, exist_ok=True)
                create_structure(path, value, verbose, force)
            else:
                typer.echo(f"Directory already exists: {path}")
                # Check for files and subdirectories within this directory
                create_structure(path, value, verbose, force)
        elif isinstance(value, list):
            if not os.path.exists(path) or force:
                os.makedirs(path, exist_ok=True)
                for item in value:
                    if isinstance(item, dict):
                        create_structure(path, item, verbose, force)
                    else:
                        item_path = os.path.join(path, item)
                        if not os.path.exists(item_path) or force:
                            if verbose:
                                typer.echo(f"Creating file: {item_path}")
                            with open(item_path, 'w') as f:
                                f.write('')
                        else:
                            typer.echo(f"File already exists: {item_path}")
            else:
                typer.echo(f"Directory already exists: {path}")
                # Check for files and subdirectories within this directory
                for item in value:
                    if isinstance(item, dict):
                        create_structure(path, item, verbose, force)
                    else:
                        item_path = os.path.join(path, item)
                        if not os.path.exists(item_path) or force:
                            if verbose:
                                typer.echo(f"Creating file: {item_path}")
                            with open(item_path, 'w') as f:
                                f.write('')
                        else:
                            typer.echo(f"File already exists: {item_path}")
        else:
            if not os.path.exists(path) or force:
                if verbose:
                    typer.echo(f"Creating file: {path}")
                with open(path, 'w') as f:
                    f.write(value)
            else:
                typer.echo(f"File already exists: {path}")

# Modify the create_project function to call the updated create_structure function
def create_project(config_file: str, output_dir: str = "", verbose: bool = False, force: bool = False):
    if not config_file:
        config_file = 'smith.yaml'
        if not os.path.exists(config_file):
            typer.echo(f"Config file '{config_file}' not found.")
            config_file = typer.prompt("Please enter the path to the config file")
            if not os.path.exists(config_file):
                typer.echo(f"Config file '{config_file}' not found. Exiting.")
                raise typer.Exit(code=1)

    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    project_name = config.get('project_name', 'MyProject')
    structure = config.get('structure', {})

    if output_dir:
        project_name = os.path.join(output_dir, project_name)

    if not os.path.exists(project_name) or force:
        if os.path.exists(project_name) and force:
            typer.echo(f"Removing existing project directory: {project_name}")
            import shutil
            shutil.rmtree(project_name)

        os.makedirs(project_name)

    create_structure(project_name, structure, verbose, force)
    typer.echo(f"Project '{project_name}' created successfully.")


def sync_structure(base_path, structure):
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path):
            structure[item] = {}
            sync_structure(item_path, structure[item])
        else:
            structure[item] = None


@app.command()
def create(config_file: str = typer.Argument(None, help="Config file"),
           output_dir: str = typer.Option("", "--output", "-o", help="Output directory"),
           verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose mode"),
           force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing project")):
    create_project(config_file, output_dir, verbose, force)


@app.command()
def delete(paths: list[str]):
    for path in paths:
        if os.path.exists(path):
            if os.path.isdir(path):
                import shutil
                shutil.rmtree(path)
                typer.echo(f"Deleted directory: {path}")
            else:
                os.remove(path)
                typer.echo(f"Deleted file: {path}")
        else:
            typer.echo(f"Path does not exist: {path}")


@app.command()
def rename(src: str, dest: str):
    if os.path.exists(src):
        os.rename(src, dest)
        typer.echo(f"Renamed {src} to {dest}")
    else:
        typer.echo(f"Source path does not exist: {src}")


@app.command()
def move(paths: list[str], dest: str):
    for path in paths:
        if os.path.exists(path):
            dest_path = os.path.join(dest, os.path.basename(path))
            os.rename(path, dest_path)
            typer.echo(f"Moved {path} to {dest_path}")
        else:
            typer.echo(f"Path does not exist: {path}")


@app.command()
def add(paths: list[str]):
    for path in paths:
        if not os.path.exists(path):
            if path.endswith(os.sep) or not os.path.splitext(path)[1]:
                # Create a directory
                os.makedirs(path, exist_ok=True)
                typer.echo(f"Created directory: {path}")
            else:
                # Create a file
                with open(path, 'w') as f:
                    f.write('')
                typer.echo(f"Created file: {path}")
        else:
            typer.echo(f"Path already exists: {path}")


@app.command()
def sync(config_file: str = typer.Option("", "--config", "-c", help="Config file"),
         output_dir: str = typer.Option("", "--output", "-o", help="Output directory"),
         verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose mode")):
    if not config_file:
        config_file = 'smith.yaml'

    project_name = os.path.basename(output_dir) if output_dir else os.getcwd()
    structure = {}

    sync_structure(project_name, structure)

    config = {
        'project_name': project_name,
        'structure': structure
    }

    with open(config_file, 'w') as file:
        yaml.dump(config, file)

    typer.echo(f"Synced structure to {config_file}")


@app.command()
def version():
    typer.echo("smithIt version 0.1")


if __name__ == "__main__":
    app()