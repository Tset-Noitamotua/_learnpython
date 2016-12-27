# -*- coding: utf-8 -*-

the_count = [11, 22, 33, 44, 55]
fruits = ['apples', 'oranges', 'pears', 'apricots', 'bananas']
p_fruits = []	# Früchte, die den Buchstaben p enthalten
v_fruits = []	# Früchste, die mit einem Vokal (s. vokale) anfangen
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
vokale = ('a', 'e', 'i', 'o', 'u')

print "\nThese are all fruits we have:",

for fruit in fruits[0:-2]:
	print str.capitalize(fruit) + ',',
print str.capitalize(fruits[-2]),
print "and " + str.capitalize(fruits[-1]) + '\n'

# Meine eigene Funktionen (Wlad) ################################################
# Hier wird meine 1. Funktion definiert
def fruits_with_p():
	"""Diese Funktion printet alle Früchte, die den Buchstaben p enthalten."""

	for fruit in fruits:
		if 'p' in fruit:
			p_fruits.append(fruit)
	print 'These words contain at least one letter "p":\n'
	for fruit in p_fruits:
		print str.capitalize(fruit)
	print '\n'


# Hier wird meine 2. Funktion definiert	
def beginnt_mit_vokal():
	"""Diese Funktion printet alle Früchte, die mit einem Vokal anfange."""
	for fruit in fruits:
		# asdf
		if fruit.startswith(vokale):
			v_fruits.append(fruit)
	print "And this one start with a vowel:\n"
	for fruit in v_fruits:
		print str.capitalize(fruit)
	print '\n'
	

# Hier werden die beiden oben definiert Funktionen aufgerufen	
fruits_with_p()
beginnt_mit_vokal()
############################### ENDE MEINER FUNKTIONEN ##########################
	
# this first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know whats's in it
for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	
# Wlad: oder nimm die Werte aus der liste "the_count" und schreib sie
# in die Liste "elements"
for i in the_count:
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
	
print elements	# printe zur Überprüfung die Liste

# now we can print them out too
for i in elements:
	print "Element was: %d" % i















 