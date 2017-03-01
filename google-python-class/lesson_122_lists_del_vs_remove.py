# -*- coding: utf-8 -*-
# https://www.dotnetperls.com/del-python
# Life is short, use Python!

import time
import sys
import progressbar



# NOTE: Del is a clear and faster way to remove elements from a list. Often we can use it instead of the remove() method which is much slower because it involves a search.

# NOTE: The greater range_count is the greater the difference in time "del"
#       and "remove()" take to run.
#       On my machine a range_count of 2000000 lets "del" take ~10 s
#                                          and "remove()" take ~15 s
range_count = 10000

# Version 1: use del on an index.
# for i in range(range_count):
#     values = [x for x in range(100)]
#     del values[95]
#     if len(values) != 99: break
#
# Version 2: use list remove method on a value.
# for i in range(range_count):
#     values = [x for x in range(100)]
#     values.remove(95)
#     if len(values) != 99: break


# ====================================== Progressbar2
# https://pypi.python.org/pypi/progressbar2/3.12.0

# bar = progressbar.ProgressBar(redirect_stdout=True)
# for i in range(range_count):
#     print('Some text', i)
#     time.sleep(0.1)
#     bar.update(i)

print("\nProgressbar -  unknown lenght")
start_timer = time.time()
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
for i in range(range_count):
    values = [x for x in range(100)]
    del values[95]
    if len(values) != 99: break
    bar.update(i)
stop_timer = time.time()
print("\ndel - Done! Duration:", stop_timer - start_timer, 's\n')

print("\nProgressbar - Wrapping an iterable")
start_timer = time.time()
bar = progressbar.ProgressBar()
for i in bar(range(range_count)):
    values = [x for x in range(100)]
    del values[95]
    if len(values) != 99: break
stop_timer = time.time()
print("del - Done! Duration:", stop_timer - start_timer, 's\n')

start_timer = time.time()
bar = progressbar.ProgressBar()
for i in bar(range(range_count)):
    values = [x for x in range(100)]
    values.remove(95)
    if len(values) != 99: break
stop_timer = time.time()
print("remove() - Done! Duration:", stop_timer - start_timer, 's\n')

print("\nProgressbar -  Context wrapper")
start_timer = time.time()
with progressbar.ProgressBar(max_value=range_count) as bar:
    for i in range(range_count):
        values = [x for x in range(100)]
        del values[95]
        if len(values) != 99: break
        bar.update(i)
stop_timer = time.time()
print("del - Done! Duration:", stop_timer - start_timer, 's\n')

start_timer = time.time()
with progressbar.ProgressBar(max_value=range_count) as bar:
    for i in range(range_count):
        values = [x for x in range(100)]
        values.remove(95)
        if len(values) != 99: break
        bar.update(i)
stop_timer = time.time()
print("remove() - Done! Duration:", stop_timer - start_timer, 's\n')


# ====================================== FraggaMuffin Bar
# http://stackoverflow.com/a/21326436/4445175
class ProgressBar(object):
    DEFAULT_BAR_LENGTH = 60
    DEFAULT_CHAR_ON  = '='
    DEFAULT_CHAR_OFF = ' '

    def __init__(self, end, start=0):
        self.end    = end
        self.start  = start
        self._barLength = self.__class__.DEFAULT_BAR_LENGTH

        self.setLevel(self.start)
        self._plotted = False

    def setLevel(self, level):
        self._level = level
        if level < self.start:  self._level = self.start
        if level > self.end:    self._level = self.end

        self._ratio = float(self._level - self.start) / float(self.end - self.start)
        self._levelChars = int(self._ratio * self._barLength)

    def plotProgress(self):
        sys.stdout.write("\r  %3i%% [%s%s]" %(
            int(self._ratio * 100.0),
            self.__class__.DEFAULT_CHAR_ON  * int(self._levelChars),
            self.__class__.DEFAULT_CHAR_OFF * int(self._barLength - self._levelChars),
        ))
        sys.stdout.flush()
        self._plotted = True

    def setAndPlot(self, level):
        oldChars = self._levelChars
        self.setLevel(level)
        if (not self._plotted) or (oldChars != self._levelChars):
            self.plotProgress()

    def __add__(self, other):
        assert type(other) in [float, int], "can only add a number"
        self.setAndPlot(self._level + other)
        return self
    def __sub__(self, other):
        return self.__add__(-other)
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__add__(-other)

    def __del__(self):
        sys.stdout.write("\n")

if __name__ == "__main__":
    import time
    print("FraggaMuffin Bar")

    pb = ProgressBar(range_count)

    start = time.time()
    #pb.plotProgress()
    for i in range(range_count):
        pb += 1
        #pb.setAndPlot(i + 1)
        # Version 1: use del on an index.
        values = [x for x in range(100)]
        del values[95]
        if len(values) != 99: break
    del pb
    stop_1 = time.time()
    print("del - Done! Duration:", stop_1 - start, 's')

