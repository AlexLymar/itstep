from datetime import date
import scipy.constants

current_year = date.today()
print(current_year.strftime("%Y"))

light_speed_in_vacuum = scipy.constants.c
print(light_speed_in_vacuum)

quote = str('"Можливо все, неможливе просто потребує більше часу." Ден Браун')
print(quote)

oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
print(oceans)


active = 10
x = 11
active = active > x
print(active == False)

naming = 'itstep'
print(list(naming))

school = {'students amount:': 5, 'students:' : ['Neo', 'Trinity', 'Morpheus', 'Mouse', 'Tank'], 'subjects': ['Python', 'Math', 'English', 'KungFu']
          }
print(school)


