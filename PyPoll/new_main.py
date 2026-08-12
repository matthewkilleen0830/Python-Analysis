# PyPoll Analysis Script
# Perform vote tallying and candidate breakdown from election dataset

# // Revision Date:  2026.Aug.12

# Import core modules for file handling and CSV parsing
import os
import csv

# Construct paths for input dataset and output report
election_csv = os.path.join('Resources', 'election_data.csv')
file_to_save = os.path.join('Analysis', 'election_textfile.txt')

# Initialize containers for vote tracking
total_count_of_votes = []     # // Upd:  2026.Aug.12 (unused list removed later)
candidates = []

# Initialize winner tracking variables
winner = ""
winner_votes = 0

# Dictionary to store vote counts per candidate
individual_candidate_votes = {}

# Track total number of votes processed
total_votes = 0

# Read and parse CSV file using UTF-8 encoding
with open(election_csv, newline='', encoding='utf-8') as csvfile:

    # Initialize CSV reader with comma delimiter
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    column_labels = next(csvreader)

    # Process each vote record
    for vote_row in csvreader:

        # Increment global vote counter
        total_votes += 1

        # Extract candidate name from row
        individual_candidate = vote_row[2]

        # Register candidate if first encounter
        if individual_candidate not in candidates:
            candidates.append(individual_candidate)
            individual_candidate_votes[individual_candidate] = 0

        # Increment candidate vote count
        individual_candidate_votes[individual_candidate] += 1   # // Upd:  2026.Aug.12 simplified increment

# Write election summary to output file
with open(file_to_save, "w") as txt_file:

    # Build and print header section of election summary
    election_summary = (
        f"Election Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"--------------------------\n"
    )
    print(election_summary)
    txt_file.write(election_summary)

    # Iterate through candidate vote totals to compute percentages
    for candidate in individual_candidate_votes:

        individual_votes = individual_candidate_votes[candidate]

        # Compute vote percentage for candidate
        percentage = (individual_votes / total_votes) * 100     # >>> NEW <<< removed unnecessary float casts

        # Build formatted candidate result line
        output = f"{candidate}: {percentage:.3f}% ({individual_votes})\n"

        # Print and write candidate results
        print(output)
        txt_file.write(output)

        # Track candidate with highest vote count
        if individual_votes > winner_votes:
            winner_votes = individual_votes
            winner = candidate

    # Build and print winner section
    winning_name = (
        f"--------------------------\n"
        f"Winner:  {winner}\n"
        f"--------------------------"
    )
    print(winning_name)
    txt_file.write(winning_name)
