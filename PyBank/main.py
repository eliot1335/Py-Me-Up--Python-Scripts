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
    # skip the header
    header = next(csvreader)

    # set up a For loop to collect total month and total profit/loss
    # initialize variables for month count and total profit/loss
    month = 0
    total_profit_loss = 0
    # create a list to hold profit/loss data of each date
    profit_list =[]
    
    for row in csvreader:
        # increment row counts for total month
        month += 1
        # increment profit/loss value for total profit/loss
        total_profit_loss += int(row[1])
        # collect each profit/loss value into list for later calculation
        profit_list.append(int(row[1]))

    # create a list to hold values of row[1] so I can loop using i and manipuate it
    profit_change_list = []
    for i in range((month)-1):
        profit_change_list.append((profit_list[i+1]) - (profit_list[i]))

# average of the changes = sum of individal changes and divided by total month -1
average_change = round(sum(profit_change_list)/(month - 1), 2)
# get the highest and lowest value of these changes for greatest increase and decrease
greatest_increase = max(profit_change_list)
greatest_decrease = min(profit_change_list)


# # using the index, 
# date_increase = profit_change_list.index(max(profit_change_list))
# date_decrease = profit_change_list.index(min(profit_change_list))

        # attempts to get row[1] of last row
        # rows = list(csvreader)
        # print(len(rows))        

# # # loop through every row in csv to add profit/losses
# # # sum/total_months for average
# # # max
# # # min

# # # contain the loop number in a variable and print in analysis later
# # # print analysis in terminal

# print("Financial Analysis ")
# print("---------------------------- ")
# print(f"Total Months: {month} ")
# print(f"Total: ${total_profit_loss} ")
# print(f"Average Change: ${average_change} ")
# print(f"Greatest Increase in Profits: {increase_date} ")
# print(f"Greatest Decrease in Profits: {decrease_date} ")


