import pandas as pd

class FileSelection:
    def main(self):
        # Open file dialog to select the file
        file_path = self.select_file()

        if file_path:
            # Read Excel file
            raw_data = pd.read_excel(file_path, "TempQueryName")

            # Sort based on job status and due date
            sorted_data = raw_data.query('Completed == "Received" or Completed == "Not Started"')
            sorted_data = sorted_data.sort_values(by=['due_date'])

        return file_path  # Return the selected file path

    def select_file(self):
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()

        return file_path

# Entry point
if __name__ == "__main__":
    selected_file_path = FileSelection().main()
    print(selected_file_path)  # Print the selected file path
