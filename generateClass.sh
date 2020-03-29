#!/bin/sh

# https://github.com/FebruaryBreeze/json-schema-to-class
# https://pypi.org/project/genson/
# pip install json-schema-to-class
# pip install Pygments
# pip install genson
# manually run the following to reverse engineer python classes

# Assume the input Google Location History file is called "2020_MARCH,json"

# generate Location History JSON schema from an example Google Location History file
genson -i 2 2020_MARCH.json > LocationHistory.schema.json

# generate Python class file from JSON Schema, pygmentize is to visualise code on terminal
json-schema-to-class LocationHistory.schema.json --indent 2 | pygmentize
json-schema-to-class LocationHistory.schema.json --indent 2 > LocationHistory.class.py
