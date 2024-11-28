import click
from commands.create import create_command
from commands.add import add_command
from commands.build import build_command

@click.group()
def cli():
    """
    Genopen CLI - A blog generator.
    """
    pass

cli.add_command(create_command)
cli.add_command(add_command)
cli.add_command(build_command)

if __name__ == "__main__":
    cli()
