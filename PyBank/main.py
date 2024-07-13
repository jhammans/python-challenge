# Dependencies
import os
import csv

# Define input and output file paths
inputPath = os.path.join("Resources", "budget_data.csv")
outputPath = os.path.join("analysis", "budget_analysis.txt")

# Open csv file
with open(inputPath) as csvFile, open(outputPath, "w") as txtFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvReader = csv.reader(csvFile, delimiter=",")

    # Read the header row first
    csvHeader = next(csvReader)

    # Initialize variables used to story summary values
    totalMonths = 0
    total = 0
    avgChange = 0
    maxChange = 0
    minChange = 0
    changeList = []
    prevMonthProfit = 0

    # Read each row of data after the header
    for row in csvReader:
        totalMonths += 1
        curMonthProfit = int(row[1])
        total += curMonthProfit
        curChange = curMonthProfit - prevMonthProfit

        # Add changes in month over month profit to list
        if prevMonthProfit != 0:
            changeList.append(curChange)

        # Find the maximum change in profit and the month it occured in
        if curChange > maxChange:
            maxChange = curChange
            maxChangeMonth = row[0]

        # Find the minimum change in profit and the month it occured in
        if curChange < minChange:
            minChange = curChange
            minChangeMonth = row[0]

        # Save previous month's profit to compare to current month
        prevMonthProfit = curMonthProfit

    # Calculate average change
    avgChange = sum(changeList) / len(changeList) if changeList else 0

    # Store results in a list so they can be printed to the terminal and a file at the same time
    results = []
    results.append("\nFinancial Analysis")
    results.append("----------------------------")
    results.append(f"Total Months: {totalMonths}")
    results.append(f"Total: ${total:,.2f}")
    results.append(f"Average Change: ${avgChange:,.2f}")
    results.append(f"Greatest Increase in Profits: {maxChangeMonth} (${maxChange:,.2f})")
    results.append(f"Greatest Decrease in Profits: {minChangeMonth} (${minChange:,.2f})\n")

    # Print results to terminal and write to file
    for line in results:
        print(line)
        txtFile.write(line + "\n")
