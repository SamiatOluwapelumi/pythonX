from math import ceil
import time

i = 0
while (i < 1):
    food = input('What are you cooking? ')
    if (food.isalpha() == True):
        i = 1
        print('Your food is cooking')
    else:
        print('Invalid food type! Enter again')
        i = 0

t = 0
while (t < 1):
    timeNeeded = input('Enter cooking time in minutes:')
    if (timeNeeded.isnumeric() == True):
        timeInSeconds = int(timeNeeded) * 60
        # timeInSeconds = int(timeNeeded) * 5
        t = 1
    else:
        print('Invalid time! Enter again')
        t = 0

a = 0
while (a < 1):
    alarmPeriod = input('Enter preferred alarm period:')
    if ((alarmPeriod.isnumeric() == True) and (int(alarmPeriod) <= int(timeNeeded))):
        alarmPeriodInSeconds = int(alarmPeriod) * 60
        # alarmPeriodInSeconds = int(alarmPeriod) * 5
        a = 1
    else:
        print('Invalid alarm period! Enter again')
        a = 0

alarmFrequency = ceil(timeInSeconds / alarmPeriodInSeconds)
print(ceil(timeInSeconds / alarmPeriodInSeconds))
print('alerm will sound ', alarmFrequency, 'times')

# Method 1
cookedTime = 0
while (timeInSeconds - cookedTime >= 0):
    if (timeInSeconds - cookedTime >= alarmPeriodInSeconds):
        time.sleep(alarmPeriodInSeconds)

    else:
        time.sleep(timeInSeconds - cookedTime)

    cookedTime += alarmPeriodInSeconds
    print("Reminder ON now")


print('Cooking completed')