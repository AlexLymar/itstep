# diary program
week_day = {"MONDAY": "at 7-10pm leave to ItStep for lesson",
            "TUESDAY": " ",
            "WEDNESDAY": "at 7-10pm leave to ItStep for lesson",
            "THURSDAY": "at 4pm Read the 'The Children of Captain Grant','at 8pm Meeting with friend Ivan'",
            "FRIDAY": " ",
            "SATURDAY": " ",
            "SUNDAY": " "
            }

day = input('Enter day please: ')
day = str(day.upper())
print(day)


if day in week_day:
    if len(week_day[day]) > 2:
      print('You have a tasks')
      print(week_day[day])


else:
    exit()
