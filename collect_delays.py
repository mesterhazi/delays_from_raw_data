import pymysql
import pandas

conn = pymysql.connect(host='192.168.0.12', db='train_data', user='vonat_data_getter', password='user')
all_data = pandas.read_sql('SELECT * FROM trains', conn)
all_data.head(10)
all_data['train_number'].drop_duplicates()
all_train_numbers = all_data['train_number'].drop_duplicates()
all_days = all_data['day']
all_train_numbers = all_data['train_number']
day = all_data[all_data['day'] == all_data['day'][-1]]
all_data['day'][-1]
all_data.day[-1]
all_data.day[1]
day = all_data[all_data['day'] == all_data['day'][1]]
train = all_data[al_data['train_number'] == all_data['train_number'][9]]
train = all_data[all_data['train_number'] == all_data['train_number'][9]]
train
train = all_data['train_number'] == all_data['train_number'][9]
train.shape()
train[0]
day = all_data['day'] == all_data['day'][1]
one_day = all_data[train and day]
one_day = all_data[train & day]
one_day
train = all_data['train_number'] == all_data['train_number'][101]
one_day = all_data[train & day]
one_day
