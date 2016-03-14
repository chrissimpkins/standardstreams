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


def test_stdout_ascii_reports_correct_statuscode(capsys):
    with pytest.raises(SystemExit):
        try:
            stdout("This is a test message", statuscode=1)
            out, err = capsys.readouterr()
            assert out == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '1'  # tests the exit status code in the SystemExit exception
            raise exit_code



