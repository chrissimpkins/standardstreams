#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Define basestring in Python version independent manner for string tests
try:  # pragma: no cover
  basestring
except NameError:  # pragma: no cover
  basestring = str

# TODO: stdout_json: std output formatted as json
# TODO: format the width in characters

# ///////////////////////////////////////////
#
# Standard Output Functions
#
# ///////////////////////////////////////////


def stdout(msg, begin="", end="\n", statuscode=None):
    """Writes msg string (or __str__ representation of msg object) to the standard output stream with option
    to exit program if the statuscode function parameter is defined with an exit status code integer.

    Strings can be prepended and appended to the msg string with function parameters.  By default, a
    platform-dependent newline character is appended to the string before the standard output stream write.
    This behavior can be redefined in the `end` function parameter.

    :param msg: The data to print in the standard output stream. Uses string representation if not a string type
    :param end: (optional) The string to append to the msg string. Default = '\n'
    :param begin: (optional) The string to prepend to the msg string. Default = empty string
    :param statuscode: (optional) an integer that represents the exit status code."""

    # Parameter type tests
    # (Note: basestring redefined to str for Py3 in module head)
    if not isinstance(msg, basestring):
        msg = str(msg)  # cast to str type for any object that is not an instance of basestring (Py2) or str (Py3)

    if not isinstance(begin, basestring):
        raise TypeError("begin keyword parameter must be defined with a string type")

    if not isinstance(end, basestring):
        raise TypeError("end keyword parameter must be defined with a string type")

    if statuscode is not None:
        if not isinstance(statuscode, int):
            raise TypeError("statuscode keyword parameter must be defined with an integer exit code value")

    # Write to standard output stream
    sys.stdout.write(begin + msg + end)

    # Handle request to raise SystemExit at the end of the standard output write
    if statuscode is not None:
        sys.exit(statuscode)

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
    """Writes msg to the standard error stream with option to exit program with the exit status code
    statuscode.  If statuscode is not defined, sys.exit() is not called by the function.

    :param msg: The data to print in the standard error stream
    :param statuscode: (optional) an integer that represents the exit status code."""

    sys.stderr.write(msg + "\n")
    if statuscode is not None:
        assert isinstance(statuscode, object)
        sys.exit(statuscode)


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
    """Reads and returns all data in the standard input stream.  The function blocks until all data is read.

    :returns: Standard input stream data
    """

    return sys.stdin.read()


def stdin_lines():
    """A generator function that reads and returns all data in the standard input stream delimited by newline
    characters.

    :returns: Standard input stream data by newline
    """
    for line in sys.stdin.readlines():
        yield line


# def stdin_comma():
#     pass

# def stdin_json():
#     pass

# def stdin_is_piped():
#     """Returns a boolean answer to the question 'Is the standard input being piped to the script from another
#     application rather than being run interactively?'
#
#     :returns: boolean.  True = standard input is piped from another program; False = standard input is not piped from
#     another program
#     """
#     if sys.stdin.isatty() is True:
#         return False
#     else:
#         return True

# def pipe():
#     pass
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
