class Event:

    _subject = ""
    _error = []
    _activity = ""
    _date = ""
    _day = ""
    _hour = ""
    _person = ""

    def __init__(self, activity, date, day, hour, person, subject):
        self._activity = activity
        self._person = person
        self._subject = subject

        self._date = date
        self._day = day
        self._hour = hour

        self._error = []



    def __str__(self):
        res = ""

        if self._subject != "none":
            res += self._subject + " "

        res += self._activity + " "
        if self._date != "none":
            res += "on " + str(self._date) + " "
        if self._day != "none":
            res += "on " + self._day + " "
        if self._hour != "none":
            res += "at " + str(self._hour) + " "
        if self._person != "none":
            res += "with " + self._person + " "

        return res + '\n'

def handle_month(month):
    try:
        if (int(month)):
            month = int(month)
            if (1 <= month and month <= 12):
                return month
            else:
                Event._error.append("Month error - out of range 1-12")
                return -1
    except:
        print("")

    if(isinstance(month, str)):
        if(month.lower() == "january" or month.lower() == "jan"):
            return 1
        elif(month.lower() == "february" or month.lower() == "feb"):
            return 2
        elif (month.lower() == "march" or month.lower() == "mar"):
            return 3
        elif (month.lower() == "april" or month.lower() == "apr"):
            return 4
        elif (month.lower() == "may"):
            return 5
        elif (month.lower() == "june" or month.lower() == "jun"):
            return 6
        elif (month.lower() == "july" or month.lower() == "jul"):
            return 7
        elif (month.lower() == "august" or month.lower() == "aug"):
            return 8
        elif (month.lower() == "september" or month.lower() == "sep"):
            return 9
        elif (month.lower() == "october" or month.lower() == "oct"):
            return 10
        elif (month.lower() == "november" or month.lower() == "nov"):
            return 11
        elif (month.lower() == "december" or month.lower() == "dec"):
            return 12

        else:
            Event._error.append("Month error - unknown string")
            return -1

    elif(isinstance(month, int)):
        if(1 <= month and month <= 12):
            return month
        else:
            Event._error.append("Month error - out of range 1-12")
            return -1

    Event._error.append("Month error")
    return -1


def handle_day(day):
    if(isinstance(day, str)):
        if(day.lower() == "monday" or day.lower() == "mon"):
            return 0
        elif(day.lower() == "tuesday" or day.lower() == "tue"):
            return 0
        elif(day.lower() == "wednesday" or day.lower() == "wed"):
            return 0
        elif(day.lower() == "thursday" or day.lower() == "thu"):
            return 0
        elif(day.lower() == "friday" or day.lower() == "fri"):
            return 0
        elif(day.lower() == "saturday" or day.lower() == "sat"):
            return 0
        elif(day.lower() == "sunday" or day.lower() == "sun"):
            return 0
        elif (day.lower() == "today"):
            return 0
        elif (day.lower() == "tomorrow"):
            return 0
        else:
            Event._error.append("Day error - unknown string")
            return -1
    Event._error.append("Day error")
    return -1


def handle_hour(hour):
    h = ""
    meridian = ""
    for c in range (0, len(hour)):
        if hour[c].isdigit():
            h += hour[c]
        if hour[c].isalpha():
            meridian += hour[c]

    if 0 < int(h) <= 12 and (meridian == "am" or meridian == "pm"):
        return 0

    Event._error.append("Hour error")
    return -1




