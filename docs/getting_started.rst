Getting Started
===============

This page details how to get started with molecool. 

Installation
------------
To install molecool, you will need an environment with the following packages:

* Python 3.11
* Numpy
* Matplotlib

Once you have these packages, clone the repository, then you can install molecool using pip::

    pip install -e .

Usage
-----
Here is an example of using molecool

.. code-block:: python

    import molecool

    symbols, coordinates = molecool.open_pdb('water.pdb')

    print(symbols)
    print(coordinates)