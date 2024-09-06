#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

cd api/

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Start the server in the background
python manage.py runserver &

# Install npm dependencies
cd ../dash-data
npm install

# Run the server
npm run dev
