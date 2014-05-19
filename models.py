from google.appengine.ext import db
	
class Names(db.Model):
	your_name = db.StringProperty(default='test')

def get_name(user_name=None):
	if user_name:
		key = db.Key.from_path('Names', user_name)
		name = db.get(key)
		return name
	else:
		return None
		
def add_name(user_name=None):
	if user_name:
		n = Names(your_name=user_name)
		n.put()


