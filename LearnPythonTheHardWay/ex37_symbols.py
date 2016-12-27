# -*- coding: utf-8 -*-

# ACHTUNG: Diese Datei ist nicht lauffähig!!!

# Symbol Review with examples for each symbol / keyword

#:::::::::::::::::::::::::::::::::: KEYWORDS

"""________ import _________________________________________________________________

Import other modules into a Python script.
"""


"""________ from ___________________________________________________________________

For importing a specific variable, class or a function from a module.
"""
# from sys import xxx erlaubt die Verwendung des importierten Elements ohne Pfad
# Beispiel:
from sys import exit
# TODO Beispiel Verwendung von exit (ODER BESSER was anderes finden) einfügen:

# Bei dieser Import-Form müsste man sys.exit schreiben, um
# exit verwendet zu können
import sys

	
"""________ del ____________________________________________________________________

del ermöglicht das Löschen von Objekten.
"""
del x


"""________ while __________________________________________________________________

controlling the flow of the program, loop while the condition is true
"""
print "x wird auf 0 gesetzt!"
x = 0
print "Solange x < 10 ist, wird die Schleife wiederholt!"
while int(x) < 10:
	print "Die Schleilfe wird wiederholf, da x mit %s noch < 10 ist." % x
	x = raw_input("Gib eine ganze positive Zahl ein: ")
	#x = str(x)
	if not x.isdigit():
		print "Alter, du sollst eine GANZE POSITIVE Zahl eingeben - kein' Muell!!"
		x = 0
	else:
		print "Sehr gut! Du hast eine Zahl eingegeben und keine Scheise!"
	
print u"Mit x = %s ist die Bedingung x < 10 nicht mehr erfüllt.\n\
Schleife wird verlassen." % x


"""________ as _____________________________________________________________________

If we want to give a module a different alias
"""
#
# Beispiel:


"""________ elif ___________________________________________________________________

Stands for else if.If the first test evaluates to False,
then it continues with the next one. Analog zu switch(?)
"""
#
# Beipsiel:


"""________ global _________________________________________________________________

Access variables defined outside functions.
"""
#
# Beispiel:


"""________ with ___________________________________________________________________

???
"""
#
# Beispiel und Erklärung:


"""________ assert _________________________________________________________________

Used for debugging purposes.
"""
#
# Beipsiel:


"""________ else ___________________________________________________________________

Is optional. The statement after the else keyword is executed, 
unless the condition is True.	
"""
#
# Beispiel:


"""________ if _____________________________________________________________________

Used to determine, which statements are going to be executed.
"""
#
# Beispiel:


"""________ pass ___________________________________________________________________

Does nothing.
"""
#
# Beispiel:


"""________ yield __________________________________________________________________

Is used with generators.
"""
#
# Beispiel:


"""________ break __________________________________________________________________

Interrupt the (loop) cycle, if needed.
"""
#
# Beispiel:


"""________ except _________________________________________________________________

Catches the exception and executes codes.
"""
#
# Beispiel:


"""________ print __________________________________________________________________

Print to console
"""
#
# Beispiel:


"""________ class __________________________________________________________________

Used to create new user defined objects.
"""
#
# Beispiel:


"""________ exec ___________________________________________________________________

Executes Python code dynamically.
"""
#
# Beispiel:


