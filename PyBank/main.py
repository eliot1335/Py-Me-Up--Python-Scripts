# Create a script with:
    # The total number of months included in the dataset x
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
    # Print analysis and export a text file as report

# load raw data
import os
import csv

# Set path
csvpath = os.path.join("Resources", "budget_data.csv")
# Open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# loop through every row in csv but skip the header
num_rows = 0

for row in open(csvpath):
    num_rows += 1
    total_months = (num_rows - 1)
# loop through every row in csv to add profit/losses
# sum/total_months for average
# max
# min

# contain the loop number in a variable and print in analysis later
# print analysis in terminal

print("Financial Analysis ")
print("----------------------------")
print(f"Total Months: {total_months}")



