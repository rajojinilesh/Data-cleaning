import pandas as pd

# Load the dataset
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# --- Data Cleaning Steps ---

# 1. Handle Missing Values
# For numerical columns, fill with the mean
for col in df.select_dtypes(include=['number']).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# For categorical columns, fill with the mode
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# 2. Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# 3. Standardize Text Values (example for 'Marital_Status')
if 'Marital_Status' in df.columns:
    df['Marital_Status'] = df['Marital_Status'].str.lower()

# 4. Convert Date Formats
if 'Dt_Customer' in df.columns:
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], dayfirst=True).dt.strftime('%d-%m-%Y')

# 5. Clean Column Headers
df.columns = df.columns.str.lower().str.replace(' ', '_')

# 6. Check and Fix Data Types
if 'income' in df.columns:
    df['income'] = df['income'].astype(int)

# --- Summary of Changes ---
summary = """
Data Cleaning and Preprocessing Summary:
1.  **Handled Missing Values:** Filled missing numerical data with the column mean and categorical data with the mode.
2.  **Removed Duplicates:** Dropped all duplicate rows from the dataset.
3.  **Standardized Text:** Converted text in 'Marital_Status' to lowercase.
4.  **Formatted Dates:** Standardized the 'Dt_Customer' column to DD-MM-YYYY format.
5.  **Cleaned Column Headers:** Converted all column headers to lowercase with underscores instead of spaces.
6.  **Corrected Data Types:** Ensured the 'income' column is of integer type.
"""

print(summary)

# Save the cleaned dataset
df.to_csv('cleaned_marketing_campaign.csv', index=False)

print("Data cleaning complete. Cleaned file saved as 'cleaned_marketing_campaign.csv'")