import os

from datetime import datetime, timedelta
import os
import pandas as pd
from FileSelection import FileSelection
from BinPacking import BinPacking
from Machines import Machines
from SimilaritySwap import SimilaritySwap
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkcalendar import DateEntry
from PIL import ImageTk, Image
import Output
import sys

sorted_data = None
mach2_day_time = []
mach5_day_times = []
mach6_day_times = []
mach9_day_times = []
earliest_start = None
latest_end = None

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
            file_name_label.config(text="")
            createButton.config(state=tk.DISABLED)

            
    def click_create_schedule_button(start_date_entry, end_date_entry):
        global mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, earliest_start, latest_end

        # Get the selected dates from the DateEntry widgets
        start_date = start_date_entry.get_date()
        end_date = end_date_entry.get_date()

        earliest_start = start_date
        latest_end = end_date
        
        # Update the time intervals for each machine
        mach2_day_times = create_time_intervals(start_date, end_date)
        mach5_day_times = create_time_intervals(start_date, end_date)
        mach6_day_times = create_time_intervals(start_date, end_date)
        mach9_day_times = create_time_intervals(start_date, end_date)

        # Print the selected dates
        print("Start Date:", start_date)
        print("End Date:", end_date)
        
        global sorted_data
        global output_save_path
        print("Running BinPacking Method")
        if sorted_data is not None:
            machines_orig = BinPacking.main(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, earliest_start, latest_end, sorted_data)
            print("---------- SOLUTION-0 --------------")
            for m in range (1, 5):
                machine_jobs = machines_orig.get_assigned_job_nums(m)
                if m == 1:
                    print("\nMachine 2\n")
                elif m == 2:
                    print("\nMachine 5\n")
                elif m == 3:
                    print("\nMachine 6\n")
                elif m == 4:
                    print("\nMachine 9\n")
                for j in range(len(machine_jobs)):
                    jobObj = machines_orig.jobs_assigned[m]
                    print("Job: ", machine_jobs[j], " | StartTime -> ", machines_orig.get_assigned_job_start(m, jobObj[j]), " | EndTime -> ", machines_orig.get_assigned_job_end(m, jobObj[j]))
            FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs = SimilaritySwap.create(machines_orig)
            Mach2_New_Order, Mach5_New_Order, Mach6_New_Order, Mach9_New_Order = SimilaritySwap.job_reorder(FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs)
            machines_alt = SimilaritySwap.time_assignment(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, Mach2_New_Order, Mach5_New_Order, Mach6_New_Order, Mach9_New_Order)
            print("---------- SOLUTION-1 --------------")
            for m in range (1, 5):
                machine_jobs = machines_alt.get_assigned_job_nums(m)
                if m == 1:
                    print("\nMachine 2\n")
                    mach2_timeslot_table = machines_alt.generate_timeslot_table_for_machine(m)
                    print(mach2_timeslot_table)
                elif m == 2:
                    print("\nMachine 5\n")
                    mach5_timeslot_table = machines_alt.generate_timeslot_table_for_machine(m)
                    print(mach5_timeslot_table)
                elif m == 3:
                    print("\nMachine 6\n")
                    mach6_timeslot_table = machines_alt.generate_timeslot_table_for_machine(m)
                    print(mach6_timeslot_table)
                elif m == 4:
                    print("\nMachine 9\n")
                    mach9_timeslot_table = machines_alt.generate_timeslot_table_for_machine(m)
                    print(mach9_timeslot_table)
                for j in range(len(machine_jobs)):
                    jobObj = machines_alt.jobs_assigned[m]
                    print("Job: ", machine_jobs[j], " | StartTime -> ", machines_alt.get_assigned_job_start(m, jobObj[j]), " | EndTime -> ", machines_alt.get_assigned_job_end(m, jobObj[j]))
            machines_os = SimilaritySwap.comparison(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, machines_orig, machines_alt, latest_end)
            print("---------- FINAL SOLUTION --------------")
            for m in range (1, 5):
                machine_jobs = machines_os.get_assigned_job_nums(m)
                if m == 1:
                    print("\nMachine 2\n")
                    mach2_timeslot_table = machines_os.generate_timeslot_table_for_machine(m)
                    print(mach2_timeslot_table)
                elif m == 2:
                    print("\nMachine 5\n")
                    mach5_timeslot_table = machines_os.generate_timeslot_table_for_machine(m)
                    print(mach5_timeslot_table)
                elif m == 3:
                    print("\nMachine 6\n")
                    mach6_timeslot_table = machines_os.generate_timeslot_table_for_machine(m)
                    print(mach6_timeslot_table)
                elif m == 4:
                    print("\nMachine 9\n")
                    mach9_timeslot_table = machines_os.generate_timeslot_table_for_machine(m)
                    print(mach9_timeslot_table)
                for j in range(len(machine_jobs)):
                    jobObj = machines_os.jobs_assigned[m]
                    print("Job: ", machine_jobs[j], " | StartTime -> ", machines_os.get_assigned_job_start(m, jobObj[j]), " | EndTime -> ", machines_os.get_assigned_job_end(m, jobObj[j]))
            materials_table = machines_os.generate_materials_list()

            # Format the datetime object as per your requirement
            fileroot = "MachineSchedule_"
            formatted_date = earliest_start.strftime("%Y_%B_%d")

            # filename = "sample_table.xlsx"
            filename = fileroot + formatted_date + ".xlsx"
            try:
                output_save_path = choose_save_directory()
                Output.create_table(output_save_path, filename, mach2_timeslot_table, mach5_timeslot_table, mach6_timeslot_table, mach9_timeslot_table)
                Output.modify_workbook(output_save_path, filename, materials_table)
            except Exception as e:
                # show_message_box("Error", str(e))
                show_message_box("Error", "Please select another file.\nExcel files (.xlsx) only.\nFile must be in correct format.")
                print("Please select a directory to save output file")

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

    # Container frame to page components
    date_container = tk.Frame(frame, bg="white")
    date_container.grid(row=2, column=0, padx=10, pady=10)

    # start date label
    start_label = tk.Label(date_container, text="Start Date: ", bg="white")
    start_label.grid(row=0, column=0, padx=30, pady=10)

    # DateEntry widget for start date
    start_date_entry = DateEntry(date_container, background='skyblue', foreground='black', borderwidth=2)
    start_date_entry.grid(row=0, column=1, padx=10, pady=5)

    # end date label
    end_label = tk.Label(date_container, text="End Date", bg="white")
    end_label.grid(row=1, column=0, padx=30, pady=5)

    # DateEntry widget for end date
    end_date_entry = DateEntry(date_container, background='skyblue', foreground='black', borderwidth=2)
    end_date_entry.grid(row=1, column=1, padx=10, pady=10)

    # create the file name label
    file_name_label = tk.Label(frame, text="", bg="white", height=2)
    file_name_label.grid(row=1, column=0, padx=5, pady=0)

    # create the file selection button
    if sys.platform == "win32":
        fileSelectionButton = tk.Button(date_container, text="File Selection", width=15, height=2, command=click_file_selection_button)
    elif sys.platform == "darwin":
        fileSelectionButton = tk.Button(date_container, text="File Selection", width=10, height=2, command=click_file_selection_button)
    fileSelectionButton.grid(row=0, column=2, padx=5, pady=5)

    # create the create schedule button
    if sys.platform == "win32":
        createButton = tk.Button(date_container, text="Create Schedule", width=15, height=2, command=lambda: click_create_schedule_button(start_date_entry, end_date_entry))
    elif sys.platform == "darwin":
        createButton = tk.Button(date_container, text="Create Schedule", width=10, height=2, command=lambda: click_create_schedule_button(start_date_entry, end_date_entry))
    createButton.grid(row=1, column=2, padx=5, pady=5)
    createButton.config(state=tk.DISABLED)

    # center the frame in the window
    frame.pack_propagate(False)
    frame.place(relx=0.5, rely=0.5, anchor="center")
    frame.configure(bg="white")

    # check the window status
    check_window_status(root)

    # runs window
    root.mainloop()

