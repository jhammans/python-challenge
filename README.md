# Python Challenge

## PyPoll - Election Results Analysis

This project analyzes election data from a CSV file and provides a summary of the results, including the total number of votes, the percentage of votes each candidate received, and the name of the winning candidate.

### Project Structure

PyPoll/
├── analysis/
│ ├── election_results.txt
├── Resources/
│ ├── election_data.csv
├── main.py

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

### Requirements

- Python 3.x

### Contributing

If you have suggestions for improvements or would like to contribute, please fork the repository and create a pull request. For major changes, please open an issue to discuss what you would like to change.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Notes:

Replace yourusername in the clone URL with your actual GitHub username.
Adjust the project structure and any other details to fit your actual project setup.
You may need to create a LICENSE file if you intend to license your project under the MIT License.