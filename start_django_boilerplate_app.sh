#!/bin/bash

# Activate virtual environment
source .venv/bin/activate

# Start Django app on port 8007
python3 manage.py runserver 0.0.0.0:8007