def FileSelectionPage(parent):
    def back_to_main_menu():
        parent.show()
        frame.destroy()
    
    frame = tk.Frame(parent)
    frame.pack(expand=True)

    back_button = tk.Button(frame, text="Return to Main Menu", command=back_to_main_menu)
    back_button.pack()

    # center the frame in the window
    frame.pack_propagate(False)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    parent.mainloop()

# file selection method
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

def create_time_intervals(earliest_start, latest_end):
    # Define the list of weekdays
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Initialize the list to store time intervals
    time_intervals = []

    # Iterate over the days between earliest_start and latest_end
    current_date = earliest_start
    while current_date <= latest_end:
        # Get the day of the week for the current date
        day_of_week = weekdays[current_date.weekday()]
        
        # Skip Fridays, Saturdays and Sundays
        if day_of_week in ['Friday', 'Saturday', 'Sunday']:
            current_date += timedelta(days=1)
            continue

        # Determine the start and end times based on the day of the week
        start_time = datetime(current_date.year, current_date.month, current_date.day, 6, 0, 0)
        end_time = datetime(current_date.year, current_date.month, current_date.day, 2, 0, 0) + timedelta(days=1)
        
        # Append the time interval to the list
        time_intervals.append((start_time, end_time))
        
        # Move to the next day
        current_date += timedelta(days=1)
    
    return time_intervals

def choose_save_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select a directory
    output_save_path = filedialog.askdirectory()

    return output_save_path
    
    
# Main method
if __name__ == "__main__":
    MainMenu()