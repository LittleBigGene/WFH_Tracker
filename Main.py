import pandas as pd

from Data.DataProvider import DataProvider
dp = DataProvider()

full_year = pd.DataFrame(pd.date_range(start='2020-1-1', end='2020-12-31').to_series(), columns=['Date'] )

full_year['DayOfWeek'] = full_year['Date'].dt.weekday

full_year['Holiday'] = full_year.Date.isin(dp.holidays())

full_year['OnVacation'] = full_year.Date.isin(dp.vacations().Vacation)

full_year['WorkingFromWA'] = full_year.Date.isin(dp.work_from_home())


working_calendar = full_year.query('DayOfWeek < 5 & not OnVacation & not Holiday') 

wfhDays = working_calendar[working_calendar.WorkingFromWA].Date.count()

print(f'There are total {working_calendar.Date.count()} working days in 2020, of which {wfhDays} days are WFH, {round(wfhDays/working_calendar.Date.count()*100,2)}%')



