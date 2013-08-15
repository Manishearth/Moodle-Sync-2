#!/usr/bin/python

import mechanize as m
import os
import BeautifulSoup as bs
import getpass

os.system("clear")

print "Welcome to MoodleSync CLI!"
print "Enter your authentication details:"
print

username = raw_input("Username: ")
password = getpass.getpass()

b=m.Browser()
b.set_handle_robots(False)

b.open("http://moodle.iitb.ac.in")

b.select_form(nr=1)

for i in range(3):
	b.form.controls[i].readonly = False

b["username"] = username
b["password"] = password
resp = b.submit()
data = resp.get_data()

os.system("clear")

print "Done authentication!"
print
print "Please wait, getting course details..."
print

data = resp.get_data()

lines = data.split('\n')

ids = []
courses = []

idLen = 4

for i in range(len(lines)):
	if "Click to enter this course" in lines[i]:
		line = lines[i].split('"Click to enter this course" href="http://moodle.iitb.ac.in/course/view.php?id=')
		try:
			int(line[1][3])
			idLen = 4
		except ValueError:
			idLen = 3
		ids.append(line[1][0:idLen])
		courses.append(line[1].split('>')[1].split('<')[0])

print "Done getting course details!"
print
print "Syncing News Forum Data..."
print

nfLinks = []

for i in range(len(ids)):
	course = b.open("https://moodle.iitb.ac.in/course/view.php?id="+ids[i])
	source = course.get_data()

	lines = source.split('\n')

	for j in range(len(lines)):
		if "News forum" in lines[j]:
			line = lines[j].split('"')
			nfLinks.append(line[7])
			break

for i in range(len(nfLinks)):
	print courses[i]

	src = b.open(nfLinks[i]).get_data()

	lines = src.split('\n')

	postNames = []
	postLinks = []
	authNames = []

	for i in range(len(lines)):
		if '<tr class="discussion' in lines[i]:
			postLinks.append(lines[i].split('<td class="topic starter"><a href="')[1].split('"')[0])
			postNames.append(lines[i].split('<td class="topic starter"><a href="https://moodle.iitb.ac.in/mod/forum/discuss.php?id=')[1].split('>')[1].split('<')[0])
			i = i+2
			authNames.append(lines[i].split('>')[2].split('<')[0])
		if '</tbody></table><div class="paging"></div>' in lines[i]:
			break
		
	for i in range(len(postNames)):
		print postNames[i]+', '+authNames[i]+', '+postLinks[i]
		
	print

print

print "Done! Press any key to exit"
print "Thank you!"
os.sys.stdin.read(1)
os.system("reset")
