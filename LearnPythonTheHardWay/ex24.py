# -*- coding: utf-8 -*-

print "Let's pratice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------------"
print poem
print "------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Funktion wird mit dem Argument "started" definiert
# In der Funktion werden den 6 Variablen jelly_beans, jars, crats,
# trucks, ships und ships2 diverse Werte zugewiesen
# Die Funktion gibt die Werte dieser Variablen mit Hilfe von return zurück.
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	trucks = crates / 10
	ships = trucks / 2
	ships2 = 1
	return jelly_beans, jars, crates, trucks, ships, ships2 # 6 return-Werte!!!
	# 6 Werte werden zurück gegeben
	# in exakt dieser Reihenfolge

# Der Variable start_point wird der Wert 10000 zugewiesen
start_point = 10000

## Hier werden die Werte, die die Funktion secret_formula über return zurück gibt,
# neuen Variablen zugewiesen.
## Die Anzahl der Variablen muss der Anzahl der return-Werte (hier 6) entsprechen,
# sonst kommt es zu Fehlern:
# Mehr Variablen als return-Werte (z.B. 7):
#  		ValueError: need more than 6 values to unpack
#  		Warum? Weil es mehr Variablen gibt als Werte, die man ihnen zuweisen könnte
# Weniger Variablen als return-Werte (z.B 5):
#		ValueError: too many values to unpack
#  		Warum? Weil es mehr Werte gibt als Variablen, in die man diese Werte
#		reinstecken könnte.
## Die Reihenfolge der Variablen ist zu BEACHTEN, denn genau in dieser Reihenfolge
# erfolgt die Zuweisung der return-Werte zu den Variablen:
# beeren = jelly_beans, dosen = jars, kisten = crates, ... , frachter = ships 2

# KURZ: return-Werte der Funktion werden den 6 Variablen zugewiesen.
beeren, dosen, kisten, lkw, schiffe, frachter = \
secret_formula(start_point);

print "With a starting point of: %d" % start_point
# Hier wird eine Auswahl einzelner return-Werte aus der Funktion secret_formula ausgegeben
# indem sie in Klammern als Argumente an den Format String übergeben werden.
# Deshalb müssen hier auch NICHT ALLE 6 Werte ausgegeben werden. Es dürfen weniger sein.
# Und man kann die Reihenfolge, in der sie ausgegen werden, selbst steuern(?)
print "We'd have %d BEEREN, %d DOSEN, %d KISTEN and %d LKWs." % (beeren, dosen, kisten, lkw)

start_point = start_point / 1

print "\nWe can also do that this way:\n"
# Bei dieser Variante MÜSSEN genauso viele Werte ausgegeben werden,
# wie die Funktion zurück gibt (also 6), ansonsten gibt es folgenden Fehler:
# Weniger als 6 Platzhalter (%d):
#		TypeError: not all arguments converted during string formatting
# Mehr als 6 Platzhalter:
#		TypeError: not enough arguments for format string
# Die Reihenfolge der Ausgabe entspricht hier der Rückgabe-Reihenfolge
# der Funktion (s. return Zeile 32) und kann nicht ohne weiteres selbst gesteuert werden(?).

# Mit dem Backslash \ kann man lange Zeilen umbrechen. Allerding darf nach dem \
# dann nichts stehen (auch kein Kommentar)
print "We'd have %d BEEREN, %d DOSEN, %d KISTEN und %d LKWs \
und %d SCHIFFE UND %d FRACHTER." % secret_formula(start_point)		
















