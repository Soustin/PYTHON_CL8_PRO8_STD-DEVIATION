import math
import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# file_data.pop(0)

# sorting the data and storing in the list
data = file_data[0]

# finding mean
def mean(data):
    n_data = len(data)
    total = 0
    for i in data:
        total += int(i)
    mean = total/n_data
    print("Mean is "+ str(mean))
    return mean

# sqauring and getting the values
square_list = []
for num in data:
    a = int(num)-mean(data)
    a = a**2
    square_list.append(a)
    
# getting sum
sum = 0
for i in square_list:
    sum += i

# dividing the sum by the total values
result = sum/len(data)-1

# getting the square-root to find the std_deviation
std_deviation = math.sqrt(result)

print(std_deviation)