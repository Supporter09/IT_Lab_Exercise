month_dict = {
    1 : 31,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30, 
    12 : 31
}

month = int(input())
year = int(input())

# YOUR CODE HERE 

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    if month == 2:
        print('29')
    else:
        print(str(month_dict[month]))
else:
    if month == 2:
        print('28')
    else:
        print(str(month_dict[month]))