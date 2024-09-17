import pandas as pd

excel_file = "E:\\jai.xlsx"

def write_excel(file_name, data):
    df = pd.DataFrame(data)  # Convert data to a DataFrame
    df.to_excel(file_name, index=False)  # Write DataFrame to an Excel file
    print(f"Data written to {file_name}")

def read_excel(file_name):
    df = pd.read_excel(file_name)  # Read the Excel file into a DataFrame
    print(df)  # Print the DataFrame

# Example usage:
students = [
    {"name": "Utkarsh Jaiswal", "college": "ITS University", "address": "1 sector-15 Vasundhara"},
    {"name": "Jane Smith", "college": "ABC College", "address": "456 Oak St"}
]

write_excel(excel_file, students)
read_excel(excel_file)
