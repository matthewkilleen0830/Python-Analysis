# Python Challenge:  PyPoll

# Import required modules
import os
import csv

# Set path to retrieve CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# Set path to save text file
file_to_save = os.path.join('Analysis', 'election_textfile.txt')

# Declare empty lists to store data from CSV
total_count_of_votes = []
candidates = []

# Declare variables to find winner, set initial values
winner = ""
winner_votes = 0

# Create dictionary to store candidate name appearances (a.k.a. votes)
individual_candidate_votes = {}

# Declare variable to count all votes, set initial value
total_votes = 0

# Read CSV file using encoding for Windows and declare temporary variable to store contents
with open(election_csv, newline='', encoding='utf-8') as csvfile:

    # Declare new variable specifying delimiter to separate values and store contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store and bypass the header row
    column_labels = next(csvreader)

    # Loop through each each row of data after the header in "csvreader" and add values to dictionary
    for vote_row in csvreader:
              
        # Add each vote to total count of votes list
        total_votes += 1

        # Declare variable, retrieve the candidate name from each row, and store value
        individual_candidate = vote_row[2]

        # Conditional statement within loop to find individual candidate appearances (a.k.a. votes) in "candidates" list
        if individual_candidate not in candidates:
            
            # Add individual candidate name to "candidates" list
            candidates.append(individual_candidate)
            
            # Set initial entry in "individual_candidate_votes" dictionary to zero
            individual_candidate_votes[individual_candidate] = 0
        
        # As loop finds "individual_candidate" names, add 1 to previous value as it loops through "individual_candidate_votes" dictionary
        individual_candidate_votes[individual_candidate] = individual_candidate_votes[individual_candidate] + 1

# Declare variable, store first part of election summary, and print first part of election summary to terminal
with open(file_to_save, "w") as txt_file:
    election_summary = (f"Election Results\n"
                        f"--------------------------\n"
                        f"Total Votes: {total_votes}\n"
                        f"--------------------------\n")
    print(election_summary)
    
    # Write first part of election summary to text file
    txt_file.write(election_summary)

    # Loop through "individual_candidate_votes" dictionary, tally vote counts, and store to variable
    for x in individual_candidate_votes:
        individual_votes = individual_candidate_votes.get(x)
        
        # Declare variable, cast strings to number using 'float' and calculate individual percentage, and store to variable
        percentage = float(individual_votes) / float(total_votes) * 100
        
        # Declare variable, format number variable within f string, and store second part of election summary to variable
        output = (f"{x}: {percentage:.3f}% ({individual_votes})\n")
        
        # Print second part of election summary to terminal
        print(output)
        
        # Write second part of election summary to text file
        txt_file.write(output)

        # Conditional statement to loop through "individual_candidate_votes" to compare vote totals to find winner
        if individual_votes > winner_votes:
            winner_votes = individual_votes
            winner = x

    # Print winner to terminal
    winning_name = (f'--------------------------\n'
                    f'Winner:  {winner}\n'
                    f'--------------------------')
    print(winning_name)
    
    # Write winner to text file
    txt_file.write(winning_name)