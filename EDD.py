import os
import subprocess
import pandas as pd
import openpyxl
import datetime
from BinPacking import BinPacking_UrgencyList

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
        
        BinPacking_UrgencyList.UrgencyList(sorted_data)

        # Tiered Tie Breakers Implementation

    else:
        print("No file path returned by the Java program.")
