# Dependencies
import os
import csv

inputPath = os.path.join('Resources', 'budget_data.csv')

with open(inputPath) as csvFile:

    # CSV reader specifies delimiter and variable that holds contents
    csvReader = csv.reader(csvFile, delimiter=',')

    # Read the header row first
    csvHeader = next(csvReader)

    #Initialize variables used to story summary values
    totalMonths = 0
    total = 0
    avgChange = 0
    maxChange = 0
    minChange = 0
    changeList = []
    prevMonthProfit = 0
    
    # Read each row of data after the header
    for row in csvReader:
        totalMonths = totalMonths + 1
        total = total + int(row[1])
        curChange = int(row[1]) - prevMonthProfit
        
        if totalMonths > 1:
            changeList.append(curChange)
        
        if curChange > maxChange:
            maxChange = curChange
            maxChangeMonth = row[0]
            
        if curChange < minChange:
            minChange = curChange
            minChangeMonth = row[0]
            
        prevMonthProfit = int(row[1])

avgChange = sum(changeList) / len(changeList)

print(f"Total Months: {totalMonths}")
print(f"Total: {total}")
print(f"Average Change: {avgChange}")
print(f"Greatest Increase in Profits: {maxChangeMonth} ({maxChange})")
print(f"Greatest Decrease in Profits: {minChangeMonth} ({minChange})")


# # Specify the file to write to
# output_path = os.path.join('analysis', 'budget_analysis.csv')

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvFile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvFile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
