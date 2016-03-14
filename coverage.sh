#!/bin/sh

coverage run --source standardstreams -m py.test
coverage report -m
coverage html

coverage xml
codecov --token=$CODECOV_STANDARDSTREAMS
