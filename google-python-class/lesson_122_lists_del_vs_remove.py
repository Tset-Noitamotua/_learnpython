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


# NOTE: "Del"" is a clear and faster way to remove elements from a list. Often we can use it instead of the remove() method which is much slower because it involves a search.

# NOTE: The greater range_count value is the greater the difference in time between
#       "del" and "remove()" execution.
#       On my machine a range_count of 2000000 lets "del" take ~10 s
#                                          and "remove()" take ~15 s
range_count = 500000


# without progressbar
# Version 1: use "del"" on an index.
timer_start = time.time()
for i in range(range_count):
    del_from_list()
timer_stop = time.time()
print('del - done in %i s' %(timer_stop - timer_start))

# Version 2: use list's "remove" method on a value.
timer_start = time.time()
for i in range(range_count):
    remove_from_list()
timer_stop = time.time()
print('remove() - done in %i s' %(timer_stop - timer_start))



# same as above but with progressbar in concole
# NOTE: runs a bit slower because of progressbar overhead
# Version 1: use del on an index.
widgets = [progressbar.Percentage(), progressbar.Bar(), progressbar.Timer()]
bar = progressbar.ProgressBar(widgets=widgets, max_value=range_count).start()
timer_start = time.time()
for i in range(range_count):
    values = [x for x in range(100)]
    del values[95]
    bar.update(i)
bar.finish()
timer_stop = time.time()
print('\ndel - done in %i s' %(timer_stop - timer_start))

# Version 2: use list remove method on a value.
widgets = [progressbar.Percentage(), progressbar.Bar(), progressbar.Timer()]
bar = progressbar.ProgressBar(widgets=widgets, max_value=range_count).start()
timer_start = time.time()
for i in range(range_count):
    values = [x for x in range(100)]
    values.remove(95)
    bar.update(i)
bar.finish()
timer_stop = time.time()
print('\nremove() - done in %i s' %(timer_stop - timer_start))
