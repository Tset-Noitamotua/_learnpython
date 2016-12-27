# -*- coding: utf-8 -*-

# Exersice 30 - else and if

def break_words(eingabe):
	"""Diese Funktion bricht einen Satz in seine einzelnen
Bestandteile (Wörter) auf."""
	woerter = eingabe.split(' ')
	return woerter
	
def try_again():
	again = raw_input("Want to try again? (type yes or no) ")
	if again == "yes" or again == "y":
		print "\nOk, let's try it again!\n"
		execfile('ex31_decisions.py')
	elif again == "no" or again == "n":
		print "Hast schiss bekommen? Na gut, cioa!"
	else:
		print "%s?!!! Dann geh' und FICK dich!!!" % again
	

print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. ..."
	print "4. ..."
	print "5. ..."
	
	bear = raw_input("> ")
		
	if bear == "1":
		print "The bear eats your face off. Good job!\n"
		try_again()
	elif bear == "2":
		print "The bear eats your legs off. Good job!\n"
		try_again()
	elif bear >= '3':
		print u"Du hast %s gewählt." % bear
		try_again()
	else:
		eingabe = break_words(bear)
		blacklist = ['ficken', 'bumsen', 'blasen']
		print eingabe
		print u"Du hast diese Wörter eingegeben:\n"
		for item in eingabe:
			print item
		try_again()
		
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
		try_again()
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		try_again()
else:
	print "You stumble around and fall on a knife and die. Good job!"
	try_again()
		
	