import numpy as np
from main import data

arg_max_day_temp = np.argmax(data[1:, 1].astype(float))
print(arg_max_day_temp)
print(data[1:,0][arg_max_day_temp])

arg_min_night_temp = np.argmin(data[1:, 2].astype(float))
print(arg_min_night_temp)
print(data[1:,0][arg_min_night_temp])

