#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.""" #what this file does

import os #work with environment variables and file paths
import sys #access command-line arguments passed to the script


def main():
    """Run administrative tasks.""" #this function is the main entry point for running Django commands

    #which settings file to use (in this case, from the transportation_Database project)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transportation_Database.settings')
    try:
        #try to import Django's built-in command-line executor
        from django.core.management import execute_from_command_line
    except ImportError as exc:
         #if Django isn't installed or activated in the virtual environment, show a helpful error
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    #runs the command that was passed in the terminal suvh as runserver, migrate, and etc.
    execute_from_command_line(sys.argv)

#this makes sure the script only runs when executed directly (not when imported)
if __name__ == '__main__':
    main()
