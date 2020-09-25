month = input()

daynum = int(input())

def month_to_num(month):
    monthnum = 0
    if month == "January":
        monthnum = 1
    if month == "February":
        monthnum = 2
    if month == "March":
        monthnum = 3
    if month == "April":
        monthnum = 4
    if month == "May":
        monthnum = 5
    if month == "June":
        monthnum = 6
    if month == "July":
        monthnum = 7
    if month == "August":
        monthnum = 8
    if month == "September":
        monthnum = 9
    if month == "October":
        monthnum = 10
    if month == "November":
        monthnum = 11
    if month == "December":
        monthnum = 12
    return monthnum

def month_day_to_number(month_num, day_num):
    if month_num == 1:
        return day_num
    elif month_num == 2:
        return (day_num + 31)
    elif month_num == 3:
        return (day_num + 60)
    elif month_num == 4:
        return (day_num + 91)
    elif month_num == 5:
        return (day_num + 121)
    elif month_num == 6:
        return (day_num + 152)
    elif month_num == 7:
        return (day_num + 182)
    elif month_num == 8:
        return (day_num + 213)
    elif month_num == 9:
        return (day_num + 244)
    elif month_num == 10:
        return (day_num + 274)
    elif month_num == 11:
        return (day_num + 305)
    elif month_num == 12:
        return (day_num + 335)

def what_day_of_the_week(day_number):
    day_number = int(day_number)
    while day_number > 7:
        day_number -= 7
    dayname = ""
    if day_number == 1:
        dayname = "Wednesday"
    elif day_number == 2:
        dayname = "Thursday"
    elif day_number == 3:
        dayname = "Friday"
    elif day_number == 4:
        dayname = "Saturday"
    elif day_number == 5:
        dayname = "Sunday"
    elif day_number == 6:
        dayname = "Monday"
    elif day_number == 7:
        dayname = "Tuesday"
    return dayname

number_of_month = month_to_num(month)

num_of_day = month_day_to_number(number_of_month, daynum)

print(month + " " + str(daynum) + "th, 2020 is a " + what_day_of_the_week(num_of_day))