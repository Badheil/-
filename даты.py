import datetime
DD,MM,YYYY = map(int,input().split("-"))
the_day = datetime.date(YYYY, MM, DD)
if the_day.weekday() != 0:
    monday_day = DD - the_day.weekday()
else:
    monday_day = DD
the_monday_day = datetime.date(YYYY, MM, monday_day)
if the_monday_day.month > 9:
    print("{}-{}-{}".format(the_monday_day.day,
    the_monday_day.month, the_monday_day.year))
else:
    print("{:02}-{:02}-{}".format(the_monday_day.day,
    the_monday_day.month, the_monday_day.year))