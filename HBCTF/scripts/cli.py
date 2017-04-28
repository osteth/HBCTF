import click
import HBCTF 

@click.group()
@click.option('-p', '--port', default=8000, help='Port numer to serve the API on.')
@click.option('-v', '--verbose', default=1, help='Sets the verbosity of outputs')
@click.option('-l', '--logging', default=1, help='Sets the detail level of logs')
def cli():
    """This is the Hacker Bootcamp CTF game control center. 
	This application controlls all aspects of the game. Additional information is avilable at https://github.com/osteth/HBCTF/"""
    pass

@click.command(help='Initialize the database.')
def initdb():
    click.echo('Initializing the database.')

@click.command(help='Drop the database.')
def dropdb():
    click.echo('Dropping the database.')
	
@click.command(help='Start the API.')
def start(port, verbose, logging):
	click.echo('Serving on http://127.0.0.1:%d/' % port)
	
@click.command(help='Stop the API.')
def stop():
	click.echo('Stopping the API.')
	
@click.command(help='Restart the API.')
def restart():
	click.echo('Restarting the API.')

@click.command(help='Show the status of the API.')
def status():
	click.echo('This status goes here.')


cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(start)
cli.add_command(stop)
cli.add_command(restart)
cli.add_command(status)