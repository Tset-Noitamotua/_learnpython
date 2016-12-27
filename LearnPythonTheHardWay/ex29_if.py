# -*- coding: utf-8 -*-

personen = 20
katzen = 30
hunde = 15


if personen < katzen:
	print "Zu viele Katzen! Die Welt ist dem Untergang geweiht!"
	
if personen > katzen:
	print "Nicht zu viele Katzen! The Welt ist sicher!"
	
if personen < hunde:
	print "Die Welt ist vollgesabbert!"
	
if personen > hunde:
	print "Die Welt ist trocken!"
	
hunde += 5

if personen >= hunde:
	print "Es gibt mehr oder genauso viele Personen wie Hunde."
	
if personen <= hunde:
	print "Es gibt genauso viele oder weniger Personen als Hunde."
	
if personen == hunde:
	print "Menschen sind Hunde."
	
print "Ein Hund ist gestorben!"
hunde -= 1
	
if personen != hunde:
	print "Hurra, wir sind doch keine Hunde!"