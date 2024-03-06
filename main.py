import pandas as pd

# Read input.csv
input_df = pd.read_csv('input.csv')

# Initialize an empty list to store the output data
output_data = []

# Iterate through each row in the input DataFrame
for index, row in input_df.iterrows():
    # Extract relevant information from the input row
    employee_code = row['Employee Code']
    manager_employee_code = row['Manager Employee Code']
    last_compensation = row['Compensation']
    date_of_joining = pd.to_datetime(row['Date of Joining'])
    compensation_date_1 = pd.to_datetime(row['Compensation 1 date'])
    compensation_date_2 = pd.to_datetime(row['Compensation 2 date'])

    # Add the initial record to the output data
    output_data.append([employee_code, manager_employee_code, last_compensation, None, None, None, None, None, None, date_of_joining, compensation_date_1])

    # Process Compensation 1
    if pd.notnull(row['Compensation 1']):
        output_data.append([employee_code, manager_employee_code, row['Compensation 1'], None, None, None, None, None, None, compensation_date_1, compensation_date_2])

    # Process Compensation 2
    if pd.notnull(row['Compensation 2']):
        if pd.notnull(row['Compensation 1 date']):
            last_compensation = row['Compensation 1']
        output_data.append([employee_code, manager_employee_code, row['Compensation 2'], None, None, None, None, None, None, compensation_date_2, '2021-02-28'])

    # Process Reviews
    for i in range(1, 3):
        review_col = f'Review {i}'
        review_date_col = f'Review {i} date'

        # Process Reviews
        if pd.notnull(row[review_col]):
            output_data.append([employee_code, manager_employee_code, last_compensation, None, None, None, None, row[review_col], None, row[review_date_col], '2021-05-31'])

    # Process Engagements
    for i in range(1, 3):
        engagement_col = f'Engagement {i}'
        engagement_date_col = f'Engagement {i} date'

        if pd.notnull(row[engagement_col]):
            output_data.append([employee_code, manager_employee_code, last_compensation, None, None, None, None, None, row[engagement_col], row[engagement_date_col], '2021-12-30'])

# Create the output DataFrame
output_df = pd.DataFrame(output_data, columns=['Employee Code', 'Manager Employee Code', 'Last Compensation', 'Compensation', 'Last Pay Raise Date', 'Variable Pay', 'Tenure in Org', 'Performance Rating', 'Engagement Score', 'Effective Date', 'End Date'])

# Convert 'Effective Date' and 'End Date' columns to datetime objects
output_df['Effective Date'] = pd.to_datetime(output_df['Effective Date'])
output_df['End Date'] = pd.to_datetime(output_df['End Date'])

# Sort DataFrame by 'Employee Code' and 'Effective Date'
output_df.sort_values(['Employee Code', 'Effective Date'], inplace=True)

# Fill forward missing values for specific columns
columns_to_fill = ['Last Pay Raise Date', 'Performance Rating', 'Engagement Score', 'Compensation']
for col in columns_to_fill:
    output_df[col] = output_df.groupby('Employee Code')[col].transform(lambda x: x.ffill().bfill())

# Calculate 'End Date' for each historical record
output_df['End Date'] = output_df.groupby('Employee Code')['Effective Date'].shift(-1) - pd.DateOffset(1)
output_df['End Date'] = output_df['End Date'].fillna(pd.to_datetime('2100-01-01'))

# Update 'End Date' with 'Date of Exit' if available
for index, row in input_df.iterrows():
    exit_date = pd.to_datetime(row['Date of Exit'])
    if pd.notnull(exit_date):
        employee_code = row['Employee Code']
        exit_mask = (output_df['Employee Code'] == employee_code) & (output_df['End Date'] == pd.to_datetime('2100-01-01'))
        output_df.loc[exit_mask, 'End Date'] = exit_date

# Set 'Last Pay Raise Date', 'Performance Rating', 'Engagement Score' to None for specific conditions
condition_mask_1 = (output_df['Effective Date'] == pd.to_datetime('2021-01-01')) & (output_df['End Date'] == pd.to_datetime('2021-02-28'))
condition_mask_2 = (output_df['Effective Date'] == pd.to_datetime('2021-03-01')) & (output_df['End Date'] == pd.to_datetime('2021-05-31'))

output_df.loc[condition_mask_1, ['Last Pay Raise Date', 'Performance Rating', 'Engagement Score']] = None
output_df.loc[condition_mask_2, 'Performance Rating'] = None

# Write the output DataFrame to output.csv
output_df.to_csv('output.csv', index=False)