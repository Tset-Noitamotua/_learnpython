# -*- coding: utf-8 -*-

number = 23
guess = int(raw_input('Enter an integer : '))

if guess == number:
    # new block starts here
    print 'Congratulation, you guessed it!'
    print 'But you do not win any prizes!'
    # end of new block

elif guess < number:
    # another block
    print 'No, it is a little higher than that.'
    # you can do whatever you want in a block ...
else:
    print 'No, it is a little lower than that.'
    # you must have guessed > number to reach here

print 'Done'
# this last statement is always executed
# after the if statement is executed.
