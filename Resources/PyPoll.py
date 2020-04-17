#The data we need to retrieve.
import csv
import os


#Assign variable for the file to load and the path.
csvpath = os.path.join("..","Resources","election_results.csv")
#Open the elction results and read the file.
with open(csvpath,newline="") as election_data:
        csvreader = csv.reader(csvpath, delimiter=",")


    # To do: perform analysis.
    

#To do: performanalysis.

# Close the file.
#election_data.close()


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
