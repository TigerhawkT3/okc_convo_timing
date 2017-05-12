import collections
import re
import sys
import datetime
import os

filename, you, them = sys.argv[1:4] # required args
# to suppress rows with no conversation
suppress = 'suppress' in sys.argv # optional arg 4 or 5

try:
    today = datetime.date(*map(int, sys.argv[4].split('/'))) # optional arg 4, not 5
except (IndexError, TypeError, ValueError):
    today = datetime.datetime.fromtimestamp(os.path.getmtime(filename)).date()

with open(filename) as f:
    content = re.findall(
                rf'^({you}|{them}) ([A-Z][a-z]+) (\d+|-)?(?:, )?(\d{{4}})? (\d\d?:\d\d[ap]m)$',
                f.read(), re.MULTILINE)

result = collections.defaultdict(int)
months = {'January':1, 'Jan':1, 'February':2, 'Feb':2, 'March':3, 'Mar':3,
          'April':4, 'Apr':4, 'May':5, 'June':6, 'Jun':6, 'July':7,
          'Jul':7, 'August':8, 'Aug':8, 'September':9, 'Sep':9, 'Sept':9,
          'October':10, 'Oct':10, 'November':11, 'Nov':11, 'December':12, 'Dec':12}
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
yest = today-datetime.timedelta(days=1)
previous = {days[x.weekday()]:(x.month, x.day) for x in (today+datetime.timedelta(days=dy) for dy in range(-5, -1))}
previous['Yesterday'] = yest.month, yest.day
previous['Today'] = today.month, today.day

def parse(m, d):
    if m in months:
        return months[m], int(d)
    return previous[m]

u, m, d, y, t = content[0]
current = datetime.datetime(int(y or today.year), *parse(m, d))
u, m, d, y, t = content[-1]
max_date = datetime.datetime(int(y or today.year), *parse(m, d)) + datetime.timedelta(days=1)

for item in content:
    user, mo, day, year, t = item
    h = int(t.split(':')[0])
    if t[-2] == 'p':
        h += 12
    mo, day = parse(mo, day)
    result[f'{year or today.year} {mo} {day} {h} {user}'] += 1

print('\t'.join(['Date', you, them]))
while current < max_date:
    y, t = (result.get(f'{current.year} {current.month} {current.day} {current.hour} {u}', 0) for u in (you, them))
    if not suppress or y or t:
        print(f'{current.year}/{current.month:0>2}/{current.day:0>2} {current.hour:0>2}:00\t{y}\t{t}')
    current += datetime.timedelta(hours=1)