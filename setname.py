from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from PyQRNative import QRErrorCorrectLevel
from PyQRNativeGAE import QRCode
import models

class SetName(webapp.RequestHandler):
	def post(self):
		your_name = self.request.get('your_name')
		models.add_name(your_name)
		
		url = 'http://yournametestapp.appspot.com/yourname?' + your_name
		qr = QRCode(QRCode.get_type_for_string(url), QRErrorCorrectLevel.L)
		qr.addData(url)
		qr.make()
		self.response.headers['Content-Type'] = 'image/png'
		self.response.out.write(qr.make_image())
		
application = webapp.WSGIApplication([('/setname', SetName)], debug=True)

def main():
	run_wsgi_app(application)
	
if __name__ == '__main__':
	main()
	
