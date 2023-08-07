#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DATABASE_URL", "postgres://dzpispkp:n2Re-UTYz06WFM4kwCOQwneCNygqaCEU@surus.db.elephantsql.com/dzpispkp")
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_venuemanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()