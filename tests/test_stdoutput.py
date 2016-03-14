#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

from standardstreams import stdout


def test_stdout_capsysfail(capsys):    # confirm that capsys capturing standard out appropriately
    stdout("bogus text for a test")
    out, err = capsys.readouterr()
    assert out != "something else"
    assert out == "bogus text for a test\n"


def test_stdout_ascii(capsys):
    stdout("This is a test message")
    out, err = capsys.readouterr()
    assert out == "This is a test message\n"


def test_stdout_unicode(capsys):
    if sys.version_info[0] == 2:
        msg = u"カイダーディー"
    else:
        msg = "カイダーディー"
    stdout(msg)
    out, err = capsys.readouterr()
    assert out == msg + "\n"


