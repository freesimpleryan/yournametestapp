from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import urlparse

class YourName(webapp.RequestHandler):
	def get(self):
		name = self.request.query_string
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write('''
		<html>
			<head>
				<title> Your name is...</title>
			</head>
			<body>
				<p>%s</p>
			</body>
		</html>
		''' % (name))

application = webapp.WSGIApplication([('/yourname', YourName)], debug = True)
		
def main():
	run_wsgi_app(application)
	
if __name__ == '__main__':
	main()