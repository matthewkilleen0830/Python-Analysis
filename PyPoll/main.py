# Import required modules
import os
import csv

# Set path to retrieve CSV file
election_csv = os.path.join('Resources', 'election_data.csv')
file_to_save = os.path.join('Analysis', 'election_textfile.txt')

# Create and name empty lists to store data from CSV
total_count_of_votes = []
candidates = []

# Find winner
winner = ""
winner_votes = 0

# Create dictionary to store candidate name appearances (votes)
individual_candidate_votes = {}

# Declare variables and set initial values
total_votes = 0

# Read CSV file using encoding for Windows and declare variable
with open(election_csv, newline='', encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and creates new variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store and bypass the header row
    column_labels = next(csvreader)

    # Loop through each each row of data after the header and add values to dictionary
    for vote_row in csvreader:
              
        # Add each vote to total count of votes list
        total_votes += 1

        # Retrieve the candidate name from each row
        individual_candidate = vote_row[2]

        # Conditional statement within loop to find individual name appearances (votes) to add to dictionary
        if individual_candidate not in candidates:
            
            # Add individual candidate name to dictionary
            candidates.append(individual_candidate)
            
            # Set initial entry in dictionary to zero
            individual_candidate_votes[individual_candidate] = 0
        
        # Add 1 to last row as it loops through dictionary
        individual_candidate_votes[individual_candidate] = individual_candidate_votes[individual_candidate] + 1

# Print summary to terminal, and write to text file
with open(file_to_save, "w") as txt_file:
    election_summary = (f"Election Results\n"
                        f"--------------------------\n"
                        f"Total Votes: {total_votes}\n"
                        f"--------------------------\n")
    print(election_summary)
    txt_file.write(election_summary)

    # Loop through dictionary, tally vote counts, calculate percentage, and store to variable
    for x in individual_candidate_votes:
        individual_votes = individual_candidate_votes.get(x)
        percentage = float(individual_votes) / float(total_votes) * 100
        output = (f"{x}: {percentage:.3f}% ({individual_votes})\n")
        
        # Print results to terminal and text file
        print(output)
        txt_file.write(output)

        # Conditional statement within dictionary loop to intrinsically compare vote totals to find winner
        if individual_votes > winner_votes:
            winner_votes = individual_votes
            winner = x

    # Print winner to terminal and text file
    winning_name = (f'--------------------------\n'
                    f'Winner:  {winner}\n'
                    f'--------------------------')
    print(winning_name)
    txt_file.write(winning_name)