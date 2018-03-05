from enum import Enum
import time

time.timezone
Moth=Enum('Month',('jan','Feb'))

print(Moth);

class Weekday(Enum):
    Sun=0
    Mon=1


print(Weekday.Sun.value)
