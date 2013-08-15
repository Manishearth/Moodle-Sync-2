from MoodleBrowser import *

passwd = open('.pass').read().strip()

a=MoodleBrowser()
a.login('manishg',passwd)
#print a.getcourselist()
print json.dumps(a.getcoursecalendar('http://moodle.iitb.ac.in/course/view.php?id=163'),indent=1)

