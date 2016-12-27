# -*- coding: utf-8 -*-

# Dictionary: iPhone* as keys and release years as values

released = {
	"iPhone 1": 2007,
	"iPhone 1": 2017,
	"iPhone 3G": 2008,
	"iPhone 3GS": 2009,
	"iPhone 4": 2010,
	"iPhone 4S": 2011,
	"iPhone 5": 2012,
	"iPhone 5S": 2013,
	"iPhone 5C": 2013,
	"iPhone 5A": 2222
}
print u"\nIteration über Dict mit seinen key/value pairs (ungeordnet):"
print "-" * 90
for phone in released:
	print phone, '\t', released[phone]

print u"\nIst es möglich die Einträge geordnet auszugeben?"
print "-" * 90

print u"""# Nicht direkt. Denn ein Dictionary kann nicht
# sortiert werden! Versucht man es dennoch, z.B. so:

>> iphone = released	# weise Dict der Variable iphone zu
>> iphone.sort()	# sortiere iphone


# bekommt man folgeden Fehler:
"""

# Dazu der ausführbarer Code, der bis auf die print Anweisungen
# nicht in der Konsole zu sehen sein wird
try:	
	iphone = released		# schreibe das Dict in die Variable iphone
	iphone.sort()       	# sortiere iphone
	
	for phone in iphone:	# iteriere über "sortiertes" dict
		print phone
except AttributeError:
	print u"""
>> Traceback (most recent call last):
>> File "tmp.py", line 28, in <module>
>> 	iphone.sort()
>> AttributeError: 'dict' object has no attribute 'sort'
	

# Auf Deutsch gesagt: Ein Dict verfügt nicht über die
# Eigenschaft 'sort', kann also NICHT sortiert werden!
# x.sort() ist eine Methode von veränderlichen Sequenz-Objekten 
# wie z.B. Listen oder Bytearrays 
# [s. Python 2.7.7 Dokumentation 5.6.4 --> 'Mutable Sequence Types']

	
DIE NÄCHSTEN BEISPIELE ZEIGEN, WIE MAN DIE AUSGABE DENNOCH ORDNEN KANN.
"""

print u"\nIteration über Liste mit SCHLÜSSEL-WERT-PAAR-Tupeln (ungeordnet):" # //////////
print "-" * 90

for phone, year in released.items():	# Iteration über SCHLÜSSEL-WERT-Paar-Tupel
	print "%s  \t%i" % (phone, year)	# die Ausgabe ist ungeordnet
	
print u"\nIteration über sortiere Liste mit SCHLÜSSEL-WERT-Paar-Tupeln:" # //////////////
print "-" * 90
print u"SCHLÜSSEL:\t", "WERTE:\n"
iPhone = released.items()	# Liste mit SCHLÜSSEL-WERT-Paar-Tupeln erzeugen
iPhone.sort()				# Liste sortieren

for phone, year in iPhone:	# jetzt iterieren wir über die sortiere Liste
	print "%s  \t%i" % (phone, year)	# dadruch erfolgt eine geordnete Ausgabe

print '\n'
print u"""# Wie am iPhone 5A zusehen ist, erfolgt die Sortierung
# anhand der SCHLÜSSEL (keys) und nicht der WERTE (values),
# sont wäre iPhone 5A an der letzten Stelle.
"""
	
print u"\nIteration über sortiere SCHLÜSSEL-Liste:" # ///////////////////////////////////
print "-" * 90
iPhone = released.keys()
iPhone.sort()

for phone in iPhone:		# Iteration über sortiere SCHLÜSSEL-Liste
	print phone, '\t', released[phone]

print '\n'
print u"""# Das Ergebnis ist das gleiche wie bei der Iteration
# über die sortieren SCHLÜSSEL-WERT-Paar-Tupel.



UND WAS IST, WENN ICH DIE AUSGABE NACH DEN JAHREN SORTIEREN MÖCHTE?

# Wir könnten zunächst Folgendes versuchen:
"""
	
print u"\nIteration über sortiere WERTE-Liste:" # ///////////////////////////////////////
print "-" * 90

years = released.values()
years.sort()
for year in years:
	print year 

