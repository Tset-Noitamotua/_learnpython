# -- coding: utf-8 --

# Das Modul argv aus Packet sys wird importiert
from sys import argv

# Die Variablen script und filename werden entpackt
# sie müssen dem Script als Argumente mitgegeben werden beim ausführen
# z.B so: python ex15_reading_files.py ex15_sample.txt
script, filename = argv

# Der Inhalt der Datei ex15_sample.txt, der
# dem Script beim Ausführen als Argument mitgegeben wurde,
# wird in die Variable txt geschrieben
txt = open(filename)

# Der Dateiname von ex15_sample.txt wird ausgegeben
print "Here's your file %r:" % filename
# Der Inhalt von txt (und damit der Inhalt von ex15_sample.txt) wird ausgegeben
print txt.read()
# Man könnte denken, dass man es auch so machen könnte ...
# print 'ex15_sample.txt'.read()    # aber das geht NICHT, weil
									# String kein Attribut read haben!!!
									# AttributeError: 'str' object has no attribute 'read'



print "Type the filename again:"
# neue Eingabeaufforderung, dadurch wird der Inhalt der Datei (deren Namen man eingibt)
# in die Variable file_again geschrieben
file_again = open(raw_input("> "))

# Der Inhalt von file_again wird ausgegeben
print file_again.read(), 'geht!!!'

# Inhalt von ex15_sample.txt wird in die Variable txt_again geschrieben
txt_again = open('ex15_sample.txt')
# Inhalt von txt_again wird ausgegeben
print txt_again.read(), 'das geht auch'