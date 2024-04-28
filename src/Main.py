import tkinter as tk
import tkinter.messagebox as messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image

class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Set window title
        self.title("Wepco Plastics Job Scheduling Software")
        self.configure(bg="white")

        # disable window resizing
        self.resizable(False, False)

        # Set window dimensions
        self.minsize(700, 500)
        self.maxsize(700, 500)

        # creates a container
        container = tk.Frame(self)  
        container.pack(expand=True)
  
        # initializing frames to an empty array
        self.frames = {}  

        for F in (HomePage, CreateSchedulePage):
  
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(HomePage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame home page
class HomePage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        self.configure(bg="white")
        self.image = Image.open("Resources/WepcoLogo.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # image label
        image_label = tk.Label(self, image=self.photo)
        image_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        image_label.configure(bg="white")

        # file name label
        padding1_label = tk.Label(self, text="text", height=2)
        padding1_label.grid(row=1, column=0, padx=5, pady=(5,0))
        padding1_label.configure(bg="white", fg="white")

        # file name label
        padding2_label = tk.Label(self, text="", height=2)
        padding2_label.grid(row=1, column=1, padx=5, pady=(5,0))
        padding2_label.configure(bg="white")

        # file name label
        file_name_label = tk.Label(self, text="", height=2)
        file_name_label.grid(row=1, column=2, padx=5, pady=(5,0))
        file_name_label.configure(bg="white")

        # file name label
        padding3_label = tk.Label(self, text="", height=2)
        padding3_label.grid(row=1, column=3, padx=5, pady=(5,0))
        padding3_label.configure(bg="white")

        # file name label
        padding4_label = tk.Label(self, text="", height=2)
        padding4_label.grid(row=1, column=4, padx=5, pady=(5,0))
        padding4_label.configure(bg="white")

        # file selection button
        fileSelectionButton = tk.Button(self, text ="File Selection", width=10, height=2, command = lambda: print("FileSelection Clicked"))
        fileSelectionButton.grid(row = 2, column = 2, padx = 10, pady = 10)
  
        # create schedule button
        createScheduleButton = tk.Button(self, text ="Create Schedule", width=10, height=2, command = lambda : controller.show_frame(CreateSchedulePage))
        createScheduleButton.grid(row = 3, column = 2, padx = 10, pady = 10)
  
# third window frame CreateSchedulePage
class CreateSchedulePage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="white")
        self.image = Image.open("Resources/WepcoLogo2.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # create the image label
        image_label = tk.Label(self, image=self.photo)
        image_label.grid(row = 0, column = 0, padx = 10, pady = 10)
        image_label.configure(bg="white")
        
        # Container frame to page components
        date_container = tk.Frame(self, bg="white")
        date_container.grid(row=1, column=0, padx=10, pady=10)

        # function to print selected dates
        def print_dates():
            start_date = start_date_entry.get_date()
            end_date = end_date_entry.get_date()
            print("Start Date:", start_date)
            print("End Date:", end_date)
        
        # start date label
        start_label = tk.Label(date_container, text="Start Date", bg="white")
        start_label.grid(row=0, column=0, padx=10, pady=10)

        # DateEntry widget for start date
        start_date_entry = DateEntry(date_container, background='skyblue', foreground='black', borderwidth=2)
        start_date_entry.grid(row=0, column=1, padx=10, pady=10)

        # command button to confirm dates
        confirmDatesButton = tk.Button(date_container, text="Confirm Dates", width=10, height=2, command=print_dates)
        confirmDatesButton.grid(row=0, column=2, padx=10, pady=10)

        # end date label
        end_label = tk.Label(date_container, text="End Date", bg="white")
        end_label.grid(row=1, column=0, padx=10, pady=10)

        # DateEntry widget for end date
        end_date_entry = DateEntry(date_container, background='skyblue', foreground='black', borderwidth=2)
        end_date_entry.grid(row=1, column=1, padx=10, pady=10)

        # additional options label
        options_label = tk.Label(date_container, text="Additional Options", bg="white")
        options_label.grid(row=2, column=0, padx=10, pady=10)

        # adjust job preferences button 
        jobPreferencesButton = tk.Button(date_container, text="Job Preferences", width=10, height=2, command = lambda: print("Job Preferences are chosen"))
        jobPreferencesButton.grid(row=2, column=1, padx=10, pady=10)

        # adjust operating hours button 
        operatingHoursButton = tk.Button(date_container, text="Operating Hours", width=10, height=2, command = lambda: print("Operating Hours are Selected"))
        operatingHoursButton.grid(row=2, column=2, padx=10, pady=10)

        # main menu button
        mainMenuButton = tk.Button(date_container, text ="Main Menu", width=10, height=2, command = lambda : controller.show_frame(HomePage))
        mainMenuButton.grid(row = 3, column = 0, padx = 10, pady = 10)

        # create schedule button 
        createScheduleButton = tk.Button(date_container, text="Create Schedule", width=10, height=2, command = lambda: print("Schedule Created"))
        createScheduleButton.grid(row=3, column=2, padx=10, pady=10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()