"""________ in / not in ____________________________________________________________

Die Operatoren 'in' und 'not in' prüfen auf Zugehörigkeit zu einer Collection / Sammlung.
Eine Collection kann ein String(?), eine Liste, ein Tuple oder ein Dictionary sein(?).
'x in s' liefert True, wenn 'x' in der Collection 's' vorkommt - anderenfalls
liefert es False. 'x not in s' negiert den Wahrheitswert von 'x in s'. 

Ein Objekt gehört zur Collection, wenn die Collection eine Sequenz bwz. Folge von
Elementen darstellt, bei denen ein Element gleich dem Objekt ist. In Beipiel_1 ist es
der String 'Hallo' sowie die Teilstrings 'H', 'Ha', 'Hal' usw.  die im String s
vorkommen. Beachte, dass 'in / not in' Groß- und Kleinschreibung unterscheidet.

HINWEIS: Für weiter Informationen rufe help('in') im Python Interpreter auf!
"""
# Beispiel_1 | x, s = Strings
x = "Hallo"
s = "Hallo Welt!"
x in s									# >>> True
'Hallo' in s							# >>> True
'H' in s								# >>> True
'Hall' in s								# >>> True
' We' in s								# >>> True
# Alles True, weil alle Zeichenfolgen als Teil-String exakt in s vorkommen!

print "\nBeispiel 1 ::: x und s sind Strings:\n"
print "x = %r" % x, 'und',				# alle print zur Veranschaulichung in Konsole
print "s = %r" % s
print "x in s -->", x in s				# >>> True
print "'Hallo' in s -->", 'Hallo' in s	# >>> True

# Beispiel_2 | Unterscheidung zw. Groß- und Kleinschreibung 
x = "hallo"
x in s									# >>> False
x not in s								# >>> True
'hallo' in s							# >>> False

print u"\nBeispiel 2 ::: Unterscheidung zw. Groß- und Kleinschreibung\n"
print "x = %r" % x
print "'x in s' -->", x in s			# >>> False
print "'x not in s' -->", x not in s	# >>> True

# Beispiel_3 | x = Sring, s = Liste:
x = "Hallo"
s = ['Hallo', 'Welt', '!']
x in s									# >>> True
'Hallo' in s							# >>> Trre
'Hallo Welt!' in s						# >>> False

print "x = %r" % x
print "s = %r" % s
print "x in s -->", x in s				# >>> True
print "'Hallo' in s -->", 'Hallo' in s	# >>> True
print "'Hallo Welt!' in s -->",\

# Beispiel_4 | x, s = Listen
x = ["Hallo", "Welt", "!"]
s = ["Hallo", "Welt", "!"]
print "x = %r" % x
print "s = %r" % s
print "x in s -->", x in s				# False (ACHTUNG! False, obwohl Listen gleich.)
	# zum Vergleich ...
print "x is s -->", x is s				# False
	# ABER ...
print "x == s -->", x == s				# True !!! WTF?!!!
print "x[0] in s -->", x[0] in s		# True beim Vergleich eines einzelnen Index

# TODO: Weitere Beispiele mit Tuples und Dictionaries???


"""________ raise __________________________________________________________________

Create a user defined exception.
"""

# Beispeil_


"""________ continue _______________________________________________________________

Used to interrupt the current cycle, without jumping out of the whole cycle. 
New cycle will begin.
"""

# Beispiel_


"""________ finally ________________________________________________________________

Is always executed in the end. Used to clean up resources.
"""

# Beispiel_


"""________ return _________________________________________________________________

Exits the function and returns a value.
"""

# Beispiel_


"""________ def ____________________________________________________________________

Used to create a new user defined function.
"""

# Beispiel_


"""________ for ____________________________________________________________________

Iterate over items of a collection in order that they appear.
"""

# Beispiel_


"""________ lambda _________________________________________________________________

Creates a new anonymous function.
"""

# Beispiel_


"""________ try ____________________________________________________________________

Specifies exception handlers.
"""

# Beispiel_



#::::::::::::::::::: DATA TYPES or DATA STRUCTURE (containers)

"""________ True ___________________________________________________________________
"""


"""________ False __________________________________________________________________
"""


"""________ None ___________________________________________________________________
"""

# /////////////////////// UNVERÄNDERLICHE SEQUENZEN
# /////////////////////// [sequentielle Datentypen] ////////////////////////////////

# MERKE: Man unterscheidet in Großem und Ganzen veränderliche (mutable) und 
# unveränderliche (immutable) Datentypen. Die ersteren sind unhashable, d.h. von
# ihnen kann kein Hash erzeugt werden. Die unveränderlichen dagegen sind hashable!
# Grob gesagt kann ein Hash als ein Fingerabdruck eines Objekts angesehen werden.

