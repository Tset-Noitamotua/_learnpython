# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print ten_things

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
print stuff
more_stuff = ["Day", "Night", "Song", "Frisbbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff
print stuff[1]
print stuff[2]
print stuff[0]
print stuff[-1]			# whoa! fancy
print stuff.pop()
print ' | '.join(stuff)	# what? cool!
print '#'.join(stuff[3:7])













