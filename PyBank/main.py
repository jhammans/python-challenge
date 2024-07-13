# Dependencies
import os
import csv

# Define input file path
inputPath = os.path.join("Resources", "budget_data.csv")

# Open csv file
with open(inputPath) as csvFile:

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

# Print summary to terminal
print("\nFinancial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${total:,.2f}")
print(f"Average Change: ${avgChange:,.2f}")
print(f"Greatest Increase in Profits: {maxChangeMonth} (${maxChange:,.2f})")
print(f"Greatest Decrease in Profits: {minChangeMonth} (${minChange:,.2f})\n")


# Specify the file to write to
outputPath = os.path.join('analysis', 'budget_analysis.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(outputPath, 'w') as export:

    # Write the text file with summary results
    export.write("Financial Analysis\n")
    export.write("----------------------------\n")
    export.write("Total Months: {}\n".format(totalMonths))
    export.write("Total: ${:,.2f}\n".format(total))
    export.write("Average Change: ${:,.2f}\n".format(avgChange))
    export.write("Greatest Increase in Profits: {} (${:,.2f})\n".format(maxChangeMonth, maxChange))
    export.write("Greatest Decrease in Profits: {} (${:,.2f})\n".format(minChangeMonth, minChange))
