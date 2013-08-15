from BeautifulSoup import *
from mechanize import *
import ConfigParser
import json

class MoodleBrowser:
	def __init__(self):
		self.b=Browser()
		self.b.set_handle_robots(False)
		self.conf=json.loads(open('conf.json').read())
		
	def login(self,user,passwd):
		self.b.open(self.conf['site'])
		self.b.select_form(nr=1)
		for i in range(3):
			self.b.form.controls[i].readonly = False
		self.b["username"] = user
		self.b["password"] = passwd
		print "submitting"
		resp = self.b.submit()
		if '/login/' in self.b.geturl():
			return False
		return True
		
	def getcourselist(self):
		resp=self.b.open(self.conf['site'])
		soup = BeautifulSoup(resp.get_data())
		links=[{"name":str(h3.find('a').contents[0]),"link":h3.find('a')['href']} for h3 in soup.findAll('h3', { "class" : "name" })]
		print links
