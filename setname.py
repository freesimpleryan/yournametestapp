from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import models

class SetName(webapp.RequestHandler):
	def post(self):
		models.add_name(self.request.get('your_name'))
		
		self.redirect('/')
		
application = webapp.WSGIApplication([('/setname', SetName)], debug=True)

def main():
	run_wsgi_app(application)
	
if __name__ == '__main__':
	main()
	
