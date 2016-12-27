# -- coding: utf-8 --

# mit \t wird ein Tabulator (Zeilenvorschub) eingefügt
tabby_cat = "\tI'm tabbed in."

# Ausgabe wird auf zwei Zeilen verteilt
persian_cat = "I'm split\non a line."

# Hier wird zweimal ein Backslash escaped
backslash_cat ="I'm \\ a \\ cat."

# Die drei Zeilen, die mit \t* anfangen sind um ein Tab eingerückt
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Jede String Variable wird mit eigener print Anweisung ausgegeben
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# nächsten zwei Zeilen sind äquivalent zu den letzten vier print Anweisungen
for i in [tabby_cat, persian_cat, backslash_cat, fat_cat]:
		print '%s' % i
		
# Das gibt GENAU das gleich, wie die beiden Varianten drüber!!!		
print '%s\n%s\n%s\n%s' % (tabby_cat, persian_cat, backslash_cat, fat_cat)

a = """
ESCAPE SEQUENCES

Escape	What it does.
\		Backslash (\)
'		Single-quote (')
"		Double-quote (")
a		ASCII bell (BEL)
b		ASCII backspace (BS)
f		ASCII formfeed (FF)
n		ASCII linefeed (LF)
N{name}		Character named name in the Unicode database (Unicode only)
r 		ASCII Carriage Return (CR)
t 		ASCII Horizontal Tab (TAB)
v 		ASCII vertical tab (VT)
ooo		Character with octal value ooo
"""
print a

