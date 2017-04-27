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

    git clone https://github.com/mapbox/HBCTF myproject
    cd HBCTF

Then install in locally editable (``-e``) mode and run the tests.

.. code-block:: console

    sudo pip install -e .[test]
    py.test
Then run the game API.
.. code-block:: console

    python3 HBCTF/scripts/api.py

Finally, give the command line game control program a try.

.. code-block:: console

    HBCTF --help
    myproject 4




Services API explaination 
--------

Checkin --> Token Decryption --> ScoreTokentSubmit

Checkin 
------
Player checks into the game server and submits to the server the ip address and port their service is running on.  The server responds out to the player with key and an encrypted score token that the player can decrypt and submit to recieve points. 

* Player Actions
   * Checkin with IP and port they are running their service on.
   * Accept tokens and dectypts them
   * Submit decrypted tokens back to the server decrypted. 
* Server Actions
   * Recieve checkin information and store it in DB. 
   * Pass out tokens every 5 minuts.
   * Recieve decrypted tokens and register scores.

ScoreTokentSubmit
--------
Player submits the decrypted token back to the server to gain their points. 
* CLI options
   * Start, Starts the api server 
      * -flags
      * -p  Specify a port for the service to run on. 
   * Stop, Stops the API server
   * Status, displays the server

Dev Roadmap
-----
* Services API -> unit tests -> documentation.
* Game Control CLI -> unit tests -> documentation.
* Expad API for jeopardy stype flags -> unit tests -> documentation.
* Jeopardy style scoreboard -> unit tests -> recustomization pipeline-> documentation.
* Expand API for battleground features -> unit tests -> documentation.
* Build battleground VM's -> Network VM's -> Seutup High Value Nodes and hook them to API -> Recustomization Pipeline -> documentation.

Dev Notes:
------
To help prevent uncustomized forks of HBCTF from being uploaded to PyPI,
I've configured the setup's upload command to dry run. Make sure to remove
this configuration from
`setup.cfg <https://docs.python.org/2/install/index.html#inst-config-syntax>`__
when you customize HBCTF.

* logging 
* isatty
* colrama
* progressbar (progressbar2)
 
