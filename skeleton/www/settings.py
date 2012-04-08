# -*- coding: utf-8 -*-

"""Default options for the application.
"""

DEBUG = True

SESSION_TIMEOUT = 3600  # 1 Hour

HASH_KEY = ''
VALIDATE_KEY = ''
ENCRYPT_KEY = ''
SECRET_KEY = ''

DB_USERNAME = ''
DB_PASSWORD = ''
DB_PORT = 1234
DB = ''

def absolute(path):
  """Get the absolute path of the given file/folder.

  ``path``: File or folder.
  """
  import os
  PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
  return os.path.normpath(os.path.join(PROJECT_DIR, path))
