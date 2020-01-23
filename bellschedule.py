from datetime import *
#from time import *

full_day_day = str(time(hour=16, minute=33, second=0).strftime('%H:%M'))
full_day_0 = str(time(hour=8, minute=30, second=0))
full_day_1 = str(time(hour=9, minute=22, second=0))
full_day_2 = str(time(hour=10, minute=13, second=0))
full_day_3 = str(time(hour=11, minute=4, second=0))
full_day_4 = str(time(hour=11, minute=55, second=0))
full_day_5 = str(time(hour=12, minute=46, second=0))
full_day_6 = str(time(hour=1, minute=37, second=0))
full_day_7 = str(time(hour=2, minute=30, second=0))
full_day_8 = str(time(hour=3, minute=19, second=0))


fullDayArray = [full_day_day, full_day_0, full_day_1, full_day_2, full_day_3, full_day_4, full_day_5, full_day_6, full_day_7, full_day_8]

timeRightNow = datetime.now().strftime('%H:%M')
print(timeRightNow)

print(full_day_day)

def periodChecker(array):
	period = 0
	print(array[0])
	if(array[period] == timeRightNow):
		print("Ring")


periodChecker(fullDayArray)

'''
checkerOnOff = True;
while checkerOnOff:
	periodChecker()
	if(buttonIsPressed== True):
		checkerOnOff = False
'''

'''
print(type(full_day_day))
print(fullDayArray[0])
'''

'''
fullDay = ["8:30", "" , 3, 4, 5, 6, 7, 8]
timeRightNow = 1
for periods in fullDay:
	if(fullDay[periods] == timeRightNow):
		print("Ring!")
	else:
		'''
