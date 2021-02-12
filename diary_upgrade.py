# diary_upgrade program
# с вводом 1-7 пока переключатель в голове не срабатывает.. доработаю!!

week_day = {"MONDAY": "at 7-10pm leave to ItStep for lesson",
            "TUESDAY": " ",
            "WEDNESDAY": "at 7-10pm leave to ItStep for lesson",
            "THURSDAY": "at 4pm Read the 'The Children of Captain Grant','at 8pm Meeting with friend Ivan'",
            "FRIDAY": " ",
            "SATURDAY": " ",
            "SUNDAY": " "
            }
end = 1
while end > 0:
    print('Input "stop" for exit')
    day = input('Enter day please: ')
    day = str(day.upper())
    shedule = day
    if day == 'STOP':
        end -= 1
        print('GOODBYE !!!')
        exit()

    if day in week_day and len(week_day[day]) > 2:
        if len(week_day[day]) > 2:
            print('You have a tasks')
            print(week_day[day])
    else:
        print('No meeting')
