from datetime import datetime, timedelta
import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from UrgencyList import UrgencyList

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
        
        # Start & End dates for production week
        start_date = datetime(2023, 4, 24, 6, 0, 0)
        end_date = datetime(2023, 4, 30, 18, 30, 0)

        print("Start Date:", start_date)
        print("End Date:", end_date)

        # Create an instance of UrgencyList
        urgency_list = UrgencyList()

        # Call the create method
        urgency_list.create(start_date, end_date, sorted_data)

        # Access and print jobs in each urgency list
        print("Attainable Jobs:")
        for job in urgency_list.UL_Attainable.values():
            print("Job Num:", job.get_Job_Num())

        print("\nOverdue Attainable Jobs:")
        for job in urgency_list.UL_Overdue_Attainable.values():
            print("Job Num:", job.get_Job_Num())

        print("\nUnattainable Jobs:")
        for job in urgency_list.UL_Unattainable.values():
            print("Job Num:", job.get_Job_Num())

        print("\nOverdue Unattainable Jobs:")
        for job in urgency_list.UL_Overdue_Unattainable.values():
            print("Job Num:", job.get_Job_Num())

        print("\nOther Jobs:")
        for job in urgency_list.UL_Other.values():
            print("Job Num:", job.get_Job_Num())
        
    else:
        print("No file path returned by the Python program.")

if __name__ == "__main__":
    run_file_selection()
