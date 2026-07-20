#!/bin/bash
# Clean Build script for Vercel Deployment
set -e

echo "==> [BUILD] Upgrading pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "==> [BUILD] Installing dependencies from requirements.txt..."
python3 -m pip install -r requirements.txt --break-system-packages

echo "==> [BUILD] Collecting static files..."
python3 manage.py collectstatic --noinput

echo "==> [BUILD] Running database migrations..."
python3 manage.py migrate --noinput

echo "==> [BUILD] Build successful!"
