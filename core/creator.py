import os
import yaml
import typer
from tqdm import tqdm

app = typer.Typer()

def create_project(config_file: str, output_dir: str = "", verbose: bool = False, show: bool = False, force: bool = False):
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

    def create_structure(base_path, structure):
        for key, value in tqdm(structure.items(), desc="Creating structure", disable=not verbose):
            path = os.path.join(base_path, key)
            if verbose:
                typer.echo(f"Processing: {path}")
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
                        if verbose:
                            typer.echo(f"Creating file: {item_path}")
                        with open(item_path, 'w') as f:
                            f.write('')
            else:
                if verbose:
                    typer.echo(f"Creating file: {path}")
                with open(path, 'w') as f:
                    f.write(value)

    if show:
        typer.echo("Performing a dry run...")
        create_structure(project_name, structure)
    else:
        create_structure(project_name, structure)
        typer.echo(f"Project '{project_name}' created successfully.")

@app.command()
def create(config_file: str, output_dir: str = typer.Option("", "--output", "-o", help="Output directory"),
           verbose: bool = typer.Option(False, "--verbose", "-v", help="Verbose mode"),
           show: bool = typer.Option(False, "--show", "-s", help="Perform a dry run"),
           force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing project")):
    create_project(config_file, output_dir, verbose, show, force)

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
def version():
    typer.echo("smithIt version 0.1")

if __name__ == "__main__":
    app()