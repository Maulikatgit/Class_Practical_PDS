# Date    :  2024-07-31 22:34
# Author  : Parmar Maulik (mm.2004.parmar@gmail.com)
# GitHub    : (https://github.com/Maulikatgit)
# Twitter    : (https://twitter.com/Mr_younglord)
# Version : 1.0.0

import pandas as pd

# Load the cvs file
try:
    df = pd.read_csv('/home/maulik/Downloads/heart_2020_cleaned.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found.")
    exit()

# Display basic information about the data
print("\nDataset Info:")
print(df.info())

print("\nFirst few rows of the dataset:")
print(df.head())

# Cleaning the raw data
numerical_cols = df.select_dtypes(include=['number']).columns
print("\nNumerical columns in the dataset:")
print(numerical_cols)

# print measures of central
print("\nMeasures of Central Tendency:")
for col in numerical_cols:
    print(f"\nColumn: {col}")
    print(f"Mean: {df[col].mean()}")   #find Mean
    print(f"Median: {df[col].median()}")    # find Median
    print(f"Mode:\n{df[col].mode().values}")    # find Mode

# print measures of dispersion/variation
print("\nMeasures of Dispersion/Variation:")
for col in numerical_cols:
    print(f"\nColumn: {col}")
    print(f"Range: {df[col].max() - df[col].min()}")  # find Range
    print(f"Variance: {df[col].var()}")     # find Variance
    print(f"Standard Deviation: {df[col].std()}")   # find SD

# print measures of location
print("\nMeasures of Location:")
for col in numerical_cols:
    print(f"\nColumn: {col}")
    print(f"Quartiles:\n{df[col].quantile([0.25, 0.5, 0.75])}")
    print(f"Inter quartile Range (IQR): {df[col].quantile(0.75) - df[col].quantile(0.25)}")

# print measures of shape and symmetry
print("\nMeasures of Shape and Symmetry:")
for col in numerical_cols:
    print(f"\nColumn: {col}")
    print(f"Skewness: {df[col].skew()}")
    print(f"Kurtosis: {df[col].kurtosis()}")
