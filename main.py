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
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
	def get(self):
		
		name_form = '''
			<form action ="/setname" method="post">
					<label for="your_name">
						Enter your name here:
					</label>
					<input name="your_name" id="your_name" type="text" size="12"/>
					<input type="submit" value="Set" />
				</form>
			'''
		
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write('''
		<html>
			<head>
				<title>What is your name?</title>
			</head>
			<body>
			%s
			</body>
		</html>
		''' % (name_form))

application = webapp.WSGIApplication([('/', MainPage)], debug = True)

def main ():
	run_wsgi_app(application)
	
if __name__ == '__main__':
	main()