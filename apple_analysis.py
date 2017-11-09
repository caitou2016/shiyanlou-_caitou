import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv',header=0)
    data['Date']= pd.to_datetime(data['Date'])
    data.set_index('Date',inplace=True)
    data_jidu = data.resample('3M').sum()
    data_sort = data_jidu.sort_values(['Volume'])
    second_volume = data_sort['Volume'][-2]
    return second_volume
  #  print(second_volume)

if __name__ == '__main__':
    quarter_volume()
