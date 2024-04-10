from datetime import datetime, timedelta
import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from Machines import Machines

# Define the data
mach2_day_times = [
    (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 13, 00, 0)),
    (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 15, 00, 0)),
    (datetime(2023, 4, 27, 6, 0, 0), datetime(2023, 4, 27, 13, 30, 0))
]
mach5_day_times = [
    (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 18, 30, 0)),
    (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 18, 30, 0)),
    (datetime(2023, 4, 27, 6, 0, 0), datetime(2023, 4, 27, 18, 30, 0)),
    (datetime(2023, 4, 28, 6, 0, 0), datetime(2023, 4, 28, 18, 30, 0))
]
mach6_day_times = [
    (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 18, 30, 0)),
    (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 18, 30, 0))
]
mach9_day_times = [
    (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 10, 30, 0))
]

# Combine all day times into one list
all_day_times = mach2_day_times + mach5_day_times + mach6_day_times + mach9_day_times

# Find the earliest start and latest end
earliest_start = min(start for start, _ in all_day_times)
latest_end = max(end for _, end in all_day_times)


print("Start: ", earliest_start)
print("End: ", latest_end)

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
        return sorted_data
    else:
        print("No file path returned by the Python program.")
        return None
if __name__ == "__main__":
    sorted_data = run_file_selection()  # Capture the returned sorted data
    if sorted_data is not None:
        BinPacking.main(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, earliest_start, latest_end, sorted_data)
    else:
        print("No sorted data returned. Exiting.")
