from main import data
import numpy as np

count_day_temp_1 = 0
for i in data[1:,0:1].astype(str|float):
    if i[1]>=30:
        print(i[0])

count_night_temp_1 = 0
for i in data[1:,2].astype(float):
    if i<-3:
        count_night_temp_1 += 1
print(count_night_temp_1)

count_day_temp_2 = 0
for i in data[1:,1].astype(float):
    if i>=25:
        count_day_temp_2 += 1
print(count_day_temp_2)

