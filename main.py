import csv
import numpy as np

with open(r"C:\Users\goshe\PycharmProjects\numpy_hw\temp_analysis\temperatures.csv", encoding="utf-8-sig") as f:
    data = csv.reader(f)
    data = np.array(list(data))
