import datetime

y, m, d = [int(n) for n in input().split()]
date = datetime.date(y, m, d)
days = datetime.timedelta(days=int(input()))
a = date + days
print(a.year, a.month, a.day)
# ИЛИ:
print((date + days).strftime("%Y %#m %#d"))