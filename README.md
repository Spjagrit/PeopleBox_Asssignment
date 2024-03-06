# PeopleBox_Asssignment


## Data Processing Steps:

* Reads the input CSV file using pandas.
* Initializes an empty list to store the transformed data.
* Iterates through each row of the input DataFrame, processing various fields such as compensation, reviews, and engagements.
* Constructs a new DataFrame (output_df) with the transformed data.
* Sorts the DataFrame by 'Employee Code' and 'Effective Date'.
* Fills forward missing values for specific columns within each employee group.
* Calculates 'End Date' for each historical record based on the next record's effective date.
* Updates 'End Date' with 'Date of Exit' if available in the input data.
* Sets certain fields to None based on specific conditions.

## Assumptions:

* The input CSV file contains columns such as 'Employee Code', 'Manager Employee Code', 'Date of Joining', 'Date of Exit', 'Compensation', 'Compensation 1', 'Compensation 2', 'Review 1', 'Review 2', 'Review 1 date', 'Review 2 date', 'Engagement 1', 'Engagement 2', 'Engagement 1 date', 'Engagement 2 date'.
* Compensation and review dates are in the format 'YYYY-MM-DD'.
* The script assumes certain default dates for end dates if not explicitly mentioned (e.g., '2100-01-01').
* Certain fields like 'Last Pay Raise Date', 'Performance Rating', 'Engagement Score' may be set to None based on specific conditions.
* Effective Date and End Date are used to track changes over time.
* The script assumes that the data for each employee is contiguous, meaning there are no missing records in between.
* The script assumes the input data is clean and doesn't contain any inconsistencies or missing values in crucial fields.

## Output:

* The transformed data is saved to an output CSV file named 'output.csv'.
