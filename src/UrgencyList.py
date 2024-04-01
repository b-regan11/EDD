from datetime import datetime
from Job import Job

class UrgencyList:
    def __init__(self):
        # Defining the Urgency Lists
        self.UL_Attainable = {}
        self.UL_Overdue_Attainable = {}
        self.UL_Unattainable = {}
        self.UL_Overdue_Unattainable = {}
        self.UL_Other = {}

    def create(self, start_date, end_date, sorted_data):
        # Urgency List Data split for Job Priorities
        UrgencyList_Data = sorted_data[(sorted_data['due_date'] >= start_date) & (sorted_data['due_date'] <= end_date)]
        attainable = UrgencyList_Data.query('production_hrs <= 25')  # 1
        unattainable = UrgencyList_Data.query('production_hrs > 25')  # 3
        UrgencyList_Data = sorted_data[(sorted_data['due_date'] > '2020-1-01') & (sorted_data['due_date'] < start_date)]
        overdue_attainable = UrgencyList_Data.query('production_hrs <= 25')  # 2
        overdue_unattainable = UrgencyList_Data.query('production_hrs > 25')  # 4
        other_list = sorted_data[(sorted_data['due_date'] > end_date) & (sorted_data['due_date'] < '2099-1-01')]  # 5

        # Calculate the remainder number of jobs to fill in the other list to total 40 jobs
        Remainder = 40 - (len(attainable) + len(overdue_attainable) + len(unattainable) + len(overdue_unattainable))
        other_list = other_list.iloc[:Remainder]  # Return extra rows to make sure there isn't more than 40 rows of data
        
        for UL in range(5):
            if UL == 0: # Attainable
                row_count = len(attainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(attainable.iloc[r,0]) # Accessing the first column of the 'attainable' DataFrame
                    self.UL_Attainable[r] = job
            elif UL == 1: # Overdue Attainable
                row_count = len(overdue_attainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(overdue_attainable.iloc[r,0]) # Accessing the first column of the 'overdue attainable' DataFrame
                    self.UL_Overdue_Attainable[r] = job
            elif UL == 2: # Unattainable
                row_count = len(unattainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(unattainable.iloc[r,0]) # Accessing the first column of the 'unattainable' DataFrame
                    self.UL_Unattainable[r] = job
            elif UL == 3: # Overdue Unattainable
                row_count = len(overdue_unattainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(overdue_unattainable.iloc[r,0]) # Accessing the first column of the 'overdue unattainable' DataFrame
                    self.UL_Overdue_Unattainable[r] = job
            elif UL == 4: # Other
                row_count = len(other_list)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(other_list.iloc[r,0]) # Accessing the first column of the 'other list' DataFrame
                    self.UL_Other[r] = job
    
    # Getter methods 
    def get_job_num(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Job_Num()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Job_Num()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Job_Num()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Job_Num()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Job_Num()
        return None # Return None if the job is not found
    
    def get_job(self, list_index, job_index):
        if list_index == 0:
            return self.UL_Attainable.get(job_index)
        elif list_index == 1:
            return self.UL_Overdue_Attainable.get(job_index)
        elif list_index == 2:
            return self.UL_Unattainable.get(job_index)
        elif list_index == 3:
            return self.UL_Overdue_Unattainable.get(job_index)
        elif list_index == 4:
            return self.UL_Other.get(job_index)
        return None  # Return None if the job is not found

if __name__ == "__main__":
    urgency_list = UrgencyList()
