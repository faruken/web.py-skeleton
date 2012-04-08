# -*- coding: utf-8 -*-

"""Pre-processors and customizations for the application.
"""

import web
from app.controllers import render

def header_html():
  """Global header setter for `text/html` documents.
  """
  web.header('Content-Type', 'text/html; charset=UTF-8')

def notfound():
  """Customized 404 Not Found message.
  """
  web.ctx.status = '404 Not Found'
  return web.notfound(str(render._404()))

def internalerror():
  """Customized 500 Internal Server Error message.
  """
  web.ctx.status = '500 Internal Server Error'
  return web.internalerror(str(render._500()))
