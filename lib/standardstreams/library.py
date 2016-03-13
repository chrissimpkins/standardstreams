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


# def stdout_xnl(msg, statuscode=None):
#     sys.stdout.write(msg)
#     if statuscode is not None:
#         assert isinstance(statuscode, object)
#         sys.exit(statuscode)
#
#
# def stdout_iter(iterable, statuscode=None):
#     for msg in iterable:
#         sys.stdout.write(msg + "\n")
#     if statuscode is not None:
#         assert isinstance(statuscode, object)
#         sys.exit(statuscode)


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


# def stderr_xnl(msg, statuscode=None):
#     sys.stderr.write(msg)
#     if statuscode is not None:
#         assert isinstance(statuscode, object)
#         sys.exit(statuscode)
#
#
# def stderr_iter(iterable, statuscode=None):
#     for msg in iterable:
#         sys.stderr.write(msg + "\n")
#     if statuscode is not None:
#         assert isinstance(statuscode, object)
#         sys.exit(statuscode)


# ///////////////////////////////////////////
#
# Standard Input Functions
#
# ///////////////////////////////////////////

def stdin():
    return sys.stdin.read()


def stdin_lines():
    for line in sys.stdin.readlines():
        yield line


# def stdin_is_piped():
#     """Returns a boolean answer to the question 'Is the standard input being piped to the script from another
#     application rather than being run interactively?'
#
#     :returns: boolean.  True = stadard input is piped from another program; False = standard input is not piped from
#     another program
#     """
#     if sys.stdin.isatty() is True:
#         return False
#     else:
#         return True
#
#
# def prompt(msg):
#     if (sys.version_info[0] == 2) is True:
#         try:
#             return raw_input(msg)
#         except NameError:
#             return input(msg)
#     else:
#         return input(msg)
