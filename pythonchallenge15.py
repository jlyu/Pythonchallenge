'''
import calendar
from datetime import date

for year in range(1006,1996,10):
	if calendar.isleap(year)==True and date(year, 1, 26).weekday()==0:
			print year
			
'''
from calendar import weekday, isleap
print filter(lambda y: isleap(y) and 0==weekday(y, 1, 26), range(1006, 2000, 10))[-2]