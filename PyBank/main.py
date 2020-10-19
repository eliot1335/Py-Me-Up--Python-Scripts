# Create a script with:
    # The total number of months included in the dataset
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

# loop through every row in csv but skip the header
# contain the loop number in a variable and print in analysis later
"""
print("Financial Analysis")
print("----------------------------")
print("Total Months: 86")
print("Total: $38382578")
print("Average  Change: $-2315.12")
print("Greatest Increase in Profits: Feb-2012 ($1926159")
print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")
"""




