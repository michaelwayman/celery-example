#!/bin/bash

source .venv/bin/activate && cd src || exit
python3 ../auto_reload.py "$@"
