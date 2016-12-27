# -- coding: utf-8 --

from sys import argv

script, einz, zwei, drei, vier = argv

print "The script ist called:", script
print "Your first variable is:", int(einz)
print "Your second variable is:", zwei
print "Your third variable is:", drei, vier
a = raw_input("schreib etwas: ")
print "Du hast geschrieben: \"%s\"" % a

