import pandas as pd

data=pd.read_html('https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml#',skiprows=1)

statewise=data[2].drop([0,1],axis=0)
statewise=statewise.drop(['Unnamed: 2','1'],axis=1)
statewise.to_csv('statewise.csv',index=False)

cases_time_series=data[3]
cases_time_series=cases_time_series.drop(1,axis=0).drop(columns=['1'])
cases_time_series.to_csv('cases_time_series.csv',index=False)

print(data[12])
