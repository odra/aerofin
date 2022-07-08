PyBov
=====

PyBov stands for "Python Ibovespa" which  is the company responsible for the brazilian stocks market.

This project provides dataclasses based schema for Ibovespa's historic archive so those can be parsed in a python project.

It also provides a "pybov" cli to parse historic archive files into json files.

License
-------

Apache 2.0

Sample Usage
------------

Command Line
************

Version
^^^^^^^

.. code-block:: shell

   $ pybov version
   $ v0.1.0

Parsing Files
^^^^^^^^^^^^^

.. code-block:: shell

   $ pybov parse SRC/ DEST/

- "SRC" being the source folder where archive text files are located (it will parse all files)
- "DEST" being an existing folder to store json files.

API
***

The project can also be used as a "data parsing" API.

A sample code on how to parse data from an archive file in python:

.. code-block:: python

    from pybov import types   

    with open('archvive.txt', 'r') as f:
      record = f.read().split('\n')[10].replace('\n', '')

    b3_record = types.Record.from_str(record)
