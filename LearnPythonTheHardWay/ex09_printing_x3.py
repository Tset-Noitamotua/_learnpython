# -- coding: utf-8 --

# Here's some new strange stuff, remember type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"

# mit \n (newline) wird ein String in einer neuen Zeile ausgegeben
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Beide Anweisungen sind äquivalent
print "Here are the days:", days
print "Here are the days: %s" % days

# Die ersten beiden Anweisungen sind äquivalent, die dritte gibt raw data aus
print "Here are the months:", months
print "Here are the months: %s" % months
print "Here are the months: %r" % months

# Mit drei doppelten Ausführungszeichen kann man mehrzeilige Kommentare schreiben.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""