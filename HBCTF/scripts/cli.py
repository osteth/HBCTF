import click
import HBCTF
import HBCTF.scripts.api as api
import couchdb, json, sys
import subprocess   


@click.group()
def cli():
    """This is the Hacker Bootcamp CTF game control center. 
	This application controlls all aspects of the game. Additional information is avilable at https://github.com/osteth/HBCTF/"""
    pass

@click.command(help='Check the Status of the Database')
def dbstatus():
    subprocess.run(['/bin/bash', '-O', 'extglob', '-c', 'service couchdb status'])
    return()

@click.command(help='Turn the Database ON.')
def dbon():
    subprocess.run(['/bin/bash', '-O', 'extglob', '-c', 'service couchdb start'])
    return()

@click.command(help='Turn the Database OFF')
def dboff():
    subprocess.run(['/bin/bash', '-O', 'extglob', '-c', 'service couchdb stop'])
    return()


@click.command(help='Initialize the database.')
@click.option('-s', '--ssl', default=False, help='sets ssl true or false.')
@click.option('-u', '--username', default='', help='Sets the username that you will connect to the database with.')
@click.option('-k', '--password', default='', help='pass in teh password that should be used to login to the database.')
@click.option('-h', '--host', default='localhost', help='sets the address for the database.')
@click.option('-p', '--port', default=5984, help='Sets the port the database should run on.')
def initdb(ssl, username, password, host, port):
    '''This command will take in database connection info, retrieve and save it to/from the DBdata.json file. Login credentials and information must be in the DBdata.json file because this is the way that the connection info is passed between scripts.'''
    click.echo('Initializing the database.')
    
    try:
        with open('DBdata.json', 'r') as f:
            click.echo('Credentials file found.')
            login_data = f.read()
            f.close()
            data = json.load(login_data)
            ssl = data.get(ssl)
            username = data.get(username)
            password = data.get(password)
            host = data.get(host)
            port = data.get(port)
            return()
        
    except:
        data = {'ssl': ssl, 'username': username, 'password': password, 'host': host, 'port': port}        
        with open('DBdata.json', 'w') as file:
            json.dump(data, file)
        file.close()
        click.echo('Setttings Saved.')
        
    else:
        click.echo('Error: Cannont find DBdata.json file and cannot create new file.')
    
    api.initdb()   

@click.command(help='Drop the database.')
def dropdb():
    click.echo('Dropping the database.')
	
@click.command(help='Start the API.')
@click.option('-p', '--port', default=8000, help='Port numer to serve the API on.')
@click.option('-d', '--debug', default=False, help='turns debuggin on/off')
def start(port, debug):
	click.echo('Starting the API')
	api.start(port, debug)
	
@click.command(help='Stop the API.')
def stop():
	click.echo('Stopping the API.')
	
@click.command(help='Restart the API.')
def restart():
	click.echo('Restarting the API.')

@click.command(help='Show the status of the API.')
def status():
	click.echo('This status goes here.')

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        click.echo(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            click.echo("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
            
@click.command(help='test module for testing new functions.')
def test():
    print(api.dbconnect())
    return()

cli.add_command(test)
cli.add_command(dbstatus)
cli.add_command(dbon)
cli.add_command(dboff)
cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(start)
cli.add_command(stop)
cli.add_command(restart)
cli.add_command(status)
