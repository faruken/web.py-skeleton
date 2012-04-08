#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The only file which is directly executed. There's no reason to modify this
file.
"""

import web
from settings import DEBUG
from urls import URLS
from app.tools.app_processor import (header_html, notfound, internalerror)

web.config.debug = DEBUG

app = web.application(URLS, globals(), autoreload=False)
app.notfound = notfound
app.internalerror = internalerror
app.add_processor(web.loadhook(header_html))

if __name__ == '__main__':
  app.run()
