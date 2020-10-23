# Create a script with:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
    # Print analysis and export a text file as report

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

    # create a list to hold values in row[2] (for total vote counts)
    candidate_col = []
    # create a dictionary to pair candidate names (keys) and their vote counts (value)
    candidate_dict = {}
    # created this list to store the vote count values of each candidate (to find the winner)
    vote_count = []
    # create this list to store the winner, there will be only one item inside which is the winner
    winner = []

    # loop through csv to get the len of column 3 (name of candidates)
    # (for total vote counts)
    for row in csvreader:
        candidate_col.append(row[2])

    total_vote = len(candidate_col)

    # loop through the list of column 3 
    # use these names in column 3 as key
    # fill the empty dictionary with candidate: vote_count
    # if the key is the same with the next, increment vote_count
    # if not the same increment the vote_count value with newly paired key
    for name in candidate_col:
        if name in candidate_dict:
            candidate_dict[name] += 1
        else:
            candidate_dict[name] = 1

    # ignore the export part
    # because I don't know how to assign variables to each key and value in dictionary
    # so I have to run for loops to:
    # do calculations/print analysis in terminal/expert report
    export_txt = os.path.join("analysis", "report.txt")
    with open(export_txt, "w") as txtfile:

        print("")
        txtfile.write(f"Election Results" "\n")
        print(f"Election Results")
        txtfile.write(f"-------------------------" "\n")
        print(f"-------------------------")
        txtfile.write(f"Total Votes: {total_vote}" "\n")
        print(f"Total Votes: {total_vote}")
        txtfile.write(f"-------------------------" "\n")
        print(f"-------------------------")

        # using .items() to get keys(candidate name) and value(vote counts) loop by loop
        for x, y in candidate_dict.items():
            # x would be candidate name
            # y would be vote counts
            # vote counts / total vote counts * 100 for percentage
            # use f string:{:0.3f} to format the value into 3 decimal places
            print(f"{x}: {round(((y / (total_vote))) * 100, 4):0.3f}% ({y})")
            txtfile.write(f"{x}: {round(((y / (total_vote))) * 100, 4):0.3f}% ({y})" "\n")
            # append vote counts to list
            vote_count.append(y)
            # use max() to find the highest in the list
            # hense the winner's vote count
            winner_vote_count = max(vote_count)
            # back track the winner's name
            if y == winner_vote_count:
                winner.append(x)

        txtfile.write(f"-------------------------" "\n")
        print(f"-------------------------")
        txtfile.write(f"Winner: {winner[0]}" "\n")
        print(f"Winner: {winner[0]}")
        txtfile.write(f"-------------------------" "\n")
        print(f"-------------------------")
    
        export_txt = os.path.join("analysis", "report.txt")
        with open(export_txt, "w") as txtfile:
            txtfile.write("---------------------------- " "\n")
