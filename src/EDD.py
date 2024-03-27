import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from JobAdd import JobAdd

# Call File Selection
def run_file_selection():
    file_selector = FileSelection()
    selected_file_path = file_selector.main()

    if selected_file_path:
        print("Python program selected file path:", selected_file_path)

        # Read Excel file & Sort based on job status
        raw_data = pd.read_excel(selected_file_path, "TempQueryName")
        sorted_data = raw_data.query('Completed == "Received" or Completed == "Not Started"')
        sorted_data = sorted_data.sort_values(by=['due_date'])

        # Calls Bin Packing
        BinPacking.SortUrgencyList(sorted_data)

        # Calls Job Add: Sorting into Urgency Lists
        # JobAdd.SortUrgencyList(sorted_data)

        # Call the SortUrgencyList function and store the returned variables
        start_date, end_date, UL_Attainable, UL_Unattainable, UL_Overdue_Attainable, UL_Overdue_Unattainable, OtherList = JobAdd.SortUrgencyList(sorted_data)

        # Call the JobAssignment function with the returned variables
        JobAdd.JobAssignment(start_date, end_date, UL_Attainable, UL_Unattainable, UL_Overdue_Attainable, UL_Overdue_Unattainable, OtherList)



    else:
        print("No file path returned by the Python program.")

if __name__ == "__main__":
    run_file_selection()
