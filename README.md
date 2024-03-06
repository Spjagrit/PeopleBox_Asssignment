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


## Code Description

The provided Python script is designed to process input data regarding employee information stored in a CSV file and transform it into a structured output format. Let's break down the code into several paragraphs for clarity.

The first section of the script imports the pandas library and reads the input CSV file named 'input.csv' into a pandas DataFrame called input_df. Additionally, it initializes an empty list named output_data to store the transformed data.

The script then iterates through each row of the input DataFrame (input_df) using a for loop. For each row, it extracts relevant information such as employee code, manager employee code, compensation, dates of joining, compensation adjustments, reviews, and engagements. These extracted details are then appended to the output_data list in a structured format.

After processing all rows in the input DataFrame, the script constructs a new DataFrame named output_df from the collected output_data. This DataFrame contains columns such as 'Employee Code', 'Manager Employee Code', 'Last Compensation', 'Compensation', 'Last Pay Raise Date', 'Variable Pay', 'Tenure in Org', 'Performance Rating', 'Engagement Score', 'Effective Date', and 'End Date'.

Subsequently, the script performs additional data manipulation tasks on the output_df DataFrame. It sorts the DataFrame based on 'Employee Code' and 'Effective Date' to ensure the records are ordered correctly. Missing values in specific columns (e.g., 'Last Pay Raise Date', 'Performance Rating', 'Engagement Score', 'Compensation') are filled forward within each employee group using the ffill() and bfill() functions.

The script then calculates the 'End Date' for each historical record by subtracting one day from the effective date of the next record. If a 'Date of Exit' is provided for an employee, the 'End Date' is updated accordingly.

Finally, the script sets certain fields to None based on specific conditions. For example, it sets 'Last Pay Raise Date', 'Performance Rating', and 'Engagement Score' to None under certain date conditions.

In conclusion, this script provides a systematic approach to process and transform employee-related data from an input CSV file to a structured output format, while adhering to certain conditions and assumptions outlined within the script.
