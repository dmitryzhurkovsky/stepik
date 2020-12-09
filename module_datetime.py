import datetime

year, month, day = map(int, input().split())
cur_date = datetime.date(year, month, day)
delta = datetime.timedelta(days=int(input()))
result = cur_date + delta
print(result.year, result.month, result.day)
