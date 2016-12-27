def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

def get_coach_data(filename):
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

    def add_time(self, time):
        self.times.append(time)

    def add_times(self, time_list):
        self.times.extend(time_list)



james = get_coach_data('james2.txt')
print(james.name + "'s 1. fastest times are: " + str(james.top3()))
james.add_time('2:00')
print(james.name + "'s 2. fastest times are: " + str(james.top3()))
james.add_times(['1:00', '2.02', '1-44'])
print(james.name + "'s 3. fastest times are: " + str(james.top3()))
