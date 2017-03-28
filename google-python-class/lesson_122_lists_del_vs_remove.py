# -*- coding: utf-8 -*-
# https://www.dotnetperls.com/del-python
# Life is short, use Python!

import time
# import sys
import progressbar      # pip install progressbar2



def del_from_list():
    values = [x for x in range(100)]
    del values[95]


def remove_from_list():
    values = [x for x in range(100)]
    values.remove(95)


# NOTE: "Del"" is a clear and faster way to remove elements from a list.
# Often we can use it instead of the remove() method which is much slower 
# because it involves a search.

# NOTE: The greater value of N is the greater the difference in time 
#       between "del" and "remove()" execution.
#       On my machine N = 2000000 --> "del" takes ~10 s
#                                 --> "remove()" takes ~15 s
N = 2000000

# # Original code without progressbar.
# # Undo comments to compare timing with progressbar-version of code below
# #
# # Version 1: use "del"" on an index.
# timer_start = time.time()
# for i in range(N):
#     del_from_list()
# timer_stop = time.time()
# print('del - done in %i s' %(timer_stop - timer_start))

# # Version 2: use list's "remove" method on a value.
# timer_start = time.time()
# for i in range(N):
#     remove_from_list()
# timer_stop = time.time()
# print('remove() - done in %i s' %(timer_stop - timer_start))



# Code with progressbar output in concole
# NOTE: runs a bit slower because of progressbar overhead
#
# Version 1: use del on an index.
widgets = [progressbar.Percentage(), progressbar.Bar(), progressbar.Timer()]
bar = progressbar.ProgressBar(widgets=widgets, max_value=N).start()
timer_start = time.time()
for i in range(N):
    values = [x for x in range(100)]
    del values[95]
    if i % 10000 == 0:  # Only updates once every 10.000 values
        bar.update(i)   # thus progressbar creates less overhead
bar.finish()
timer_stop = time.time()
print('del - done in %i s\n' %(timer_stop - timer_start))

# Version 2: use list remove method on a value.
widgets = [progressbar.Percentage(), progressbar.Bar(), progressbar.Timer()]
bar = progressbar.ProgressBar(widgets=widgets, max_value=N).start()
timer_start = time.time()
for i in range(N):
    values = [x for x in range(100)]
    values.remove(95)
    if i % 10000 == 0:
        bar.update(i)
bar.finish()
timer_stop = time.time()
print('remove() - done in %i s' %(timer_stop - timer_start))
