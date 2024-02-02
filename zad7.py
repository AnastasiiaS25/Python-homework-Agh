#Kalendarz

from datetime import date

year = int(input('Enter a year: '))

#result = []
#for month in range(1, 13):
    #if date(year, month, 13).weekday() == 4:
        #result.append(date(year,month, 13))

result = [date(year, month, 13)for month in range(1, 13) if date(year, month, 13).weekday()==4]
number = len(result)

print(f'There{"is" if number==1 else"are"}{number}"Friday the 13th" in the year{year}:')

for date in result:
    print('',date.strftime('%d-%m-%Y'))


















