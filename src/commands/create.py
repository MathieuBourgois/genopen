import os
import shutil
from pathlib import Path
import click

@click.command("create")
@click.argument("project_name")
def create_command(project_name):
    """
    Creates a new project in a folder named PROJECT_NAME.
    Copies files and directories from the `template` directory.
    """
    current_dir = Path.cwd()
    project_dir = current_dir / project_name
    templates_dir = Path(__file__).parent.parent.parent / "template"

    if project_dir.exists():
        click.echo(f"Error: The folder '{project_name}' already exists.")
        return

    try:
        project_dir.mkdir()
        click.echo(f"Created folder: {project_dir}")

        shutil.copytree(templates_dir, project_dir, dirs_exist_ok=True)
        click.echo(f"Copied files from {templates_dir} to {project_dir}")

    except Exception as e:
        click.echo(f"Error while creating the project: {e}")
