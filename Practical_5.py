# Date    :  2024-08-01 09:44
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Linkedin    : (https://www.linkedin.com/in/maulik-parmar-659284218/)
# Version : 1.0.0

import pandas as pd
import numpy as np

# Create an array “rank” with 5 element(rank1,rank2,…,rank5)
rank = ['rank1', 'rank2', 'rank3', 'rank4', 'rank5']

# Create and display a DataFrame “exam” from a specified dictionary “exam_data_array”
exam_data_array = {
    'Name': ['Maulik', 'Vivek', 'Nevil', 'Prasham', 'Shrey'],
    'Score': [18, 22, 14, 19, 16],
    'Qualify': ['yes', 'no', 'yes', 'yes', 'no'],
    'Attempts': [1, 3, 2, 1, 2]
}
# Create the DataFrame
exam = pd.DataFrame(exam_data_array, index=rank)

# display a summary of basic information and its data.
print("DataFrame 'exam':")
print(exam)

# Select the rows where the score is between 15 and 20 (inclusive).
filtered_scores = exam[(exam['Score'] >= 15) & (exam['Score'] <= 20)]
print("\nRows where the Score is between 15 and 20 (inclusive):")
print(filtered_scores)

# Sort the data first by “score” in ascending order , then by “name” in descending order.
sorted_exam = exam.sort_values(by=['Score', 'Name'], ascending=[True, False])
print("\nSorted DataFrame by 'Score' (ascending) and 'Name' (descending):")
print(sorted_exam)

# Replace the 'yes' and 'no' values from column “qualify” with True and False
exam['Qualify'] = exam['Qualify'].map({'yes': True, 'no': False})
print("\nDataFrame with 'Qualify' values replaced with True and False:")
print(exam)

# Display specified columns(columns: 2 and 4) and rows(row: 1,3 and 5).
specified_data = exam.iloc[[0, 2, 4], [1, 3]]
print("\nSpecified Columns and Rows:")
print(specified_data)

# Select the rows where number of attempts in the examination is < 2 and > 15.
filtered_attempts = exam[(exam['Attempts'] < 2) & (exam['Score'] > 15)]
print("\nRows with Attempts < 2 and Score > 15:")
print(filtered_attempts)

# Change the name 'James' to 'Suresh' in “name” column of the data frame.
exam['Name'] = exam['Name'].replace('Vivek', 'Suresh')
print("\nDataFrame with 'Vivek' changed to 'Suresh' in 'Name' column:")
print(exam)

# Calculate the sum of the examination attempts by the students.
total_attempts = exam['Attempts'].sum()
print("\nSum of Examination Attempts by Students:")
print(total_attempts)

# Append one row
new_row = pd.DataFrame({'Name': ['Raj'], 'Score': [20], 'Qualify': [True], 'Attempts': [1]}, index=['rank6'])
exam = exam._append(new_row)
print("\nDataFrame after Appending a New Row:")
print(exam)

# Insert a new column “exam_name” and then Delete the ”exam_name” column.
exam['exam_name'] = 'Midterm Exam'
print("\nDataFrame with New 'exam_name' Column:")
print(exam)

exam = exam.drop(columns=['exam_name'])
print("\nDataFrame after Deleting 'exam_name' Column:")
print(exam)

# Convert a NumPy array to a Series
numpy_array = np.array([1, 2, 3, 4, 5])
series_from_array = pd.Series(numpy_array)
print("\nSeries from NumPy Array:")
print(series_from_array)

# Convert a dictionary to a Series
dict_data = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(series_from_dict)

# Convert the first column of the DataFrame to a Series
first_column_series = exam['Name']
print("\nSeries from First Column of DataFrame:")
print(first_column_series)

