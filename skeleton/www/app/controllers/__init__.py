# -*- coding: utf-8 -*-

"""Mako template options which are used, basically, by all handler modules in
controllers of the app.
"""

from web.contrib.template import render_mako
from settings import (absolute, DEBUG)

# Mako Template options
render = render_mako(
  directories=[absolute('app/views')],
  module_directory=absolute('tmp/mako_modules'),
  cache_dir=absolute('tmp/mako_cache'),
  input_encoding='utf-8',
  output_encoding='utf-8',
  default_filters=['decode.utf8'],
  encoding_errors='replace',
  filesystem_checks=DEBUG,
  collection_size=512
)
