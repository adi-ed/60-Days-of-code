import csv

with open("weather.csv",'r') as f:
    data = list(csv.reader(f))
    
city = input("Enter city(New York, New Zealand or Kuala Lumpur): ")

for row in data[1:]:
    if row[0]==city:
        print("Temperature:",row[1])