HBCTF
======

.. image:: https://travis-ci.org/osteth/HBCTF.svg?branch=master
   :target: https://travis-ci.org/osteth/HBCTF

.. image:: https://coveralls.io/repos/github/osteth/HBCTF/badge.svg
   :target: https://coveralls.io/github/osteth/HBCTF

A hybrid CTF game, combining a dev-ops service hack and patch, jeopardy style flags, and an explorable battfield were players go head to head to control strategic network nodes.

.. image:: http://www.hackbama.com/wp-content/uploads/2017/03/Hackbama_Logo-enc-400x400.png

.. contents:: **Table of Contents**
  :backlinks: none

Quick start
-------------------------

To use HBCTF as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

.. code-block:: console

    git clone https://github.com/osteth/HBCTF
    cd HBCTF

Then install in locally editable (``-e``) mode and run the tests.

.. code-block:: console

    sudo pip install -e .[test]
    py.test

Then install couchDB (Developtment and testing is done on Ubuntu 16.04)
.. code-block:: console

    sudo apt-get install couchDB

Finally, give the command line game control program a try.

.. code-block:: console

    HBCTF --help




Services API explaination
-------------------------

Checkin --> Token Decryption --> ScoreTokentSubmit


Checkin
------------------------
Player checks into the game server and submits to the server the ip address and port their service is running on.  The server responds out to the player with key and an encrypted score token that the player can decrypt and submit to receive points.

* Player Actions
   * Checkin with IP and port they are running their service on.
   * Accept tokens and decrypts them

   * Submit decrypted tokens back to the server decrypted.
* Server Actions
   * Recieve checkin information and store it in DB.

   * Pass out tokens every 5 minutes.
   * Recieve decrypted tokens and register scores.

ScoreTokentSubmit
-----------------------

Player submits the decrypted token back to the server to gain their points.

CLI Commands
-----------------------
Usage: HBCTF [OPTIONS] COMMAND [ARGS]...

Options:
------------------------
+---------------+---------+---------------------------------+
|Flag           |Type     | Description                     |
+---------------+---------+---------------------------------+
| -p, --port    | INTEGER | Port number to serve the API on.|
| -v, --verbose | INTEGER | Sets the verbosity of outputs   |
| -l, --logging | INTEGER | Sets the detail level of logs   |
| --help        |         | Show this message and exit.     |
+---------------+---------+---------------------------------+

Commands:
-----------------------
+--------+-------------------------------+
|Command | Action                        |
+--------+-------------------------------+
|dropdb  | Drop the database.            |
|initdb  | Initialize the database.      |
|restart | Restart the API.              |
|start   | Start the API.                |
|status  | Show the status of the API.   |
|stop    | Stop the API.                 |
+--------+-------------------------------+

Dev Roadmap
----------------------
* Services API -> unit tests -> documentation.
* Game Control CLI -> unit tests -> documentation.
* Expad API for jeopardy stype flags -> unit tests -> documentation.
* Jeopardy style scoreboard -> unit tests -> recustomization pipeline-> documentation.
* Expand API for battleground features -> unit tests -> documentation.
* Build battleground VM's -> Network VM's -> Seutup High Value Nodes and hook them to API -> Recustomization Pipeline -> documentation.

Dev Notes:
-----------------------
To help prevent uncustomized forks of HBCTF from being uploaded to PyPI,
I've configured the setup's upload command to dry run. Make sure to remove
this configuration from
`setup.cfg <https://docs.python.org/2/install/index.html#inst-config-syntax>`__
when you customize HBCTF.


* logging
* isatty
* colrama
* progressbar (progressbar2)

