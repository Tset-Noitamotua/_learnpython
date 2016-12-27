# -*- coding: utf-8 -*-

# Klasse definieren
class Song(object):

	# wozu ist das???
	def __init__(self, shit):
		self.lyrics = shit
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"with pockets full of shells"])
						
wlad = Song(["Hallo ihr Fotzen",
			"Nur Titten ist nicht genug",
			"Ficken ist besser als ein Blowjob"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

wlad.sing_me_a_song()