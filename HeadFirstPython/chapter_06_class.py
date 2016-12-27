"""
Module doc string ...
foo bar
bang
"""

def sanitize(time_string):
    """
    function doc string"""

    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs

def get_coach_data(filename):
    """
    function doc string"""
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(Athlete(templ.pop(0), templ.pop(0), templ))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)



class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name  = a_name
        self.dob   = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])



james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