print '\n'
print u"""# Das ist zwar schön und gut. ABER nun fehlt uns das
# Mapping zu den SCHLÜSSELn. Wir können auch nicht analog zum
# vorherigen Beispiel (released[phone]) jetzt released[year] sagen,
# weil ein Dict nur SCHLÜSSEL als Indexe akzeptiert und nicht
# in umgekehrter Weise von den WERTEn auf die zugehörigen SCHLÜSSEL
# schließen kann.



WIR MÜSSEN ALSO IRGENDWIE SCHLÜSSEL UND WERTE VERTAUSCHEN,
WENN WIR DIE AUSGABE NACH DEN JAHREN SORTIEREN MÖCHTEN!

# 1. Möglichkeit (dictionary comprehension):

>> new_dict = {year:phone for phone,year in released.iteritems()}

# Aus unserem Dict 'released' haben wir damit ein neues Dict 'new_dict'
# erzeugt, in dem SCHLÜSSEL und WERTE vertauscht sind, d.h. aus
# SCHLÜSSELn sind WERTE und aus WERTEn sind SCHLÜSSEL geworden.
# Nun sind also Jahre die SCHLÜSSEL und iPhone Modelle die WERTE!
# Und die ungeordnete Ausgabe sieht so aus:

SCHLÜSSEL	WERTE
"""

new_dict = {year:phone for phone,year in released.iteritems()}

for year in new_dict:
	print str(year), '\t\t', new_dict[year]

print '\n', u"""
# BEACHTE: Im alten Dict haben wir den WERT '2013' doppelt
# (beim iPhone 5S und 5C). Da SCHLÜSSEL unique (eindeutig) sein
# MÜSSEN - es also KEINE zwei oder mehr gleiche SCHLÜSSEL geben darf,
# geht uns bei der Umwandlung ein Eintrag verloren (iPhone 5S)


# 2. Möglichkeit (intuitiv - mit uns bereits bekannten Mittel):

>> new_dict = {}			# leeres Dict erzeugen
>> for k, v in released.items():	# über Liste mit SCHLÜSSEL-WERT-Paar-Tupeln iterieren
>> 	new_dict[v] = k			# Eintrag in das leere Dict hinzufügen,
>> 					# 	dabei den WERT 'v' (für value) als SCHLÜSSEL
>> 					# 	und den SCHLÜSSEL 'k' (für key) als WERT
>> 					# 	verwenden
"""

new_dict = {}					# leeres Dict erzeugen
for k, v in released.items():	# über Liste mit SCHLÜSSEL-WERT-Paar-Tupeln iterieren
	new_dict[v] = k				# Eintrag in das leere Dict hinzufügen,
								# 	dabei den WERT 'v' (für value) als SCHLÜSSEL
								# 	und den SCHLÜSSEL 'k' (für key) als WERT
								# 	verwenden
print u"""
# Die Ausgabe können wir wieder mit Hilfe von Iteration über
# eine Liste mit SCHLÜSSEL-WERT-PAAR-Tupeln, die wir aus dem
# neuen Dict 'new_dict' erzeugen realisieren.
"""

print u"\nIteration über Liste mit SCHLÜSSEL-WERTE-PAAR-Tupeln (ungeordnet):" # /////////
print "-" * 90								
								
years = new_dict.items()
for k, v in years:
	print v,'\t', k
print '\n'

print u"""
# Nun sind wir in der Lage die Ausgabe sinnvoll (nach Jahren) zu ordnen
# ohne das Mapping zu verlieren:
"""	

print u"\nIteration über sortiere Liste mit SCHLÜSSEL-WERTE-PAAR-Tupeln:" # /////////////
print "-" * 90	

years.sort()
for k, v in years:
	print v,'\t', k
print '\n'

#
# DEN KRAM AB HIER WIEDER LÖSCHEN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#

new_dict[2014] = "iPhone 6"
print u"Lösche iPhone 5A:\n"
del new_dict[2222]

print u"Ändere iPhone 5C in 5S\n"
new_dict[2013] = "iPhone 5S"

kvt_new_dict = new_dict.items()
kvt_new_dict.sort()
for k, v in kvt_new_dict:
	print v, '\t', k
	
print u"Unser Dict enhält %i Einträge" % len(new_dict)

jahre = [2001, 2002, 2003, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2016]
enthalten = []
nicht_enthalten = []
x = 0
for i in jahre:
	if i in new_dict:
		enthalten.append(i)
	else:
		nicht_enthalten.append(i)

# Im Dict enhaltene Jahre		
print u"\nDie Jahre", 
for y in enthalten[0:-2]:
	print str(y) + ',',
print enthalten[-2],
print "und %d" % enthalten[-1],
print 'sind im Dict enthalten.'

# Im Dict nicht enthaltene Jahre
print u"\nDie Jahre", 
for y in nicht_enthalten[0:-2]:
	print str(y) + ',',
print nicht_enthalten[-2],
print "und %d" % nicht_enthalten[-1],
print 'sind dagegen nicht in unserem Dict!'





























