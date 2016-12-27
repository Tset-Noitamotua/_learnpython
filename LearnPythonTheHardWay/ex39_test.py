# -*- coding: utf-8 -*-

import ex39_hashmap

# The tests that it will work

jazz = ex39_hashmap.new()
ex39_hashmap.set(jazz, 'Miles Davis', 'Flamenco Sketches')
# confirm set will replace previous one
ex39_hashmap.set(jazz, 'Miles Davis', 'Kind of Blue')
ex39_hashmap.set(jazz, 'Duke Ellington', 'Beginning To See The Light')
ex39_hashmap.set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- List Test ----"
ex39_hashmap.list(jazz)

print "---- Get Test ----"
print ex39_hashmap.get(jazz, 'Miles Davis')
print ex39_hashmap.get(jazz, 'Duke Ellington')
print ex39_hashmap.get(jazz, 'Billy Strayhorn')

print "---- Delete Test ----"
print "** Goodbye Miles"
ex39_hashmap.delete(jazz, "Miles Davis")
ex39_hashmap.list(jazz)

print "** Goodbye Duke"
ex39_hashmap.delete(jazz, "Duke Ellington")
ex39_hashmap.list(jazz)

print "** Goodbye Billy"
ex39_hashmap.delete(jazz, "Billy Strayhorn")
ex39_hashmap.list(jazz)

print "** Goodbye Pork Pie Hat"
ex39_hashmap.delete(jazz, "Charles Mingus")