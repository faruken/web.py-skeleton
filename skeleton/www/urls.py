# -*- coding: utf-8 -*-

"""URL definitions of the application. Regex based URLs are mapped to their
class handlers.
"""

from app.controllers.main_handler import IndexHandler

URLS = (
  r'^/', IndexHandler
)
