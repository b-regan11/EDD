import os
import subprocess
import pandas as pd
import datetime


# Compile & Run the Java class (File Selection)
subprocess.run(['javac', 'FileSelection/FileSelection.java'])

# Run the Java class and capture the standard output
result = subprocess.run(['java', 'FileSelection/FileSelection'], stdout=subprocess.PIPE, text=True)

# Check if the Java program ran successfully
if result.returncode == 0:
    # Access the standard output of the Java program
    java_output = result.stdout

    # Process or extract the file path from the Java output
    lines = java_output.splitlines()
    if lines:
        selected_file_path = lines[-1].strip()  # Assuming the file path is the last line of output
        print("Java program selected file path:", selected_file_path)

        # Extract only the file path from the message
        prefix = "You chose to open this file: "
        if selected_file_path.startswith(prefix):
            selected_file_path = selected_file_path[len(prefix):]
        
        # Read Excel file & Sort based on job status
        raw_data = pd.read_excel(selected_file_path,"TempQueryName")
        sorted_data = raw_data.query('Completed == "Received" or Completed == "Not Started"') # This is only sorting for status, not date
        sorted_data = sorted_data.sort_values(by=['due_date'])
        print(sorted_data)
        
        # Start & End dates for production week
        start_date = '2023-4-24' # datetime.date(2023,4,24)
        end_date = '2023-4-30' # datetime.date(2023,4,30)         #both of these should be user input later on

        # Urgency List for Job Priorities
        UrgencyList = sorted_data[(sorted_data['due_date'] >= start_date) & (sorted_data['due_date'] <= end_date)]
        UL_Attainable = UrgencyList.query('production_hrs <= 25') # 1
        UL_Unattainable = UrgencyList.query('production_hrs > 25') # 3
        UrgencyList = sorted_data[(sorted_data['due_date'] > '2020-1-01') & (sorted_data['due_date'] < start_date)]
        UL_Overdue_Attainable = UrgencyList.query('production_hrs <= 25') # 2
        UL_Overdue_Unattainable = UrgencyList.query('production_hrs > 25') # 4
        OtherList = sorted_data[(sorted_data['due_date'] > end_date) & (sorted_data['due_date'] < '2099-1-01')] # 5

        print(UL_Attainable)
        print(UL_Overdue_Attainable)
        print(UL_Unattainable)
        print(UL_Overdue_Unattainable)
        print(OtherList)

        # Tiered Tie Breakers Implementation

    else:
        print("No file path returned by the Java program.")

# def BinPacking(data):