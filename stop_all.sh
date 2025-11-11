#!/bin/bash

echo "🛑 Stopping all services..."

# Stop Celery
if pgrep -f 'celery' > /dev/null
then
    echo "Stopping Celery..."
    pkill -f 'celery'
else
    echo "Celery not running."
fi

# Stop Redis
if redis-cli ping &> /dev/null
then
    echo "Stopping Redis..."
    redis-cli shutdown
else
    echo "Redis not running."
fi

# Stop Django
if pgrep -f 'manage.py runserver' > /dev/null
then
    echo "Stopping Django server..."
    pkill -f 'manage.py runserver'
else
    echo "Django not running."
fi

# Stop Vite
if pgrep -f 'vite' > /dev/null
then
    echo "Stopping Vite..."
    pkill -f 'vite'
else
    echo "Vite not running."
fi

echo "✅ All components stopped."
