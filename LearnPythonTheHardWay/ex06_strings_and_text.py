# -- coding: utf-8 --

# x wird ein Format-String zugewiesen
x = "There are %d types of people." % 10

# binary und do_not wird jeweils ein String zugewiesen
binary = "binary"
do_not = "don´t"

# y wird ein Format-String zugewiesen, in den zwei Strings eingefügt werden
y = "Those who know %s and those who %s." % (binary, do_not)

# x und y werden ausgegeben
print x
print y

# String "I said ..." wird ausgegeben, wobei x als raw data integriert wird
print "I said: %r." % x
# das gleich wie bei x nur mit y
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn´t that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
