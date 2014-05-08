from google.appengine.api import users
from google.appengine.ext import db

class UserPrefs(db.Model):
	tz_offset = db.IntegerProperty(default=0)
	user = db.UserProperty(auto_current_user_add=True)
	
class Names(db.Model):
	your_name = db.StringProperty(default='test')
	
def get_userprefs(user_id=None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()
	
	key = db.Key.from_path('UserPrefs', user_id)
	userprefs = db.get(key)
	if not userprefs:
		userprefs = UserPrefs(key_name=user_id)
	return userprefs

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


