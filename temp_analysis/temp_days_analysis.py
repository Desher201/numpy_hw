from main import data
import numpy as np

count_night_temp_1 = 0
for i in data[1:,2].astype(float):
    if i<0:
        count_night_temp_1 += 1
print(count_night_temp_1)

count_day_temp_1 = 0
for i in data[1:,1].astype(float):
    if 0<=i<=9:
        count_day_temp_1 += 1
print(count_day_temp_1)

count_day_temp_2 = 0
for i in data[1:,1].astype(float):
    if 10<=i<=19:
        count_day_temp_2 += 1
print(count_day_temp_2)

count_day_temp_3 = 0
for i in data[1:,1].astype(float):
    if 20<=i<=29:
        count_day_temp_3 += 1
print(count_day_temp_3)

count_day_temp_4 = 0
for i in data[1:,1].astype(float):
    if i>=30:
        count_day_temp_4 += 1
print(count_day_temp_4)

