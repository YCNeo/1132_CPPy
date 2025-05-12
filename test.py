import datetime

print("2023-11-30" > "0000-01-01")

d1 = datetime.datetime.strptime("2023-01-01", "%Y-%m-%d").date()
d2 = datetime.datetime.strptime("2023-05-20", "%Y-%m-%d").date()

count_1sts = 0
current = d1
while current <= d2:
    if current.day == 1:
        count_1sts += 1
    current += datetime.timedelta(days=1)

print(count_1sts)
