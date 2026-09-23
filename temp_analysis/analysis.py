import numpy as np

from main import data

max_day_temp = np.max(data[1:, 1].astype(float))
print(max_day_temp)

min_night_temp = np.min(data[1:, 2].astype(float))
print(min_night_temp)

average_day_temp = np.average(data[1:, 1].astype(float))
print(round(average_day_temp, 2))

average_night_temp = np.average(data[1:, 2].astype(float))
print(round(average_night_temp, 2))

median_day_temp = np.median(data[1:, 1].astype(float))
print(median_day_temp)

median_night_temp = np.median(data[1:, 2].astype(float))
print(median_night_temp)

sum_day_temp = np.sum(data[1:, 1].astype(float))
print(sum_day_temp)

sum_night_temp = np.sum(data[1:, 2].astype(float))
print(sum_night_temp)