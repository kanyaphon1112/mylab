#!/bin/bash
# Build script for Vercel deployment
set -e

echo "==> Installing Python dependencies..."
python3 -m pip install -r requirements.txt --break-system-packages

echo "==> Collecting static files..."
python3 manage.py collectstatic --noinput

echo "==> Running database migrations..."
python3 manage.py migrate --noinput

echo "==> Build complete!"
