#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

from standardstreams import stdin


def test_stdin_ascii():
    sys.stdin = StringIO(u"test string")
    assert stdin() == u"test string"
    sys.stdin.close()


def test_stdin_unicode():
    sys.stdin = StringIO(u"カイダーディー")
    assert stdin() == u"カイダーディー"
    sys.stdin.close()

