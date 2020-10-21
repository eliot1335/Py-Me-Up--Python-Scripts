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

    # create a list to hold candidate name
    # or maybe to create a dictionary to hold these data
    candidate_col = []
    candidate_dict = {}
    candidate_list = []
        
    for row in csvreader:
        candidate_col.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    
    total_vote = len(candidate_col)

print(total_vote)
print(candidate_list)
    # for i in range(0, total_vote):
    #     candidate_dict["name"] = candidate_col[i]
    
# if row[2] not in candidates




    



  
# export_txt = os.path.join("analysis", "report.txt")

# # create and open a new .txt file in write mode
# with open(export_txt, "w") as txtfile:
#     # input all result in the same fashion
#     # remember to add "\n" for new line
#     txtfile.write(f"{candidate_dict} " "\n")




# if row[2] == xxx:
    # xxx_vote_count += 1




# # set export path
# export_txt = os.path.join("analysis", "report.txt")

# # create and open a new .txt file in write mode
# with open(export_txt, "w") as txtfile:
#     # input all result in the same fashion
#     # remember to add "\n" for new line
    #  txtfile.write("---------------------------- " "\n")

# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------



