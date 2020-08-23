# -*- coding: utf-8 -*-

import os
import mock


THRIFT_FILE = os.path.join(os.path.dirname(__file__), 'echo.thrift')


def test_load_config():
    from folklore_config import config
    assert config._confs == {
        'app_name': 'echo',
        'settings': 'settings',
        'app': 'echo:service',
        'thrift_file': 'tests/echo.thrift',
        'requirements': 'requirements.txt',
        'thrift_protocol_class': 'settings.DemoClass',
    }


def test_env_config():
    from folklore_config import config
    assert config.env == 'dev'
    with mock.patch.dict(os.environ, {'FOLKLORE_ENV': 'prod'}):
        assert config.env == 'prod'


def test_app_config():
    from folklore_config import config
    assert config.app == 'echo:service'
    assert config.app_name == 'echo'
    assert config.requirements == 'requirements.txt'
    assert config.thrift_protocol_class.__name__ == 'DemoClass'
    assert config.thrift_file == THRIFT_FILE
    assert config.worker_connections == 1000
    assert config.workers == 2
    assert config.timeout == 30
    assert config.client_timeout == 1200
    assert config.port == 8010


def test_app_config_settings():
    from folklore_config import config
    assert config.settings
    assert (config.settings['DB_DSN'] ==
            'psycopg2+postgresql://root:123@localhost:5432/dev')
