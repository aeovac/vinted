import click

@click.command()
@click.argument('name')
@click.option('--config', '-g')
def main(name, greeting):
    click.echo("{}, {}".format(greeting, name))