# Beispiel (unhashable / mutable):
>>> a = ['a', 'b']						# Eine Liste ist
>>> hash(a)								# ein veränderliches Objekt,
Traceback (most recent call last):		# ...
  File "<stdin>", line 1, in <module>	# ...
TypeError: unhashable type: 'list'		# deshalb unhashable!

# Beispiel mit dict:
>>> b = {1: 'a', 2: 'b'}				# Ein Dictionary, 
>>> hash(b)								# das ja ebenfalls
Traceback (most recent call last):		# veränderlich ist,
  File "<stdin>", line 1, in <module>	# ...
TypeError: unhashable type: 'dict'		# ist auch NICHT hashable!

# Beispiel (hashable / immutable):
>>> c = ('a', 'b')						# Ein Tupel dagegen ist
>>> hash(c)								# UNVERÄNDERLICH und deshalb
555422938				 				# hashable

""" ''''''''''''''' string (Zeichenkette) '''''''''''''''''' """
#
# unveränderlicher Datentyp (immutable sequence type)
# Dieser Typ speichert Bytefolgen, also auch reine ASCII-Zeichenketten
#


""" ''''''''''''''' unicode (Zeichenkette) ''''''''''''''''' """
#
# unveränderlicher Datentyp (immutable sequence type)
# Dieser Datentyp speichert Zeichenfolgen in Unicode ab.


""" ''''''''''''''' xrange ''''''''''''''''''''''''''''''''' """
#
# unveränderlicher Datentyp (immutable sequence type)
# eingeschränkt: unterstützt nur indexing, iteration, und len() Funktion


""" ''''''''''''''' tuple (Tupel) '''''''''''''''''''''''''' """
#
# unveränderlicher Datentyp (immutable sequence type)
# In einem Tupel wird wie in einer Liste eine Folge belieber Instanzen
# gespeichert, aber diese kann dann während des weiteren Programmverlaufs
# nicht mehr verändert werden.
#


# ////////////////////// VERÄNDERLICHE SEQUENZEN ///////////////////////////////////

""" ''''''''''''''' list (Liste) ''''''''''''''''''''''''''' """
#
# veränderlicher Datentyp (mutable sequence type)
# geordneter Datentyp (d.h. die Items sind geordnet)
# In einer Liste kann eine Folge belieber Instanzen gespeichert werden.
# Eine Liste kann jederzeit während des Programmablaufs wieder geändert werden.


""" ''''''''''''''' dict (Dictionary) ''''''''''''''''''''''''' """
#
# veränderlicher Datentyp (mutable sequence type)
# UNgeordner Datentyp (d.h. die Item liegen ungeordnet vor)
# Auch MAPPING TYPE genannt, weil Items aus Schlüssel-Objekt-Paaren bestehen.
# Man sagt auch Schlüssel-Wert-Paare oder key/value pairs
# Die Schlüssel (Keys) dürfen nur aus unveränderlicher (immutable) Datentypen
# 	bestehen, es dürfen also z.B. keine Listen und keine Dictionaries sein.
# Verwendet man dennoch z.B. eine Liste als Key, bekommt man die Fehlermeldung:
# 	TypeError: list objects are unhashable 


""" ''''''''''''''' bytearray (???) ''''''''''''''''''''''''''' """
# ???
# veränderlicher Datentyp (mutable sequence type)


# ////////////////////// COLLECTIONS ///////////////////////////////////////////////

""" ''''''''''''''' set ''''''''''''''''''''''''''''''''''''''' """
#
# veränderlicher Datentyp (mutable sequence type) ABER ACHTUNG:
# UNgeordneter Datentyp
# Sie sind zwar selbst veränderlich, dürfen aber keine veränderlichen Elemente
# wie Listen enthalten, sont --> TypeError: unhashable type: 'list' 
# A set object is an unordered collection of distinct hashable objects.
# eingeschränkt:  do NOT support indexing, slicing, or other sequence-like behavior.


