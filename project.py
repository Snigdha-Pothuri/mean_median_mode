import csv
from collections import Counter 
with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    number=file_data[i][2]
    new_data.append(float(number))
n=len(new_data)
total=0
for x in new_data:
    total+=x     
mean=total/n
print("Average is:"+str(mean))  

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    number=file_data[i][2]
    new_data.append(float(number))
n=len(new_data)
new_data.sort()   
if(n/2 == 0):
    median1=float(new_data[n//2])
    median2=float(new_data[n//2-1])
    median=(median1+median2)/2
else:
    median=new_data[n//2]
print("median is:"+str(median))

with open("SOCR-HeightWeight.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    number=file_data[i][2]
    new_data.append(float(number))
data=Counter(new_data)
for height,occurence in data.items():
    if(occurence==max(list(data.values()))):
        print(occurence)
        print(height)
