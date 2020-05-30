import pandas as pd

from Data.DataProvider import DataProvider
dp = DataProvider()

full_year = pd.DataFrame(pd.date_range(start='2020-1-1', end='2020-12-31').to_series(), columns=['Date'] )

full_year['DayOfWeek'] = full_year['Date'].dt.weekday

full_year['IsHoliday'] = full_year.Date.isin(dp.holidays())

full_year['OnVacation'] = full_year.Date.isin(dp.vacations().Vacation)

full_year['WorkingFromWA'] = full_year.Date.isin(dp.work_from_home())


working_calendar = full_year.query('DayOfWeek < 5 & not OnVacation & not IsHoliday') 

wfhDays = working_calendar.query('WorkingFromWA')

print(working_calendar.count())



