#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pytest

from standardstreams import stdout


# ////////////////////////////////////////////////
#
# Setup
#
# ////////////////////////////////////////////////

# class definitions for tests

class Bogus(object):
    def __init__(self):
        pass


class BogusWithStr(object):
    def __init__(self):
        pass

    def __str__(self):
        return "__str__ success"


class BogusWithRepr(object):
    def __init__(self):
        pass

    def __repr__(self):
        return "__repr__ success"


class BogusWithBoth(object):
    def __init__(self):
        pass

    def __str__(self):
        return "__str__ success"

    def __repr__(self):
        return "__repr__ success"


# ///////////////////////////////////////////////////////
#
# pytest capsys capture tests
#    confirms capture of std output and std error streams
#
# ///////////////////////////////////////////////////////


def test_pytest_capsys(capsys):
    print("bogus text for a test")
    sys.stderr.write("more text for a test")
    out, err = capsys.readouterr()
    assert out == "bogus text for a test\n"
    assert out != "something else"
    assert err == "more text for a test"
    assert err != "something else"


# ////////////////////////////////////////////////
#
# stdout() parameter testing tests
#
# ////////////////////////////////////////////////

def test_stdout_msg_parameter_test_nonstring_casts_ok():
    stdout(str)  # confirm that string object casts to str without raising exception


def test_stdout_msg_parameter_test_nonstring_cast_fails_nonexistent_object():
    with pytest.raises(NameError):
        stdout(Fakeola)


def test_stdout_msg_parameter_test_object_nostr_norepr(capsys):
    bogus = Bogus()
    out, err = capsys.readouterr()
    stdout(bogus)  # confirm that this does not raise exception


def test_stdout_msg_parameter_test_object_str_norepr(capsys):
    bogus = BogusWithStr()
    stdout(bogus)
    out, err = capsys.readouterr()
    assert out == "__str__ success\n"


def test_stdout_msg_parameter_test_object_nostr_repr(capsys):
    bogus = BogusWithRepr()
    stdout(bogus)
    out, err = capsys.readouterr()
    assert out == "__repr__ success\n"


def test_stdout_msg_parameter_test_object_str_repr(capsys):
    bogus = BogusWithBoth()
    stdout(bogus)
    out, err = capsys.readouterr()
    assert out == "__str__ success\n"


def test_stdout_begin_parameter_test_true_ascii(capsys):
    stdout("This is a test message", begin="[test] ")
    out, err = capsys.readouterr()
    assert out == "[test] This is a test message\n"


def test_stdout_begin_parameter_test_false_ascii(capsys):
    with pytest.raises(TypeError):
        stdout("This is a test message", begin=123)
        out, err = capsys.readouterr()
        assert out == "123This is a test message\n"


def test_stdout_begin_parameter_test_true_unicode(capsys):
    if sys.version_info[0] == 2:
        msg = u"カイダーディー"
        beg_str = u'ディー '
    else:
        msg = "カイダーディー"
        beg_str = u'ディー '
    stdout(msg, begin=beg_str)
    out, err = capsys.readouterr()
    assert out == beg_str + msg + '\n'


def test_stdout_begin_parameter_test_false_unicode(capsys):
    with pytest.raises(TypeError):
        if sys.version_info[0] == 2:
            msg = u"カイダーディー"
        else:
            msg = "カイダーディー"
        beg_str = 123 # define as an integer
        stdout(msg, begin=beg_str)
        out, err = capsys.readouterr()
        assert out == beg_str + msg + '\n'


# ////////////////////////////////////////////////
#
# stdout() function tests with default parameters
#
# ////////////////////////////////////////////////


def test_stdout_missing_msg_parameter(capsys):
    with pytest.raises(TypeError):
        stdout()
        out, err = capsys.readouterr()
        assert out == "\n"


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


def test_stdout_ascii_reports_correct_statuscode_one(capsys):
    with pytest.raises(SystemExit):
        try:
            stdout("This is a test message", statuscode=1)
            out, err = capsys.readouterr()
            assert out == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stdout_ascii_reports_correct_statuscode_zero(capsys):
    with pytest.raises(SystemExit):
        try:
            stdout("This is a test message", statuscode=0)
            out, err = capsys.readouterr()
            assert out == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '0'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stdout_ascii_reports_correct_statuscode_minusone(capsys):
    with pytest.raises(SystemExit):
        try:
            stdout("This is a test message", statuscode=-1)
            out, err = capsys.readouterr()
            assert out == "This is a test message\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '-1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stdout_unicode_reports_correct_statuscode(capsys):
    if sys.version_info[0] == 2:
        msg = u"カイダーディー"
    else:
        msg = "カイダーディー"
    with pytest.raises(SystemExit):
        try:
            stdout(msg, statuscode=1)
            out, err = capsys.readouterr()
            assert out == msg + "\n"
        except SystemExit as exit_code:
            assert exit_code.__str__() == '1'  # tests the exit status code in the SystemExit exception
            raise exit_code


def test_stdout_bad_object_as_statuscode():
    with pytest.raises(NameError):
        stdout("This is a test message", statuscode=bogusobj)




