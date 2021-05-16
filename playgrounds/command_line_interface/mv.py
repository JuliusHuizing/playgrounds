import click

"""
For a good explanation of programmes, arguments, options:
https://docs.python.org/dev/library/optparse.html#background

For a quick guide on Click:
https://zetcode.com/python/click/

"""


"""
Remaking the standard Lunix 'mv' programme using the Click package for python.

Usage (after 'poetry shell && poetry install')
-----
    example1: python mv.py --help

"""
@click.command()
@click.option('-v', is_flag=True, help='Cause mv to be verbose, showing files after they are moved.')
@click.argument('source', nargs=-1)
@click.argument('destination')
def mv(v, source, destination):
    if v:
        for item in source:
            print(item)
    print(f'moved {source} to {destination}.')


if __name__ == "__main__":
    mv()


