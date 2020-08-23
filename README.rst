folklore-config
===============

.. image:: https://travis-ci.org/maralla/folklore-config.svg?branch=master
    :target: https://travis-ci.org/maralla/folklore-config

The Folklore framework configuration manager.

Configs are in yaml format stored in *app.yaml* by default. An
environment vairable ``FOLKLORE_APP_CONFIG_PATH`` can be used to change
the path of the yaml file.

To set current running environment of the app use environment vairable
``FOLKLORE_ENV``. The default env is ``dev``.

Usage
-----

For the given config files:

.. code:: yaml

    # app.yaml
    app_name: echo
    app: echo:service
    settings: settings

.. code:: python

    # settings.py
    DB_DSN = 'psycopg2+postgresql://root:123@localhost:5432/dev'

.. code-block:: python

    >>> # With this environment vairable set:
    >>> # FOLKLORE_ENV=prod
    >>>
    >>> from folklore_config import config
    >>> print(config.env)
    'prod'
    >>> print(config.app_name)
    'echo'
    >>> config.settings.update({'TEST': True, 'HELLO': 'world'})
    >>> print(config.settings['TEST'])
    True
    >>> print(config.settings['DB_DSN'])
    'psycopg2+postgresql://root:123@localhost:5432/dev'
