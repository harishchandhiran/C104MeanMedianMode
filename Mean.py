import csv
from collections import Counter

with open("SOCR-HeightWeight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0

for a in new_data:
    total = total + a
mean = total/n
print("mean:- ",mean)