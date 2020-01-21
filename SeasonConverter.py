#MaxLab
# Written by Ryuon
def monthCovert (str):
    month = str.capitalize()
    return month
    
def dayCheck(int):
    if int < 1 or int > 31:
        print("Invalid day")
        exit()

#slice5 = slice(0, 5, 1)
#print(name[slice5])
def seasonOfYear(day, month):
    dayCheck(day)
    month = monthCovert(month)
    if month == "January":
        print("Winter")

    elif month == "February":
        print("Winter")

    elif month == "March":
        if day < 20:
            print("Winter")
        else :
            print("Spring")

    elif month == "April":
        print("Spring")

    elif month == "May":
        print("Spring")

    elif month == "June":
        if day < 21:
            print("Spring")
        else :
            print("Summer")

    elif month == "July":
        print("Summer")

    elif month == "August":
        print("Summer")

    elif month == "September":
        if day < 22:
            print("Summer")
        else :
            print("Autumn")

    elif month == "October":
        print("Autumn")

    elif month == "November":
        print("Autumn")

    elif month == "December":
        if day < 21:
            print("Autumn")
        else :
            print("Winter")

    else :
        print("Invalid month")

seasonOfYear(5, "august")
