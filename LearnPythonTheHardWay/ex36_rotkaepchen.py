# -*- coding: utf-8 -*-
from sys import exit
# Kleines Text-Adventure auf der Basis des Märchens "Rotkäppchen" der Brüder Grimm

def ende(grund):
	if grund == 0:
		print "\tEs dauerte zu lange. Die Oma starb! ENDE der Geschichte.\n"
		exit(0)
	elif grund == 1:
		print u"\tDer Wolf wurde sauer und fraß alle im Märchen auf! ENDE der Geschichte."
		exit(0)
	else:
		print "ENDE!"
		exit(0)
		

def wald():
	print u"""
	Die Grossmutter aber wohnte draussen im Wald, eine halbe Stunde
	vom Dorf. Wie nun Rotkäppchen in den Wald kam, begegnete ihm der Wolf.
	Rotkäppchen aber wusste nicht, was das für ein böses Tier war,
	und fürchtete sich nicht vor ihm. "Guten Tag, Rotkäppchen!" sprach er.
	"""
	print u"""	/////// Was soll Rotkäppchen ihm antworten? Wähle ...\n 
	(1) Schönen Dank, Wolf! Guten Tag zurück!
	(2) Quatsch mich nicht dumm von der Seite an, du FICKER!
	"""
	
	while True:
		weiter = raw_input('\t--> ')
		
		if '1' in weiter:
			print u"""\n\tRotkäppchen: "Schönen Dank, Wolf!"
	Wolf: "Wohin des Weges so früh, Rotkäppchen?"
	Rotkäppchen: "Zur Grossmutter."
	Wolf: "Was trägst du unter der Schürze?"
	"""	
			weiter = raw_input("\tRotkaeppchen: ")
			if 'wein' in weiter or 'kuchen' in weiter:
				print u'\t"Wein und Kuchen." antwortete Rotkäppchen.'
			else:
				print u'"\tKein Höschen!" sagte sie und grinste dreckig.'
		elif '2' in weiter:
			print '\t\n"Quatsch mich nicht dumm an, du FICKERasdf!" sagte sie mit erregter Stimme.'
			ende(1)

def start():
	print u"""
	Es war einmal ein kleines süsses Mädchen, das hatte jedermann lieb,
	der sie nur ansah, am allerliebsten aber ihre Grossmutter,
	die wusste gar nicht, was sie alles dem Kinde geben sollte.
	
	Einmal schenkte sie ihm ein Käppchen von rotem Samt, und weil ihm das
	so wohl stand, und es nichts anders mehr tragen wollte,
	hiess es nur das Rotkäppchen.
	
	Eines Tages sprach seine Mutter zu ihm: "Komm, Rotkäppchen, da hast du
	ein Stück Kuchen und eine Flasche Wein, bring das der Grossmutter hinaus;
	sie ist krank und schwach und wird sich daran laben.
	Mach dich auf, bevor es heiss wird, und wenn du hinauskommst, so geh
	hübsch sittsam und lauf nicht vom Wege ab, sonst fällst du und zerbrichst
	das Glas, und die Grossmutter hat nichts. Und wenn du in ihre Stube
	kommst, so vergiss nicht guten Morgen zu sagen und guck nicht erst in
	allen Ecken herum!" \n"""
	
	while True:
		weiter = raw_input("""\t/////// Was soll Rotkaeppchen ihrer Mutter antworten? Waehle ...\n
	(1) OK!
	(2) Was hast du gesagt, Mama?
	(3) Ne, hab keine Lust, soll die alte doch verrecken!
	oder schreib eine eigene Antwort!\n\t--> """)
		
		if '1' in weiter:
			print u"""
	OK. Ich will schon alles richtig machen," sagte Rotkäppchen zur Mutter,
	und gab ihr die Hand darauf.
	"""
			wald()
		elif '2' in weiter:
			print "\tIch sagte, du sollst dir edlich einen Stecher finden, \
Kinder kriegen und ausziehen!"
			ende(0)
		elif '3' in weiter:
			ende(0)
		elif 'asdf' in weiter:
			ende(2)
		else:
			print "\tWas meinst du damit?"
			
start()