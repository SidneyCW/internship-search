#!/bin/bash

echo "🚀 Starting backend services..."

# Start Redis if not already running
if ! pgrep redis-server > /dev/null
then
    echo "Starting Redis..."
    redis-server --daemonize yes
else
    echo "Redis already running."
fi

# Activate virtual environment
source venv/bin/activate

# Start Django in the background
echo "Starting Django..."
nohup python manage.py runserver 127.0.0.1:8000 > django.log 2>&1 &

# Start Celery in the background
echo "Starting Celery worker..."
nohup celery -A backend worker -l info -n worker1@%h > celery.log 2>&1 &

echo "✅ Backend stack is running."
echo "Logs: django.log and celery.log"
