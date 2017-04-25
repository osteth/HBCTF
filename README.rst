HBCTF
======

.. image:: https://travis-ci.org/osteth/HBCTF.svg?branch=master
   :target: https://travis-ci.org/osteth/HBCTF
   
.. image:: https://coveralls.io/repos/github/osteth/HBCTF/badge.svg
   :target: https://coveralls.io/github/osteth/HBCTF

A skeleton of a Python package with CLI and test suite included.
   
.. image:: http://www.hackbama.com/wp-content/uploads/2017/03/Hackbama_Logo-enc-400x400.png

Customization quick start
-------------------------

To use HBCTF as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

.. code-block:: console

    git clone https://github.com/mapbox/HBCTF myproject
    cd myproject

Replace all occurrences of 'HBCTF' with the name of your own project.
(Note: the commands below require bash, find, and sed and are yet tested only on OS X.)

.. code-block:: console

    if [ -d HBCTF ]; then find . -not -path './.git*' -type f -exec sed -i '' -e 's/HBCTF/myproject/g' {} + ; fi
    mv HBCTF myproject

Then install in locally editable (``-e``) mode and run the tests.

.. code-block:: console

    sudo pip install -e .[test]
    py.test

Finally, give the command line program a try.

.. code-block:: console

    myproject --help
    myproject 4

To help prevent uncustomized forks of HBCTF from being uploaded to PyPI,
I've configured the setup's upload command to dry run. Make sure to remove
this configuration from
`setup.cfg <https://docs.python.org/2/install/index.html#inst-config-syntax>`__
when you customize HBCTF.

Please also note that the Travis-CI and Coveralls badge URLs and links in the README
contain the string 'mapbox.' You'll need to change this to your own user or organization
name and turn on the webhooks for your new project.

A post on the Mapbox blog has more information about this project:
https://www.mapbox.com/blog/HBCTF/.

See also
--------

Here are a few other tools for initializing Python projects.

- Paste Script's `paster create <http://pythonpaste.org/script/#paster-create>`__ is
  one that I've used for a long time.
- `cookiecutter-pypackage <https://github.com/audreyr/cookiecutter-pypackage>`__ is
  a Cookiecutter template for a Python package. Cookiecutter supports many languages,
  includes Travis configuration and much more.

