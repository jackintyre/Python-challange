import os
import csv
num_months=0
total_profit=0
avg_change=0.0
greatest_inc=0
greatest_dec=0
bank_csv = os.path.join("..", "Resources", "budget_data.csv")
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    num_months = len(list(csvreader))
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        total_profit +=int(row[1])
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if (int(row[1])>greatest_inc):
            date_inc= row[0]
            greatest_inc=int(row[1])
with open(bank_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        if (int(row[1])<greatest_dec):
            date_dec=row[0]
            greatest_dec =int(row[1])

avg_change =total_profit/num_months
    
    
print("Total Months:", num_months, "Months")
print("Total Profits:", total_profit)
print("Average Change:", round(avg_change,2))
print("Greatest Increase:", date_inc, greatest_inc)
print("Greatest Decrease:", date_dec, greatest_dec)