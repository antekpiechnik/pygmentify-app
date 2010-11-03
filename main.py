#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re

def pygmentify(body, language):
  lexer = get_lexer_by_name(language)
  formatter = HtmlFormatter()
  result = re.sub('(^<div class="highlight">)|(<\/div>$)', '', highlight(body, lexer, formatter))
  return re.sub('(^<pre>)|(<\/pre>$)', '', result).rstrip()

class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write('Use POST instead! (with params "body" and "language")')
    def post(self):
        self.response.headers.add_header('Content-Type', 'text/plain')
        self.response.out.write(pygmentify(self.request.get('body'), self.request.get('language')))

def main():
    application = webapp.WSGIApplication([('/', MainHandler)])
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
