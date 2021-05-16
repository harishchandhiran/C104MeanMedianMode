import csv

with open("SOCR-HeightWeight.csv",newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)

n = len(new_data)
new_data.sort()
#Using slow division get the nearest whole number
#Slow division is represented by //
if(n%2==0):
    #Getting the first median
    median1 = float(new_data[n//2])
    #Getting the first median
    median2 = float(new_data[n//2-1])
    #Getting the mean of two meadians
    meadian = (median1 + median2) / 2
else:
    meadian = float(new_data[n//2])
print(meadian)