# Create a script with:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
# Print analysis and export a text file as report



#

# set up necessary packages to handle raw data
import os
import csv

# Set resource path
csvpath = os.path.join("Resources", "election_data.csv")
# open file
with open(csvpath) as csvfile:
    # set reader
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip the header
    next(csvreader, None)

    cast_count = 0
    # create a list to hold candidate name
    # or maybe to create a dictionary to hold these data
    candidate_col = []

    for row in csvreader:
        cast_count += 1
        candidate_col.append(row[2])
    
    candidate_col.sort()
    print(len(candidate_col))
    # for i in range(len(candidate_col)):
    #     if 





# if row[2] == xxx:
    # xxx_vote_count += 1




# # set export path
# export_txt = os.path.join("analysis", "report.txt")

# # create and open a new .txt file in write mode
# with open(export_txt, "w") as txtfile:
#     # input all result in the same fashion
#     # remember to add "\n" for new line
#     txtfile.write("Financial Analysis " "\n")
#     txtfile.write("---------------------------- " "\n")
#     txtfile.write(f"Total Months: {month} ")
#     txtfile.write(f"Total: ${total_profit_loss} " "\n") 
#     txtfile.write(f"Average Change: ${average_change} " "\n")
#     txtfile.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})" "\n")   
#     txtfile.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")



