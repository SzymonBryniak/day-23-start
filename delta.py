import datetime
import time

lastTime = datetime.datetime.now()
print(lastTime)
while True:
    period = datetime.datetime.now()

    if period.second % 30 == 0 and (period - lastTime).total_seconds() >= 1:
        print(period)
        lastTime = period
