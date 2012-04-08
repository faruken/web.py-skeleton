# -*- coding: utf-8 -*-

"""This module contains the main handler of the application.
"""

import web
from . import render


class IndexHandler(object):
  """Homepage of the app.
  """
  def GET(self):
    """Returns the homepage (`index.html`) of the app.
    """
    return render.index(title='Hello World')
