from datetime import datetime, timedelta
import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from Machines import Machines
from SimilaritySwap import SimilaritySwap
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image

# ------------- This section will be resolved to a separate method w/ user input later on
# Define the data
mach2_day_times = [
    # Week4
    # (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    # (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 13, 00, 0)),
    # (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 15, 00, 0)),
    # (datetime(2023, 4, 27, 6, 0, 0), datetime(2023, 4, 27, 13, 30, 0))
    # Week3
    # (datetime(2023, 4, 10, 6, 0, 0), datetime(2023, 4, 10, 18, 30, 0)),
    # (datetime(2023, 4, 11, 6, 0, 0), datetime(2023, 4, 11, 18, 30, 0)),
    # (datetime(2023, 4, 12, 6, 0, 0), datetime(2023, 4, 12, 18, 30, 0)),
    # (datetime(2023, 4, 13, 6, 0, 0), datetime(2023, 4, 13, 18, 30, 0)),
    # (datetime(2023, 4, 14, 6, 0, 0), datetime(2023, 4, 14, 18, 30, 0))
    # Week2
    (datetime(2023, 4, 3, 6, 0, 0), datetime(2023, 4, 3, 18, 30, 0)),
    (datetime(2023, 4, 4, 6, 0, 0), datetime(2023, 4, 4, 18, 30, 0)),
    (datetime(2023, 4, 5, 6, 0, 0), datetime(2023, 4, 5, 18, 30, 0)),
    (datetime(2023, 4, 6, 6, 0, 0), datetime(2023, 4, 6, 18, 30, 0))
]
mach5_day_times = [
    # Week4
    # (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    # (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 18, 30, 0)),
    # (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 18, 30, 0)),
    # (datetime(2023, 4, 27, 6, 0, 0), datetime(2023, 4, 27, 18, 30, 0)),
    # (datetime(2023, 4, 28, 6, 0, 0), datetime(2023, 4, 28, 18, 30, 0))
    # Week3
    # (datetime(2023, 4, 10, 6, 0, 0), datetime(2023, 4, 10, 18, 30, 0)),
    # (datetime(2023, 4, 11, 6, 0, 0), datetime(2023, 4, 11, 18, 30, 0)),
    # (datetime(2023, 4, 12, 6, 0, 0), datetime(2023, 4, 12, 18, 30, 0)),
    # (datetime(2023, 4, 13, 6, 0, 0), datetime(2023, 4, 13, 18, 30, 0)),
    # (datetime(2023, 4, 14, 6, 0, 0), datetime(2023, 4, 14, 18, 30, 0))
    # Week2
    (datetime(2023, 4, 3, 6, 0, 0), datetime(2023, 4, 3, 18, 30, 0)),
    (datetime(2023, 4, 4, 6, 0, 0), datetime(2023, 4, 4, 18, 30, 0)),
    (datetime(2023, 4, 5, 6, 0, 0), datetime(2023, 4, 5, 18, 30, 0)),
    (datetime(2023, 4, 6, 6, 0, 0), datetime(2023, 4, 6, 18, 30, 0))
]
mach6_day_times = [
    # Week4
    # (datetime(2023, 4, 24, 6, 0, 0), datetime(2023, 4, 24, 18, 30, 0)),
    # (datetime(2023, 4, 25, 6, 0, 0), datetime(2023, 4, 25, 18, 30, 0)),
    # (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 18, 30, 0))
    # Week3
    # (datetime(2023, 4, 10, 6, 0, 0), datetime(2023, 4, 10, 18, 30, 0)),
    # (datetime(2023, 4, 11, 6, 0, 0), datetime(2023, 4, 11, 18, 30, 0)),
    # (datetime(2023, 4, 12, 6, 0, 0), datetime(2023, 4, 12, 18, 30, 0)),
    # (datetime(2023, 4, 13, 6, 0, 0), datetime(2023, 4, 13, 18, 30, 0)),
    # (datetime(2023, 4, 14, 6, 0, 0), datetime(2023, 4, 14, 18, 30, 0))
    # Week2
    (datetime(2023, 4, 3, 6, 0, 0), datetime(2023, 4, 3, 18, 30, 0)),
    (datetime(2023, 4, 4, 6, 0, 0), datetime(2023, 4, 4, 18, 30, 0)),
    (datetime(2023, 4, 5, 6, 0, 0), datetime(2023, 4, 5, 18, 30, 0)),
    (datetime(2023, 4, 6, 6, 0, 0), datetime(2023, 4, 6, 18, 30, 0))
]
mach9_day_times = [
    # Week4
    # (datetime(2023, 4, 26, 6, 0, 0), datetime(2023, 4, 26, 10, 30, 0))
    # Week3
    # (datetime(2023, 4, 10, 6, 0, 0), datetime(2023, 4, 10, 18, 30, 0)),
    # (datetime(2023, 4, 11, 6, 0, 0), datetime(2023, 4, 11, 10, 30, 0)),
    # (datetime(2023, 4, 12, 6, 0, 0), datetime(2023, 4, 12, 18, 30, 0)),
    # (datetime(2023, 4, 13, 6, 0, 0), datetime(2023, 4, 13, 18, 30, 0)),
    # (datetime(2023, 4, 14, 6, 0, 0), datetime(2023, 4, 14, 18, 30, 0))
    # Week2
    (datetime(2023, 4, 3, 6, 0, 0), datetime(2023, 4, 3, 16, 0, 0)),
    (datetime(2023, 4, 4, 6, 0, 0), datetime(2023, 4, 4, 18, 30, 0)),
    (datetime(2023, 4, 5, 6, 0, 0), datetime(2023, 4, 5, 18, 30, 0)),
    (datetime(2023, 4, 6, 6, 0, 0), datetime(2023, 4, 6, 18, 30, 0))
]
# Combine all day times into one list
all_day_times = mach2_day_times + mach5_day_times + mach6_day_times + mach9_day_times
# Find the earliest start and latest end
earliest_start = min(start for start, _ in all_day_times)
latest_end = max(end for _, end in all_day_times)

