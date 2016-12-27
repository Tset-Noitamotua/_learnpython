# -*- coding: utf-8 -*-
""" DICTIONARY

	TODO: Dokument vervollständigen und aufräumen!!!!!!!!!!!!!!!!
	
	Was ist ein DICTionary (DICT)?
	
	Ein DICT ist ein Datentyp (data type) mit folgenden Eigenschaften:
	- Container, in dem Daten gespeichert und modifiziert werden können.
	- (ungeordnete, veränderliche) Sequenz von Einträgen.
	- Jeder Eintrag ist ein PAAR aus einem SCHLÜSSEL (key) und einem WERT (value).
	- Mapping zw. SCHLÜSSELn und WERTEn (mapping data type), 
	- d.h. jedem SCHLÜSSEL ist jeweils ein WERT zugeordnet.
	- Einträge = SCHLÜSSEL-WERT-PAARe (key/value pairs)
	- veränderlich (mutable) --> Einträge können hinzugefügt, gelöscht oder geändert werden
	- ungeordnet, d.h. Ausgabe entspricht nicht zwansläufig der Reihenfolge, in der
	- ... die Einträge hinzugefügt wurden.
	
	Was kann man mit einem DICT alles machen?
	
	- Leeres DICT erzeugen
	- DICT mit Eingrägen erzeugen
	- Einen neuen Eintrag hinzufügen
	- Auf einen Eintrag zugreifen (seinen WERT ausgeben und sonst wie damit arbeiten)
	- Einen Eintrag modifizieren (den WERT des Eintrags)
	- Einen Eintrag löschen (key/value pair)
	- Alle Einträge löschen --> leeres DICT
	- DICT in Konsole ausgeben (printen)
	- SCHLÜSSEL-Liste erzeugen und ausgeben (ungeordnet)
	- Sortiere SCHLÜSSEL-Liste erzeugen
	- WERTE-Liste (values) erzeugen und ausgeben
	- Liste der SCHLÜSSEL-WERT-PAAR-Tupel erzeugen und ausgeben
	- Über DICT-Einträge iterieren (ungeordnet)
	- Über WERTE-Liste iterieren (ungeordnet)
	- Über SCHLÜSSEL-Liste iterieren (ungeordnet)
	- Über Liste der SCHLÜSSEL-WERT-PAAR-Tupel iterieren (ungeordnet)
	- SCHLÜSSEL sortieren und geordnet ausgeben
	- WERTE sortieren und geordnet ausgeben
	- Größe (Anzahl Einträge) des DICT ermitteln
	- GET A VALUE OF A SPECIFIED KEY (TODO: Übersetzen!)
	- WERTE als String ausgeben (NUR bei keys vom Typ String möglich)
	- TODO: WERT in DICT suchen (Erweiterung: mehrere WERTE suchen)
	- DICT löschen
	
"""

print u"# LEERES DICT ERZEUGEN (DEKLARIEREN)" # //////////////////////////////////////////
woerter = {}

print u"# DICT MIT EINTRÄGEN ERZEUGEN (DEKLARIEREN)" # ///////////////////////////////////
woerter  = {
	"AAA": "Affe",	# das ist ein SCHLÜSSEL-WERT-PAAR (key/value pair)	
	"B": "Banane",		# Linke Seite: A, B, C --> SCHLÜSSEL (keys)
	"C": "Clown",	# Rechte Seite: Affe, Banane, Clown --> WERTE (values)
	"1": "Nummer"
}

print "# Einen Neuen Eintrag Hinzufügen" # //////////////////////////////////////////////
woerter['D'] = 'Dschungel'	# Dem DICT wird das SCHLÜSSEL-WERT-PAAR
								# 'D': 'Dschungel' hinzugefügt

# Auf Einen Eintrag Zugreifen (um damit zu arbeiten)
woerter["AAA"]		# Zugriff erfolgt über den key (hier: "AAA")
print woerter["AAA"]	# Den WERT eines Eintrags ausgeben (hier: den WERT von "AAA")
print "B:\t", woerter["B"]	# Den WERT von "B" ausgeben
var = woerter["AAA"]	# Den WERT (value) einer Variable zuweisen
#print var			# Variable ausgeben

# Einen Eintrag Modifizieren
woerter["AAA"] = "ARSCH"	# Zugriff erfolgt über den key "AAA", dem der WERT
						# "Affe" zugeordnet ist. Dieser WERT wird mit dem
						# WERT "ARSCH" überschrieben.
							
# Einen Eintrag Löschen (über key)
del woerter["AAA"]	# Eintrag mit dem key "AAA" löschen
print woerter

# DICT In Konsole Ausgeben (printen)
print "DICT:\t",  woerter

# Machen wir die Löschung von A wieder rückgängig, damit
# die nächsten Beispiele hübscher aussehen
woerter['AAA'] = 'Affenkopf'

print u"SCHLÜSSEL-LISTE ERZEUGEN (UNGEORDNET) /////////////////////////////////////////\n" 
woerter.keys()			# ['AAA', 'C', 'B', 'D']

print "KEYS:\t", woerter.keys()	# AUSGEBEN (ungeordnet)

print u"\nSORTIERTE SCHLÜSSEL-LISTE ERZEUGEN ////////////////////////////////////////////\n"
# alphanumerische aufsteigende Sortierung 
sorted(woerter)			# [1, 'AAA', 'B', 'C', 'D']
print sorted(woerter),	"\t# alphanumerisch aufsteigend" 
						# AUSGEBEN (geordnet)
						# TODO: Klären ... evtl. ist das veraltet (?)

# aufsteigende Sortierung nach der Länge der KEYS
print (sorted(woerter, key=len)), u"\t# nach der Länge der KEYS aufsteigend"
									# ['1', 'C', 'B', 'D', 'AAA']

						
