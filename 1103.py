import datetime

while sum((hour := list(map(int, input().split())))) != 0:
    h1, m1, h2, m2 = hour
    time1 = datetime.datetime(year=2021, month=5, day=23, hour=h1, minute=m1)

    if h2 < h1 or h1 == h2 and m2 < m1:
        time2 = datetime.datetime(year=2021, month=5, day=24, hour=h2, minute=m2)
    else:
        time2 = datetime.datetime(year=2021, month=5, day=23, hour=h2, minute=m2)
    total = time2 - time1

    print(int(total.seconds/60))
