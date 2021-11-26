#!/bin/sh
python3 -m virtualenv env
source env/bin/activate
pip install $(./compile_dependencies.py)