print "\nWERTE-LISTE (VALUES) ERZEUGEN (UNGEORDNET) ///////////////////////////////////\n"
woerter.values()		# ['Affe', 'Banane', 'Clown']

# WERTE-Liste Ausgeben
print "VALUES:\t", woerter.values()	# >>> ['Affe', 'Banane', 'Clown', 'Dschungel']

print u"\nLISTE DER SCHLÜSSEL-WERT-PAAR-TUPEL ERZEUGEN (UNGEORDNET) ////////////////////\n"
woerter.items()		# [('AAA', 'Affe'), ('B', 'Banane'), ('C', 'Clown')]
					# Ausgabe analog zu den Beispielen oben mit print
print "ITEMS:\t", woerter.items()

print "-" * 30

print u"\n# NUR DIE SCHLÜSSEL AUSGEBEN" # /////////////////////////////////////////////////

for key in woerter:
	print key					# SCHLÜSSEL ausgeben

print u"\n# NUR DIE WERTE AUSGEBEN" # /////////////////////////////////////////////////////

								# Über DICT-Einträge Iterieren (Looping mit for-Schleife)
for key in woerter:				# Iteration über key/value pairs des DICT
	print woerter[key]			# WERT zum jeweiligen SCHLÜSSEL ausgeben (ungeordnet)
	
print u"\n# SCHLÜSSEL UND WERTE AUSGEBEN (Alternative 1)" # ////////////////////////////////	

liste_woerter = woerter.items()	# Liste mit Tupeln aus SCHLÜSSEL-WERT-PAARen erzeugen
for key, value in liste_woerter:
	print key, '-', value
	
print u"\n# SCHLÜSSEL UND WERTE AUSGEBEN (Alternative 2)" # //////////////////////////////
for key in woerter:
	print "%s: %s" % (key, woerter[key])	# key: value ausgeben

	

# Über WERTE-Liste Iterieren (Looping mit for-Schleife über values)	
for value in woerter.values():	# Iteration über WERTE-Liste des DICT (ungeordnet)
	print value					# s. auch # WERTE-Liste erzeugen
								# WERTE (values) ausgeben
	
# Über SCHLÜSSEL-Liste Iterieren (Looping mit for-Schleife über keys)
for key in woerter.keys():		# Iteration über SCHLÜSSEL (ungeordnet)
	print key					# s. auch # SCHLÜSSEL-Liste erzeugen
								# SCHLÜSSEL (keys) ausgeben
								
print u"# ÜBER LISTE DER SCHLÜSSEL-WERT-PAAR-TUPEL ITERIEREN" #//////////////////////////
for key, value in woerter.items():	# Iteration über SCHLÜSSEL-WERT-PAAR-Tupel (ungeordnet)
	print "%s = %s" % (key, value)
								# "key = value" ausgeben
								
print u"# SCHLÜSSEL Sortieren Und Geordnet Ausgeben" # //////////////////////////////////
keys = woerter.keys()	# SCHLÜSSEL-Liste in Variable speichern
print keys				# ausgeben
keys.sort()				# SCHLÜSSEL alphabetisch sortieren
print keys				# nochmal ausgeben und mit letzer Ausgabe vergleichen!
for key in keys:		# Iteration über sortierte SCHLÜSSEL-Liste
	print woerter[key]	# WERTE zu den SCHLÜSSELn ausgeben
						# ACHTUNG: die WERTE sind NICHT alphabetisch sortiert
						
print u"# WERTE Sortieren Und Geordnet Ausgeben" # //////////////////////////////////////
values = woerter.values()
print values
values.sort()
print values
for value in values:
	print value

print u"# Größe (Anzahl Einträge) des DICT ermitteln" # /////////////////////////////////	
len(woerter)

print len(woerter)		# Gib die Anzahl der Einträge im DICT aus
	

print "# GET A VALUE OF A SPECIFIED KEY" # ////////////////////////////////////////////////
# Den WERT zum KEY 'AAA' Ausgeben
# BEACHTE: Wenn die KEYS Zahlen sind, dann sind sie ohne Anführungszeichen anzugeben
#	z.B. so woerter.get(123, "Standardmeldung")
print "woerter.get('AAA') -->",
print woerter.get("AAA", "FEHLER: So ein KEY existiert NICHT, du dumme Hurre!!!")
print "woerter.get('E') -->",
print woerter.get("E", "FEHLER: KEY 'E' existiert NICHT, du dumme Hurre!!!\n")
print u"""Die DICT.get(KEY, MESSAGE)-Methode erlaubt uns eine Meldung
zu definierten, die ausgegeben werden kann, wenn der angegebene KEY im DICT nicht 
existiert.

"""


print "WERTE ALS STRING AUSGEBEN ////////////////////////////////////////////////////////\n"
print ', '.join(woerter), '\n'
# In den Anführungszeichen am Anfang kann man festlegen durch welche Zeichenfolge die
# KEYs von ein ander getrennt werden sollen.
# BEACHTE: Diese Operation ist nur bei KEYS vom Typ 'string' möglich
# 	bei KEYS vom Typ 'int' gibt's ein
#	'TypeError: sequence item 0: expected string, int found'


print u"# ALLE EINTRÄGE LÖSCHEN --> leeres DICT # /////////////////////////////////////"
woerter.clear()

print woerter			#
print len(woerter)		# sollte nach dem Löschen der Einträge nun Null sein!


print u"# DICT LÖSCHEN" # /////////////////////////////////////////////////////////////
del woerter
try:
	print woerter
except NameError:
	print u"Kann das DICT 'woerter' nicht ausgeben. Vermutlich wurde es bereits gelöscht!"



