import math
import csv
import plotly.express as px

with open("data.csv", "r", newline="") as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)

data = file_data[1]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squared_list = []

for i in data:
    a = int(i)-mean(data)
    a = a**2
    squared_list.append(a)

sum = 0

for i in squared_list:
    sum = sum + i

result = sum/(len(data)-1)

standard_deviation = math.sqrt(result)

print(file_data)
print(standard_deviation)