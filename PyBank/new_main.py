# PyBank Analysis Script
# Perform financial analysis on monthly profit/loss data

# // Revision Date:  2026.Aug.12

# Import core modules for file handling and CSV parsing
import os
import csv

# Import statistics module for mean calculations
import statistics as avg

# Construct path to input dataset
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Initialize containers for raw CSV fields
month = []
profit_or_loss = []
revenue_change = []

# Compute average change using statistics.mean
def Average(myList):
    return avg.mean(myList)

# Read and parse CSV file using UTF-8 encoding
with open(budget_csv, newline='', encoding='utf-8') as csvfile:

    # Initialize CSV reader with comma delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    column_labels = next(csvreader)

    # Extract month and profit/loss values from each row
    for budget_row in csvreader:

        # Append month label
        month.append(budget_row[0])

        # Convert profit/loss to float and append
        profit_or_loss.append(float(budget_row[1]))

# Compute total net profit/loss across all months
# // Upd:  2026.Aug.12 more Pythonic, use sum() instead of manual loop
net_profit = sum(profit_or_loss)

# Compute month-to-month revenue deltas
# // Upd:  2026.Aug.12 cleaner list comprehension with direct iteration
revenue_change = [
    profit_or_loss[i + 1] - profit_or_loss[i]
    for i in range(len(profit_or_loss) - 1)
]

# Count total number of months
total_months = len(month)

# Compute average revenue change
average_change = Average(revenue_change)

# Identify greatest increase in profits
greatest_profit = max(revenue_change)
list_max_profit = revenue_change.index(greatest_profit)
greatest_month = month[list_max_profit + 1]

# Identify greatest decrease in profits
least_profit = min(revenue_change)
list_min_profit = revenue_change.index(least_profit)
least_month = month[list_min_profit + 1]

# Build formatted financial analysis summary
analysis_summary = (
    f'Financial Analysis\n'
    f'---------------------------------------------------\n'
    f'Total Months:  {total_months}\n'
    f'Total:  ${net_profit:.0f}\n'
    f'Average Change:  ${average_change:.2f}\n'
    f'Greatest Increase in Profits:  {greatest_month} (${greatest_profit:.0f})\n'
    f'Greatest Decrease in Profits:  {least_month} (${least_profit:.0f})'
)

# Output summary to terminal
print(analysis_summary)

# Persist summary to output text file
analysis_output_file = os.path.join("Analysis", "PyBank_Financial_Analysis.txt")
with open(analysis_output_file, 'w') as textfile:
    textfile.write(analysis_summary)
