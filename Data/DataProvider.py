
import pandas as pd

class DataProvider():

    def holidays(self):
        h = pd.read_csv('Data/Holidays.csv')
        return pd.to_datetime(h.Holiday)


    def vacations(self):
        v = pd.read_csv('Data/Vacations.csv')
        v.Vacation = pd.to_datetime(v.Vacation)
        return v

    def work_from_home(self):        
        w = pd.read_csv('Data/WFH.csv')

        tempSeries = pd.Series()

        for row in w.iterrows():
            if '~' in row[1].WFH:
                dateRange = row[1].WFH.split('~')
                s = pd.date_range(start = dateRange[0], end=dateRange[1]).to_series()                
                
                w = w.drop(index = row[0])
                tempSeries = tempSeries.append(s)

        tempSeries = w.WFH.append(tempSeries)

        return pd.to_datetime(tempSeries)



if __name__ == '__main__':

    dp = DataProvider()

    # print(dp.holidays()) 
    # print(dp.vacations()) 
    
    print(dp.work_from_home().head(10))
