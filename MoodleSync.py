from MoodleBrowser import *

passwd = open('.pass').read().strip()

a=MoodleBrowser()
a.login('alankar.kotwal',passwd)
