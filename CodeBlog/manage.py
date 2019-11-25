#!/usr/bin/env python
import os
import sys

from dotenv import load_dotenv
project_folder = os.path.expanduser('~/NerdVenture-CodeBlog')
load_dotenv(os.path.join(project_folder, '.env'))

if __name__ == "__main__":
    
    if os.getenv('IS_PRODUCTION')=='True':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CodeBlog.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CodeBlog.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
