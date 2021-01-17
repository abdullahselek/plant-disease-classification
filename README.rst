plant-disease-classification
============================

.. image:: https://img.shields.io/pypi/v/plant-disease-classification.svg
    :target: https://pypi.org/pypi/plant-disease-classification/

.. image:: https://img.shields.io/pypi/pyversions/plant-disease-classification.svg
    :target: https://pypi.org/project/plant-disease-classification

A Python module that classifies disease on plants. You can classify plant images from Python or
from the command line with a simple classification library.

Built using Deep Learning and Convolutional Networks models trained `here <https://github.com/abdullahselek/plant-disease-classification-pytorch/>`_.

This also provides a simple plant disease classification command line tool that lets you do face recognition on a folder of images from the command line.

Installation
------------

You can install plant-disease-classification using::

    $ pip install plant-disease-classification

Getting the code
----------------

The code is hosted at https://github.com/abdullahselek/plant-disease-classification

Check out the latest development version anonymously with::

    $ git clone git://github.com/abdullahselek/plant-disease-classification.git
    $ cd plant-disease-classification

To install dependencies, run either::

    $ pip install -r requirements.txt

To install the minimal dependencies for production use (i.e., what is installed
with ``pip install plant-disease-classification``) run::

    $ pip install -r requirements.txt

Usage
=====

Classification using Python
---------------------------

.. code:: python

    from plant_disease_classification import api

    # Classification with image path
    result = api.classify(image_path="YOUR_IMAGE_PATH")

    # Classification with image data
    result = api.classify(image_data=YOUR_IMAGE_DATA)

Classification via CLI
----------------------

.. code:: bash

    python -m plant_disease_classification -p testdata/4507d7a208e839e34466ba7d7bdb144e.jpg

    python -m plant_disease_classification -d BASE64_ENCODED_IMAGE_DATA
