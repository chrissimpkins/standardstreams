#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO

from standardstreams import stdin, stdin_lines

# TODO: test binary data with BinaryIO


def test_stdin_text_ascii():
    sys.stdin = StringIO(u"test string")
    assert stdin() == u"test string"
    sys.stdin.close()


def test_stdin_text_unicode():
    sys.stdin = StringIO(u"カイダーディー")
    assert stdin() == u"カイダーディー"
    sys.stdin.close()


def test_stdin_lines_text_ascii():
    sys.stdin = StringIO(u"test string\nanother string")
    line_list = []
    for line in stdin_lines():
        line_list.append(line)
    assert line_list[0] == u"test string\n"
    assert line_list[1] == u"another string"
    sys.stdin.close()


def test_stdin_lines_text_unicode():
    sys.stdin = StringIO(u"カイダ\nーディー")
    line_list = []
    for line in stdin_lines():
        line_list.append(line)
    assert line_list[0] == u"カイダ\n"
    assert line_list[1] == u"ーディー"
    sys.stdin.close()
