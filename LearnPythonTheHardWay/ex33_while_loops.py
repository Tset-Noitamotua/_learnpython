# -*- coding: utf-8 -*-

def while_loop(loops, increment):
	# i und eine leere Liste namens "numbers" werden definiert
	i = 0
	numbers = []
	# solange i kleiner 6 ist mach ...
	while i < loops:
		# ... den Wert von i ausgeben
		print "At the top i is %d" % i
		# ... den Wert von i der Liste numbers hinzufügen
		numbers.append(i)
		# ... den Wert von i um 1 erhöhen
		i += increment
		# ... die Liste ausgeben
		print "numbers now:", numbers
		# ... den Wert von i erneut (also NACH der Erhöhung) ausgeben
		print "At the bottom i is %d" % i
		# HIER IST DAS ENDE DER WHILE-SCHLEIFE!!!!!
		
	print "\nThe numbers: "
	# Jedes Element aus der Liste numbers wird in einer neuen Zeile ausgegeben
	for num in numbers:
		print num,
	print '\n'
	

# Hier die gleiche Funktion als for-Schleife
def for_loop(start, end, steps):
	numbers = []
	for x in range(start,end, steps):
		print "At the top x is %d" % x
		numbers.append(x)
		print "numbers now:", numbers
		print "At the bottom x is %d" % x
	
	print "\nThe numbers: "
	for num in numbers:
		print num,
	print '\n'


# Beiden Funktionen werden nacheinander aufgerufen		
while_loop(6, 1)
# Funktion wird mit den Argument start = 0, end = 6 und steps = 1 aufgerufen
# d.h. die Schleife geht von 0 bis 6 in einser Schritten
# steps = 1 entspricht increment = 1, ist also
# das gleiche wie i += 1 oder i = i + 1 in der while_loop-Funktion	
for_loop(0,6,1)