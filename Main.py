import pandas as pd

from Data.DataProvider import DataProvider
dp = DataProvider()

s = pd.date_range(start='2020-1-1', end='2020-12-31').to_series()
df = pd.DataFrame(s , columns=['Date'] )
df['DayOfWeek'] = df['Date'].dt.weekday

df['IsHoliday'] = df.Date.isin(dp.holidays())

df['OnVacation'] = df.Date.isin(dp.vacations().Vacation)

df['WorkingFromWA'] = df.Date.isin(dp.work_from_home())

print( df.iloc[90:150])





