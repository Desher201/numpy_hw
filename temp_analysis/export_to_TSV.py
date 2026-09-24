from main import data
import csv

"""
min_night_temperature #мінімальна нічна температура
max_day_temperature #максимальна денна температура
mean_day_temperature #середня денна температура
mean_night_temperature #середня нічна температура
sum_day_temperature #сума всіх денних температур
sum_night_temperature #сума всіх нічних температур
days_count #кількість днів
below_zero_nights #кількість ночей із температурою нижче 0°C
at_or_above_30_days #кількість днів із температурою 30°C і вище
"""

min_night_temperature = data[1:,2].astype(float).min()
min_day_temperature = data[1:,1].astype(float).min()
mean_day_temperature = data[1:,1].astype(float).mean()
mean_night_temperature = data[1:,1].astype(float).mean()
sum_day_temperature = data[1:,1].astype(float).sum()
sum_night_temperature = data[1:,2].astype(float).sum()
days_count = len(data[1:,0].astype(str))
below_zero_nights = len([i for i in data[1:,2].astype(float) if i == 0])
at_or_above_30_days = len([i for i in data[1:,1].astype(float) if i >= 30])

datas = {"min_night_temperature":min_night_temperature,
 "min_day_temperature":min_day_temperature,
 "mean_day_temperature":mean_day_temperature,
 "mean_night_temperature":mean_night_temperature,
 "sum_day_temperature":sum_day_temperature,
 "sum_night_temperature":sum_night_temperature,
 "days_count":days_count,
 "below_zero_nights":below_zero_nights,
 "at_or_above_30_days":at_or_above_30_days}

with (open("data.tsv", "a", encoding="utf-8",newline="") as f):
    tsv_writer = csv.writer(f, delimiter="\t")
    for v,k in datas.items():
        tsv_writer.writerow([v,k])