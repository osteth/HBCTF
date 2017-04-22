# Skeleton of a CLI

import click

import HBCTF


@click.command('HBCTF')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(HBCTF.has_legs)
