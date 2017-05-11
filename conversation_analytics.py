import collections
import re
import sys
import datetime

today = datetime.datetime.now().date()
filename, you, them = sys.argv[1:]

with open(filename) as f:
    content = [line.split() for line in f if re.match(rf'(?:{you}|{them}) [A-Z][a-z]+ (?:\d+|-) \d\d?:\d\d[ap]m$', line.strip())]

result = collections.defaultdict(lambda: collections.defaultdict(int))
months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,
          'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
yest = today-datetime.timedelta(days=1)
previous = {days[x.weekday()]:(x.month, x.day) for x in (today+datetime.timedelta(days=dy) for dy in range(-5, -1))}
previous['Yesterday'] = yest.month, yest.day
previous['Today'] = today.month, today.day

def parse(m, d):
    if m in months:
        return months[m], int(d)
    return previous[m]

u, m, d, t = content[0]
min_month, min_day = parse(m, d)
u, m, d, t = content[-1]
max_month, max_day = parse(m, d)

for item in content:
    user, mo, day, t = item
    h = int(t.split(':')[0])
    if t[-2] == 'p':
        h += 12
    mo, day = parse(mo, day)
    result[f'{mo} {day} {h}'][user] += 1

print('\t'.join(['Date', you, them]))
for month in range(min_month, max_month+1):
    for day in range(min_day, max_day+1):
        for hour in range(24):
            y, t = (result.get(f'{month} {day} {hour}', {}).get(u, 0) for u in (you, them))
            print(f'{month}/{day}/{hour}\t{y}\t{t}')