""" ''''''''''''''' frozenset '''''''''''''''''''''''''''''' """
#
# unveränderlicher Datentyp (immutable sequence type)
#




""" ''''''''''''''' collections ''''''''''''''''''''''''''''''' """


#------------------- ZAHLEN oder nummerische Datentypen

""" '''' integer (Ganzzahl) '''' """


""" '''' float (Fleißkommazahl) '''' """


#::::::::::::::::::::::::::: STRING ESCAPE SEQUENCES

''' '''''''''''''''''''''''''''' \\ '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \' '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \" '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \a '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \b '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \f '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \n	'''''''''''''''''''''''''''''' '''
# Newline

''' '''''''''''''''''''''''''''' \r '''''''''''''''''''''''''''''' '''
#

''' '''''''''''''''''''''''''''' \t '''''''''''''''''''''''''''''' '''
#  TAB-Vorschub


''' '''''''''''''''''''''''''''' \v '''''''''''''''''''''''''''''' '''
#



# ::::::::::::::::::::::::::: STRING FORMATS

''' '''''''''''''''''''''''''''' %d '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %i '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %o '''''''''''''''''''''''''''''' '''
#
	

''' '''''''''''''''''''''''''''' %u '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %x '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %X '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %e '''''''''''''''''''''''''''''' '''
#
	
	
''' '''''''''''''''''''''''''''' %E '''''''''''''''''''''''''''''' '''
#	
	
	
''' '''''''''''''''''''''''''''' %f '''''''''''''''''''''''''''''' '''
#	
	
	
''' '''''''''''''''''''''''''''' %F '''''''''''''''''''''''''''''' '''
#	
	
	
''' '''''''''''''''''''''''''''' %g '''''''''''''''''''''''''''''' '''
#	
	
	
''' '''''''''''''''''''''''''''' %G '''''''''''''''''''''''''''''' '''
#	

	
''' '''''''''''''''''''''''''''' %c '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %r '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %s '''''''''''''''''''''''''''''' '''
#


''' '''''''''''''''''''''''''''' %% '''''''''''''''''''''''''''''' '''
#

""" """

#:::::::::::::::::::::::::::::: OPERATORS

""" '''''''''''''''''''''''''''' boolean  '''''''''''''''''''''''' """
#		and		or		not

### and
# All conditions in a boolean expression must be met.
#
# Beispiel:
print "Setze x auf False"
x = True and False
print "Gebe x aus und erhalte x ist %s" % x	
y = 1			# sollte False ausgeben

if x == False and y == 1:
	print 'OK'
else:
	print 'Fehler!'


### or
# At least one condition must be met.
#
# Beispiel:


### not		and not		or not		not(... and ...)		not(... or ...)
# Negates a boolean value.
#
# Beispiel_1:
x = not True
print x
# Beispiel_2:

# Beispiel_3:


''' '''''''''''''''''''''''''''' counting '''''''''''''''''''''''' '''
#		+		-		*		**		/		//		%
# + (plus)
# - (minus)
# ...


''' '''''''''''''''''''''''''''' shortcuts ''''''''''''''''''''''' '''
#		+=		-=		*=		**=		/=		//=		%=


''' '''''''''''''''''''''''''''' comparing ''''''''''''''''''''''' '''
#		<		>		<=		>=		==		!=		<>		is / is not

### is / is not
# Tests for object identity.
#
# Beispiel_1:
a = 1
b = 
a is b		# >>> True

# Beispiel_2:

# TODO: Besseres Beispiel???


''' '''''''''''''''''''''''''''' grouping '''''''''''''''''''''''' '''
#		()		[]		{}


''' '''''''''''''''''''''''''''' misc '''''''''''''''''''''''''''' '''
#		=		.		:		;		'		










