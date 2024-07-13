# Dependencies
import os
import csv

# Define input file path
inputPath = os.path.join("Resources", "election_data.csv")
outputPath = os.path.join("analysis", "election_results.txt")

# Open csv file
with open(inputPath) as csvFile, open(outputPath, "w") as txtFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvReader = csv.DictReader(csvFile, delimiter=",")

    # Initialize variables used to story summary values
    totalVotes = 0
    candidateVotes = {}

    # Read each row of data
    for row in csvReader:
        # Get total vote count
        totalVotes += 1
        # Get total vote count for each candidate
        if row["Candidate"] in candidateVotes:
            candidateVotes[row["Candidate"]] += 1
        else:
            candidateVotes[row["Candidate"]] = 1

    # Store results in a list so they can be printed to the terminal and a file at the same time
    results = []
    results.append("\nElection Results")
    results.append("-------------------------")
    results.append(f"Total votes: {totalVotes:,}")
    results.append("-------------------------")

    # Calculate and print candidate vote percentages
    for candidate, votes in candidateVotes.items():
        percentage = (votes / totalVotes) * 100
        results.append(f"{candidate}: {percentage:.3f}% ({votes:,})")

    # Find the winning candidate
    winner = max(candidateVotes.items(), key=lambda item: item[1])
    results.append("-------------------------")
    results.append(f"Winner: {winner[0]}")
    results.append("-------------------------\n")

    # Print results to terminal and write to file
    for line in results:
        print(line)
        txtFile.write(line + "\n")
