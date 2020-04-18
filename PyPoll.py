#The data we need to retrieve.
import csv
import os

#Assign variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis","election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Candidate options and votes
candidate_options = []
candidates_votes = {}

#Winning Candidate and Winning count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the elction results and read the file.
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)

    #Read and print the header row
    headers = next(csvreader)
    print(headers)

    #Print each row in the CSV file
    for row in csvreader:
    #Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking the candidate's vote count.
            candidates_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidates_votes[candidate_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    # Save hte final vote count to the text files.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate in candidates_votes:
        #2. Retrieve vote count of a candidate
        votes = candidates_votes[candidate]
        #3 Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        #save the candidate results to our text file.
        txt_file.write(candidate_results)

        #Determin winning vote count and candidate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If ture then set winning_count = votes and winning_percent =
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3 Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate 

    #Votes to the terminal

    #candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

    #Print each candidate , their voter count, and percentage to the terminal
    #print(candidate_results)
    #Save the candidate results to our text file
    #txt_file.write(candidate_results)

    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_count:,}\n"
        f"Winner Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n"
    )

    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

