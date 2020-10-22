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
    candidates =[]
    vote_count = []
    winner = []
    # candidate_a = []
    # candidate_b = []
    # candidate_c = []
    # candidate_d = []
        
    for row in csvreader:
        candidate_col.append(row[2])

        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    total_vote = len(candidate_col)

    for name in candidate_col:
        if name in candidate_dict:
            candidate_dict[name] += 1
        else:
            candidate_dict[name] = 1

    print("")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_vote}")
    print(f"-------------------------")

    for x, y in candidate_dict.items():
        print(f"{x}: {round(((y / (total_vote)) * 100), 4)}% ({y})")
        vote_count.append(y)
        winner_vote_count = max(vote_count)
        if y == winner_vote_count:
            winner.append(x)
    print(f"-------------------------")
    print(f"Winner: {winner[0]}")
    print(f"-------------------------")
    # # loop through to get vote counts
    # for votes in candidate_dict:
    #     candidate_dict[votes]



    # # loop through to get candidate names
    # for names in candidate_dict:







    # for x, y in candidate_dict.items():
    #     candidates.append(x)
    #     vote_count.append(y)



    # print(candidates)
    # print(vote_count)
    # for i in range(len(candidate_list)):
    #      vote_count.append(candidate_dict[candidate_list[i]])
    #      print(vote_count)
        #  if candidate_dict[candidate_list[i]] != candidate_dict[candidate_list[i + 1]]:
             
 

# I need to give the key a variable to extract them    
   
        # if row[2] not in candidate_list:
        #     # get candidate list and index
        #     candidate_list.append(row[2])

        # if row[2] == candidate_list[0]:
        #     candidate_a.append(row[2])
        
        # elif row[2] == candidate_list[1]:
        #     candidate_b.append(row[2])
        
        # elif row[2] == candidate_list[2]:
        #     candidate_c.append(row[2])
        
        # elif row[2] == candidate_list[3]:
        #     candidate_d.append(row[2])

    
   

# print(len(candidate_a))
# print(len(candidate_b))
# print(len(candidate_c))
# print(len(candidate_d))


    

# vote count for each candidate
# total vote casted
# calcuation




  
# export_txt = os.path.join("analysis", "report.txt")

# # create and open a new .txt file in write mode
# with open(export_txt, "w") as txtfile:
#     # input all result in the same fashion
#     # remember to add "\n" for new line





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



