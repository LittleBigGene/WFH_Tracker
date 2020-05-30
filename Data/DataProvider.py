
import pandas as pd

class DataProvider():

    def holidays(self):
        return pd.read_csv('Data/Holidays.csv')

    def vacations(self):
        return pd.read_csv('Data/Vacations.csv')

    def work_from_home(self):        
        pass

if __name__ == '__main__':

    dp = DataProvider()
    print(dp.holidays()) 
    print(dp.vacations()) 
