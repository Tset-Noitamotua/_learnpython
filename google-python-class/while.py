# -*- coding: utf-8 -*-

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer: '))

    if guess == number:
        print 'congratulation, you guessed it.'
        # this causes the while loop zu stop
        running = False
    elif guess < number:
        print 'No, it is a little higher than that.'
    else:
        print 'No, it is a little lower than that.'
else: 'The while loop is over!'
    # do anything else you want to do here
print 'Done!'

