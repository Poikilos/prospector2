prospector
==========

.. image:: https://img.shields.io/pypi/v/prospector2.svg
   :target: https://pypi.python.org/pypi/prospector2
   :alt: Latest Version of Prospector
.. image:: https://travis-ci.org/landscapeio/prospector2.png?branch=master
   :target: https://travis-ci.org/landscapeio/prospector2
   :alt: Build Status
.. image:: https://landscape.io/github/landscapeio/prospector/master/landscape.png?style=flat
   :target: https://landscape.io/github/landscapeio/prospector/master
   :alt: Code Health
.. image:: https://img.shields.io/coveralls/landscapeio/prospector2.svg?style=flat
   :target: https://coveralls.io/r/PyCQA/prospector
   :alt: Test Coverage
.. image:: https://readthedocs.org/projects/prospector2/badge/?version=latest
   :target: http://prospector2.readthedocs.io/
   :alt: Documentation


Read This First!
----------------

Prospector was originally written as part of https://landscape.io and has been moved across
to the PyCQA group of python code analysis tools to enable it to have more maintainers and
more frequent bug fixes and updates.

The official version (which is still supported by myself, @carlio) is at https://github.com/PyCQA/prospector.

This fork is to keep a version which will continue to run under Python2, as various dependencies and libraries
that prospector uses or tests - such as pylint, astroid, and Django - have stopped supporting python2.

This version of prospector will use older versions of those libraries in order to keep Python2 compatability,
however, the main reason for this is to allow Landscape.io to continue checking python-2-based codebases. You
are welcome to use this in your own projects and I will do my best to keep it working however the recommended
use case in personal projects or your own CI setup is to migrate to using Python3 and the PyCQA version of prospector.

Additionally this fork will not support Python3 but instead be only supporting Python2.

About
-----

Prospector is a tool to analyse Python code and output information about
errors, potential problems, convention violations and complexity.

It brings together the functionality of other Python analysis tools such as
`Pylint <http://docs.pylint.org/>`_,
`pep8 <http://pep8.readthedocs.org/en/latest/>`_,
and `McCabe complexity <https://pypi.python.org/pypi/mccabe>`_.
See the `Supported Tools <http://prospector.readthedocs.io/en/latest/supported_tools.html>`_
documentation section for a complete list.

The primary aim of Prospector is to be useful 'out of the box'. A common complaint of other
Python analysis tools is that it takes a long time to filter through which errors are relevant
or interesting to your own coding style. Prospector provides some default profiles, which
hopefully will provide a good starting point and will be useful straight away, and adapts
the output depending on the libraries your project uses.

Installation
------------

Prospector can be installed using ``pip`` by running the following command::

    pip install prospector


Optional dependencies for Prospector, such as ``pyroma`` can also be installed by running::

    pip install prospector[with_pyroma]


For a list of all of the optional dependencies, see the optional extras section on the ReadTheDocs
page on `Supported Tools Extras <https://prospector.readthedocs.io/en/latest/supported_tools.html#optional-extras>`_.

For more detailed information on installing the tool, see the
`installation section <http://prospector.readthedocs.io/en/latest/#installation>`_ of the tool's main page
on ReadTheDocs.

If pip shows version conflicts (packages requiring older versions of other packages), some packages may need to be held back manually:

    pip uninstall flake8 pep8-naming
    pip install prospector2 flake8==3.5.0 pep8-naming==0.3.3


Documentation
-------------

Full `documentation is available at ReadTheDocs <http://prospector.readthedocs.io>`_.

Usage
-----

Simply run prospector from the root of your project::

    prospector

This will output a list of messages pointing out potential problems or errors, for example::

    prospector.tools.base (prospector/tools/base.py):
        L5:0 ToolBase: pylint - R0922
        Abstract class is only referenced 1 times

Options
```````

Run ``prospector --help`` for a full list of options and their effects.

Output Format
~~~~~~~~~~~~~

The default output format of ``prospector`` is designed to be human readable. For parsing
(for example, for reporting), you can use the ``--output-format json`` flag to get JSON-formatted
output.

Profiles
~~~~~~~~

Prospector is configurable using "profiles". These are composable YAML files with directives to
disable or enable tools or messages. For more information, read
`the documentation about profiles <http://prospector.readthedocs.io/en/latest/profiles.html>`_.

If your code uses frameworks and libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often tools such as pylint find errors in code which is not an error, for example due to attributes of classes being
created at run time by a library or framework used by your project.
For example, by default, pylint will generate an error for Django models when accessing ``objects``, as the
``objects`` attribute is not part of the ``Model`` class definition.

Prospector mitigates this by providing an understanding of these frameworks to the underlying tools.

Prospector will try to intuit which libraries your project uses by
`detecting dependencies <https://github.com/landscapeio/requirements-detector>`_ and automatically turning on
support for the requisite libraries. You can see which adaptors were run in the metadata section of the report.

If Prospector does not correctly detect your project's dependencies, you can specify them manually from the commandline::

    prospector --uses django celery

Additionally, if Prospector is automatically detecting a library that you do not in fact use, you can turn
off autodetection completely::

    prospector --no-autodetect

Note that as far as possible, these adaptors have been written as plugins or augmentations for the underlying
tools so that they can be used without requiring Prospector. For example, the Django support is available as a pylint plugin.

Strictness
~~~~~~~~~~

Prospector has a configurable 'strictness' level which will determine how harshly it searches for errors::

    prospector --strictness high

Possible values are ``verylow``, ``low``, ``medium``, ``high``, ``veryhigh``.

Prospector does not include documentation warnings by default, but you can turn
this on using the ``--doc-warnings`` flag.


License
-------

Prospector is available under the GPLv2 License.
