# Python Challenge

## PyBank - Financial Results Analysis

This project analyzes financial data from a CSV file and provides a summary of the results.

### Project Structure

- `analysis/` : Directory containing the output text file.
- `Resources/` : Directory containing the input CSV file.
- `main.py` : Main script to perform the financial results analysis.

### Input Data

The input data is expected to be in a CSV file located at `Resources/budget_data.csv`. The CSV file should contain the following columns:

- `Date` : Month and year.
- `Profit/Loss` : Profit or loss for the period.

### Output Data

The script outputs the results to the console and writes to `analysis/budget_analysis.txt`. The output includes:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

### Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/jhammans/python-challenge.git
    cd python-challenge/PyBank
    ```

2. **Prepare the input data:**
    - Place your `budget_data.csv` file in the `Resources/` directory.

3. **Run the script:**
    ```sh
    python main.py
    ```

4. **View the results:**
    - The results will be printed to the console.
    - The results will also be written to `Resources/budget_analysis.txt`.

### Example

Here is an example of the expected output in `budget_analysis.txt`:

Financial Analysis

Total Months: 86

Total: $22,564,198.00

Average Change: $-8,311.11

Greatest Increase in Profits: Aug-16 ($1,862,002.00)

Greatest Decrease in Profits: Feb-14 ($-1,825,558.00)


## PyPoll - Election Results Analysis

This project analyzes election data from a CSV file and provides a summary of the results.

### Project Structure

- `analysis/` : Directory containing the output text file.
- `Resources/` : Directory containing the input CSV file.
- `main.py` : Main script to perform the election results analysis.

### Input Data

The input data is expected to be in a CSV file located at `Resources/election_data.csv`. The CSV file should contain the following columns:

- `Voter ID` : Unique identifier for each voter.
- `County` : The county in which the vote was cast.
- `Candidate` : The candidate for whom the vote was cast.

### Output Data

The script outputs the election results to the console and writes the results to `analysis/election_results.txt`. The output includes:

- Total number of votes cast.
- Percentage and number of votes each candidate received.
- The winning candidate.

### Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/jhammans/python-challenge.git
    cd python-challenge
    ```

2. **Prepare the input data:**
    - Place your `election_data.csv` file in the `Resources/` directory.

3. **Run the script:**
    ```sh
    python main.py
    ```

4. **View the results:**
    - The results will be printed to the console.
    - The results will also be written to `Resources/election_results.txt`.

### Example

Here is an example of the expected output in `election_results.txt`:

Election Results

Total votes: 3521001

Charles Casper Stockham: 23.049% (805,051)
Diana DeGette: 73.812% (2,780,582)
Raymon Anthony Doane: 3.139% (114,368)

Winner: Diana DeGette