# print("Start: ", earliest_start)
# print("End: ", latest_end)

sorted_data = None

#---------------------- End of Section --------------------
# method to test if GUI window is open, quit if not open
def check_window_status(window):
    def on_closing():
        print("Window is closed.")
        window.quit()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    print("Window is open")

def MainMenu():
    def show_message_box(title, message):
        messagebox.showinfo(title, message)

    def click_file_selection_button():
        global sorted_data
        print("Choosing File")
        try:
            selected_file_path, sorted_data = run_file_selection()
            print("Python program selected file path:", selected_file_path)
             # Extract file name from file path
            file_name = os.path.basename(selected_file_path)
            file_name_label.config(text="Selected File: " + file_name)  
            createButton.config(state=tk.NORMAL)
        except Exception as e:
            # show_message_box("Error", str(e))
            show_message_box("Error", "Please select another file.\nExcel files (.xlsx) only.\nFile must be in correct format.")
            print("Please select an Excel file")
            
    def click_create_schedule_button():
        global sorted_data
        print("Running BinPacking Method")
        if sorted_data is not None:
            machines = BinPacking.main(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, earliest_start, latest_end, sorted_data)
            print("jobs on machine 2: ", machines.get_assigned_job_nums(1))
            print("jobs on machine 5: ", machines.get_assigned_job_nums(2))
            print("jobs on machine 6: ", machines.get_assigned_job_nums(3))
            print("jobs on machine 9: ", machines.get_assigned_job_nums(4))

            for m in range (1, 5):
                machine_jobs = machines.get_assigned_job_nums(m)
                if m == 1:
                    print("\nMachine 2\n")
                elif m == 2:
                    print("\nMachine 5\n")
                elif m == 3:
                    print("\nMachine 6\n")
                elif m == 4:
                    print("\nMachine 9\n")
                for j in range(len(machine_jobs)):
                    jobObj = machines.jobs_assigned[m]
                    print("Job: ", machine_jobs[j], " | StartTime -> ", machines.get_assigned_job_start(m, jobObj[j]), " | EndTime -> ", machines.get_assigned_job_end(m, jobObj[j]))
            # exit(0)
            FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs = SimilaritySwap.create(machines)
            SimilaritySwap.reorder(FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs, 1)

        else:
            print("No sorted data returned. Exiting.")
        
    # sets sorted_data as a global variable
    global sorted_data

    # creates a tkinter GUI window
    root = tk.Tk()
    root.title("Wepco Plastics Job Scheduling Software")
    root.configure(bg="white")

    # disable window resizing
    root.resizable(False, False)

    image = Image.open("Resources/WepcoLogo.png")
    photo = ImageTk.PhotoImage(image)

    # set window dimensions
    root.minsize(700, 500)
    root.maxsize(700, 500)

    # create a frame to hold Main Menu components
    frame = tk.Frame(root)
    frame.pack(expand=True)

    # create the image label
    image_label = tk.Label(frame, image=photo)
    image_label.grid(row=0, column=0, padx=5, pady=5)
    image_label.configure(bg="white")

    # create the file name label
    file_name_label = tk.Label(frame, text="", bg="white", height=2)
    file_name_label.grid(row=1, column=0, padx=5, pady=(5,0))

    # create the file selection button
    fileSelectionButton = tk.Button(frame, text="File Selection", width=10, height=2, command=click_file_selection_button)
    fileSelectionButton.grid(row=2, column=0, padx=5, pady=(10,5))

    # create the create schedule button
    createButton = tk.Button(frame, text="Create Schedule", width=10, height=2, command=click_create_schedule_button)
    createButton.grid(row=3, column=0, padx=5, pady=5)
    createButton.config(state=tk.DISABLED)

    # center the frame in the window
    frame.pack_propagate(False)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.configure(bg="white")

    # check the window status
    check_window_status(root)

    # runs window
    root.mainloop()


# Call File Selection
def run_file_selection():
    file_selector = FileSelection()
    selected_file_path = file_selector.main()
    global sorted_data
    if selected_file_path:
        # Read Excel file & Sort based on job status
        raw_data = pd.read_excel(selected_file_path, "TempQueryName")
        sorted_data = raw_data.query('Completed == "Received" or Completed == "Not Started"')
        sorted_data = sorted_data.sort_values(by=['due_date'])
        return selected_file_path, sorted_data
    else:
        print("No file path returned by the Python program.")
        return None, None
    
# Main method
if __name__ == "__main__":
    MainMenu()