# -*- coding: utf-8 -*-

# create a mapping of state to abbreviation
# WLAD: dict "states" wird erzeugt
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

# create a basic set of states an some cities in them
# WLAD: dict "cities" wird erzeugt
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

# add some more cities
# WLAD: NY - New York und OR - Portland werden zum dict "cities" hinzugefügt
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10 				# WLAD: Trennlinie
# WLAD: Aus dem dict "cities" werden die Werte zu den Keys NY und OR augegeben
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
# WLAD: Aus dem dict "states" werden die Werte zu den Keys Michigan u. Florida ausgegeb.
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
# WLAD: Hier werden die Dictionaries in einander verschachtelt
# cities[states['Michiga']] = cities['MI'] = 'Detroit'
# cities[states['Florida']] = cities['FL'] = 'Jacksonville'
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# WLAD: Für jedes Elementen-Paar im dict gibt eine Zeile aus, die den Key ...
# ... und den dazugehörigen Wert enthält.
# ... Der Key (z.B 'Florida') wird dabei in der Variable state zwischengespeichert.
# ... Der Wert zum Key (z.B. 'FL' bei Florida) wird in abbrev zwischengespeichert.
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)
	
# print every city in state
print '-' * 10
# WLAD: Das gleiche Spiel wie vorhin - jetzt mit dem dict "cities".
# ... Für jedes Paar im dict werden Key mit zugehörigem Wert in einer Zeile ausgegeben.
# ... Keys werden in abbrev und Werte in city zwischengespeichert.
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
print '-' * 10
# WLAD: Hier wird über das dict states iteriert.
# ... Je Zeile wird ein Key mit zugehörigem Wert aus dem dict states ausgegeben.
# ... UND zusätzlich wird je Zeile ein Key aus dem dict cities ausgegeben.
# ... Key aus cities ergibt sich dabei aus cities[abbrev].
# ... In abbrev werden die Werte der Keys aus dem dict states zwischengelagert.
# ... diese Werte entsprechen den Keys im dict cities.
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safely get an abbreviation by state that might not be there
# WLAD: Den Wert zum Key 'Texas' aus dem dict states aufrufen.
# ... Dieser Wert existiert aber gar nicht und der Key auch nicht
state = states.get('Texas')
state2 = states.get('Florida')
print state # liefert --> None (weil es keine Key 'Texas' im dict states gibt)
print not state # --> True

# WLAD: da state None liefert, ist die Bedingung "not state" True.
# ... Deshalb wird "Sorry, no Texas." ausgegeben.
if not state:
	print "Sorry, no Texas."

# get a city with a default value
# WLAD: Wird versucht ein Key aufzurufen, der im dict nicht vorhanden ist,
# ... kann auf diese Weise ein Standardwert dafür definiert werden.
city = cities.get('NOT_EXISTING_KEY', 'Does not exist (als Standardwert)')
print "The city for the state 'NOT_EXISTING_KEY' is: %s" % city
print city
city2 = cities.get('NICHT_VORHANDENE_STADT', 'Standardwert: DIESE STADT GIBT\
	ES NICHT! WIXA!')
print city2