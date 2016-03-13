#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# ///////////////////////////////////////////
#
# Standard Output Functions
#
# ///////////////////////////////////////////


def stdout(msg, statuscode=None):
    sys.stdout.write(msg + "\n")
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


def stdout_xnl(msg, statuscode=None):
    sys.stdout.write(msg)
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


def stdout_iter(iterable, statuscode=None):
    for msg in iterable:
        sys.stdout.write(msg + "\n")
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


# ///////////////////////////////////////////
#
# Standard Error Functions
#
# ///////////////////////////////////////////


def stderr(msg, statuscode=None):
    sys.stderr.write(msg + "\n")
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


def stderr_xnl(msg, statuscode=None):
    sys.stderr.write(msg)
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


def stderr_iter(iterable, statuscode=None):
    for msg in iterable:
        sys.stderr.write(msg + "\n")
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


# ///////////////////////////////////////////
#
# Standard Input Functions
#
# ///////////////////////////////////////////

def stdin():
    return sys.stdin.read()


def stdin_by_line():
    for line in sys.stdin.readlines():
        yield line


def prompt(msg):
    pass