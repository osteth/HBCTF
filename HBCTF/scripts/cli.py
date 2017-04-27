
import click, time
from daemonocle.cli import DaemonCLI
# Doc's availabe at https://github.com/jnrbsn/daemonocle

import HBCTF 

	
@click.command(cls=DaemonCLI, daemon_params={'pidfile': '/var/run/example.pid'})
def main():
    """This is the Hacker Bootcamp CTF game control center. 
	This application controlls all aspects of the game. Additional information is avilable at https://github.com/osteth/HBCTF/"""
    while True:
        time.sleep(10)

if __name__ == '__main__':
    main()
