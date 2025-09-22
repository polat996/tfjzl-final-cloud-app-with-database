#!/usr/bin/env python
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('✅ Superuser created successfully!')
    print('Username: admin')
    print('Password: admin123')
    print('Email: admin@example.com')
else:
    print('ℹ️ Superuser already exists!')
    print('Username: admin')
    print('Password: admin123')
