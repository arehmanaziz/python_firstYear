date = int(input("Enter day of the date: "))
month = int(input("Enter month of the date: "))
day = 0

if month == 1:
    day = date

elif month == 2:
    day = date + 31

elif month == 3:
    day = date + 59

elif month == 4:
    day = date + 90

elif month == 5:
    day = date + 120

elif month == 6:
    day = date + 151

elif month == 7:
    day = date + 181

elif month == 8:
    day = date + 212

elif month == 9:
    day = date + 242

elif month == 10:
    day = date + 273

elif month == 11:
    day = date + 303

elif month == 12:
    day = date + 334

print(day)