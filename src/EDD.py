from datetime import datetime, timedelta
import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from Machines import Machines

# Define the data
mach2_day_times = [
    (datetime(2024, 3, 22, 5, 0, 0), datetime(2024, 3, 22, 18, 30, 0)),
    (datetime(2024, 3, 23, 6, 0, 0), datetime(2024, 3, 23, 10, 30, 0)),
    (datetime(2024, 3, 24, 14, 0, 0), datetime(2024, 3, 24, 18, 30, 0))
]
mach5_day_times = [
    (datetime(2024, 3, 22, 6, 0, 0), datetime(2024, 3, 22, 18, 30, 0)),
    (datetime(2024, 3, 23, 6, 0, 0), datetime(2024, 3, 23, 10, 30, 0)),
    (datetime(2024, 3, 23, 14, 0, 0), datetime(2024, 3, 23, 18, 30, 0))
]
mach6_day_times = [
    (datetime(2024, 3, 22, 6, 0, 0), datetime(2024, 3, 22, 18, 30, 0)),
    (datetime(2024, 3, 23, 6, 0, 0), datetime(2024, 3, 23, 10, 30, 0)),
    (datetime(2024, 3, 23, 14, 0, 0), datetime(2024, 3, 23, 18, 30, 0))
]
mach9_day_times = [
    (datetime(2024, 3, 22, 6, 0, 0), datetime(2024, 3, 22, 18, 30, 0)),
    (datetime(2024, 3, 23, 6, 0, 0), datetime(2024, 3, 23, 10, 30, 0)),
    (datetime(2024, 3, 23, 14, 0, 0), datetime(2024, 3, 24, 18, 30, 0))
]

# Combine the data into a list
machines_day_times = [
    mach2_day_times,
    mach5_day_times,
    mach6_day_times,
    mach9_day_times
]

# # Find the earliest start and latest end
earliest_start = None
latest_end = None

for day_times in machines_day_times:
    for start, end in day_times:
        if earliest_start is None or start < earliest_start:
            earliest_start = start
        if latest_end is None or end > latest_end:
            latest_end = end

# # Print the results
print("Earliest start:", earliest_start)
print("Latest end:", latest_end)

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
        
        # # Start & End dates for production week
        # start_date = datetime(2023, 4, 24, 6, 0, 0)
        # end_date = datetime(2023, 4, 30, 18, 30, 0)

        # print("Start Date:", start_date)
        # print("End Date:", end_date)

        #BinPacking.main(earliest_start, latest_end, sorted_data)

        machines = Machines()
        machines.create(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times)
        
    else:
        print("No file path returned by the Python program.")

if __name__ == "__main__":
    run_file_selection()
    # This is where everything should be called in the final product
