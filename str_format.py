# -*- coding: utf-8 -*-

age = 20
name = 'wlad'

print '{0} was {1} years old when he wrote this book'.format(name, age)
print 'why is {0} playing with that python?'.format(name)

print name + ' is ' + str(age) + ' years old.'

# decimal (.) precision of 3 for float '0.333'
print '{0:.3f}'.format(1.0/3)

# fill with underscores (_) with the text centered
# (^) to 11 width '__hello__'
print '{0:_^11}'.format('hello')
print '{0:_^21}'.format('hello')
print '{0:_^31}'.format('hello')
print '{0:_^41}'.format('hello')
print '{0:+^51}'.format('hello')

# FUCK: Wie kriegt man Umlaute mit .format korrekt ausgegeben???????
print '{0:-^61}'.format('BEISPIEL ÜBERSCHRIFT')
print "müschi"
print u"müschi"

# keyword-based 'Wlad wrote a Test Automation Book'
print '{name} wrote {book}'.format(name='Wlad',
                                  book='Test Automation Bibel')

print 'a'
print 'b'

print 'a',
print 'b'

print 'das ist die erste zeile\ndas ist die zweite zeile'
print 'das ist die erste zeile \
       und das bleibt auch in der ersten zeile'

print r'Newlines a indicated by \n'
print "Hallo Git Hub!"


