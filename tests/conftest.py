# -*- coding: utf-8 -*-

import mock
import os
import pytest


@pytest.fixture(autouse=True)
def app_yaml():
    with mock.patch.dict(os.environ,
                         {'FOLKLORE_APP_CONFIG_PATH': 'tests/app.yaml'}):
        yield
