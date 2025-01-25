#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Start Django app
python3 manage.py runserver 0.0.0.0:8002

