#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

from standardstreams import stderr


def test_stderr_capsysfail(capsys):    # confirm that capsys capturing standard out appropriately
    stderr("bogus text for a test")
    out, err = capsys.readouterr()
    assert err != "something else"
    assert err == "bogus text for a test\n"


# ///////////////////////////////////////////
#
# stderr() function tests
#
# ///////////////////////////////////////////

def test_stderr_ascii(capsys):
    stderr("This is a test message")
    out, err = capsys.readouterr()
    assert err == "This is a test message\n"


def test_stderr_unicode(capsys):
    if sys.version_info[0] == 2:
        msg = u"カイダーディー"
    else:
        msg = "カイダーディー"
    stderr(msg)
    out, err = capsys.readouterr()
    assert err == msg + "\n"


def test_stderr_ascii_reports_correct_statuscode_one(capsys):
    with pytest.raises(SystemExit):
        try:
            stderr("This is a test message", statuscode=1)
            out, err = capsys.readouterr()
            assert err == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stderr_ascii_reports_correct_statuscode_zero(capsys):
    with pytest.raises(SystemExit):
        try:
            stderr("This is a test message", statuscode=0)
            out, err = capsys.readouterr()
            assert err == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '0'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stderr_ascii_reports_correct_statuscode_minusone(capsys):
    with pytest.raises(SystemExit):
        try:
            stderr("This is a test message", statuscode=-1)
            out, err = capsys.readouterr()
            assert err == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '-1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stderr_unicode_reports_correct_statuscode(capsys):
    if sys.version_info[0] == 2:
        msg = u"カイダーディー"
    else:
        msg = "カイダーディー"
    with pytest.raises(SystemExit):
        try:
            stderr(msg, statuscode=1)
            out, err = capsys.readouterr()
            assert err == msg + "\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stderr_bad_object_as_statuscode():
    with pytest.raises(NameError):
        stderr("This is a test message", statuscode=bogusobj)