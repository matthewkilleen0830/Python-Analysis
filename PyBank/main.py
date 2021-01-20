# Import modules
import os
import csv

# Set path to retrieve CSV file
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Create and name empty lists to store data from CSV
month = []
profit_or_loss = []
revenue_change = []

# Read CSV file using encoding for Windows and declare variable
with open(budget_csv, newline='', encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and creates new variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Bypass the header row
    next(csvreader)

    # Loop through each each row of data after the header and add values to corresponding lists
    for budget_row in csvreader:
                
        # Add month from each row
        month.append(budget_row[0])

        # Cast profit or loss to number using 'float' and add to list
        profit_or_loss.append(float(budget_row[1]))

# Declare variable, count total number of months, and store value
total_months = (len(month))
print(total_months)

# Declare variable, calculate net total amount of profit or loss, and store value
net_pl = sum(profit_or_loss)
print(net_pl)

# Loop through each row of data in list, declare variable, and calculate average and store value
for x in range(1,len(profit_or_loss)):
    revenue_change.append(profit_or_loss[x] - profit_or_loss[x - 1])
    monthly_change = (profit_or_loss[x] - profit_or_loss[x - 1])
    
    
    print(monthly_change)
    # average_change = sum(revenue_change) / len(revenue_change)
    # print(average_change)

    # Write a function that returns the arithmetic average for a list of numbers
    # def average(monthly_change):
    #     length = len(monthly_change)
    #     total = 0.0
    #     for number in monthly_change:
    #         total += number
    #     return total / length








# Declare variable, locate the greatest increase in profits (date and amount), and store value
greatest_increase = max(revenue_change)
print(greatest_increase)

# Declare variable, locate date of greatest increase in profits, and store value
list_max_pl = revenue_change.index(greatest_increase)

# Declare variable to store the month of greatest increase in profits
greatest_month = month[list_max_pl + 1]
print(greatest_month)
