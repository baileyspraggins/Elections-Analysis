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

#County List and votes per county list
counties = [] 
counties_count = 0

#Largest turnout and highest turnout tracker
largest_turnout = ""
c_highest_count = 0
c_highest_percentage = 0

#County voting dictionary
counties_voting = {} 

#Open the elction results and read the file.
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)

    #Read and print the header row
    headers = next(csvreader)
    #print(headers)

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

        #Print the county name for each row.
        county_name = row[1]

        #If the county name does not match any existing candidate
        if county_name not in counties:
            #Add the county name to the county list
            counties.append(county_name)
            #Begin tracking the counties vote count
            counties_voting[county_name] = 0
        #Add a vote to that countie's count
        counties_voting[county_name] += 1

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text files.
    txt_file.write(election_results)

    #Print the County Vote Header
    county_header = (
        f"             \n"
        f"County Votes:\n"
    )
    print(county_header)
    txt_file.write(county_header)

    #Determine the percentage of votes for each county by looping throug the counts
    #1 Iterate through the county list
    for county in counties_voting:
        #2 Retrieve vote count of a candidate
        c_votes = counties_voting[county]
        #3 Calculate the percentage of votes
        c_votes_percentage = float(c_votes) / float(total_votes) * 100

        county_results = (f"{county}: {c_votes_percentage:.1f}% ({c_votes:,})\n")

        #Print each counties voter count and percentage to the terminal
        print(county_results)
        #Save the candidate results to our text file.
        txt_file.write(county_results) 

        #Determine highest vote count county
        #Determine if the votes are greater that the most votes in a county
        if (c_votes > c_highest_count) and (c_votes_percentage > c_highest_percentage):
            #2 If true then set highest county count to county votes and highest county percentage to county vote percentage
            c_highest_count = c_votes
            c_highest_percentage = c_votes_percentage
            #3 Set the winning county equal to the counties name
            largest_turnout = county

    #Print the highest voting count summary and save it to the Text file
    highest_voting_county_summary = (
        f"--------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"--------------------------\n"
    )
    
    print(highest_voting_county_summary)
    txt_file.write(highest_voting_county_summary)

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

        #Determine winning vote count and candidate
        #1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If ture then set winning_count = votes and winning_percent =
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3 Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate 


    winning_candidate_summary = (
        f"---------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_count:,}\n"
        f"Winner Percentage: {winning_percentage:.1f}%\n"
        f"---------------------\n"
    )



    #Print the highest voting count summary and save it to the Text file
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

