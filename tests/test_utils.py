# -*- coding: utf-8 -*-

import mock
import sys


def test_load_class():
    from folklore_config.utils import load_class
    Test = type('Test', (object,), {})
    mock_module = mock.Mock(Test=Test)
    with mock.patch.dict(sys.modules,
                         {'hello': mock.Mock(), 'hello.world': mock_module}):
        ret = load_class('hello.world.Test')
        assert ret is Test
        ret = load_class(Test)
        assert ret is Test
