from datetime import datetime, timedelta
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
        # Convert start_date and end_date to datetime objects
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        
        # Urgency List Data split for Job Priorities
        UrgencyList_Data = sorted_data[(sorted_data['due_date'] >= start_date - timedelta(days=0.5)) & (sorted_data['due_date'] <= end_date + timedelta(days=2))]
        attainable = UrgencyList_Data.query('production_hrs <= 25')  # 1
        unattainable = UrgencyList_Data.query('production_hrs > 25')  # 3
        UrgencyList_Data = sorted_data[(sorted_data['due_date'] > '2023-1-01') & (sorted_data['due_date'] < start_date - timedelta(days=0.5))]
        overdue_attainable = UrgencyList_Data.query('production_hrs <= 25')  # 2
        overdue_unattainable = UrgencyList_Data.query('production_hrs > 25')  # 4
        other_list = sorted_data[(sorted_data['due_date'] > end_date + timedelta(days=2)) & (sorted_data['due_date'] < '2099-1-01')]  # 5

        # Calculate the remainder number of jobs to fill in the other list to total 40 jobs
        Remainder = 40 - (len(attainable) + len(overdue_attainable) + len(unattainable) + len(overdue_unattainable))
        other_list = other_list.iloc[:Remainder]  # Return extra rows to make sure there isn't more than 40 rows of data
        # print(attainable)
        # print(overdue_attainable)
        # print(unattainable)
        # print(overdue_unattainable)
        # print(other_list)
        
        for UL in range(5):
            if UL == 0: # Attainable
                row_count = len(attainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(attainable.iloc[r,0]) # Accessing the first column of the 'attainable' DataFrame
                    job.set_Qty(attainable.iloc[r,1])
                    job.set_ProductionHours(attainable.iloc[r,2])
                    job.set_Deadline(attainable.iloc[r,4])
                    job.set_Status(attainable.iloc[r,5])
                    job.set_PO_Num(attainable.iloc[r,6])
                    job.set_SO_Num(attainable.iloc[r,7])
                    job.set_PO_Price(attainable.iloc[r,8])
                    job.set_Frame(attainable.iloc[r,9])
                    job.set_Lbs(attainable.iloc[r,10])
                    job.set_Material_ID(attainable.iloc[r,11])
                    job.set_Cost_Per_Pound(attainable.iloc[r,12])
                    job.set_Colorant_ID(attainable.iloc[r,13])
                    
                    job.set_Overall_Color(None)
                    job.set_Job_Availability(False)
                    job.set_Machine_Assignment(None)
                    job.set_Start(None)
                    job.set_End(None)
                    self.UL_Attainable[r] = job
            elif UL == 1: # Overdue Attainable
                row_count = len(overdue_attainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(overdue_attainable.iloc[r,0]) 
                    job.set_Qty(overdue_attainable.iloc[r,1])
                    job.set_ProductionHours(overdue_attainable.iloc[r,2])
                    job.set_Deadline(overdue_attainable.iloc[r,4])
                    job.set_Status(overdue_attainable.iloc[r,5])
                    job.set_PO_Num(overdue_attainable.iloc[r,6])
                    job.set_SO_Num(overdue_attainable.iloc[r,7])
                    job.set_PO_Price(overdue_attainable.iloc[r,8])
                    job.set_Frame(overdue_attainable.iloc[r,9])
                    job.set_Lbs(overdue_attainable.iloc[r,10])
                    job.set_Material_ID(overdue_attainable.iloc[r,11])
                    job.set_Cost_Per_Pound(overdue_attainable.iloc[r,12])
                    job.set_Colorant_ID(overdue_attainable.iloc[r,13])
                    
                    job.set_Overall_Color(None)
                    job.set_Job_Availability(False)
                    job.set_Machine_Assignment(None)
                    job.set_Start(None)
                    job.set_End(None)
                    self.UL_Overdue_Attainable[r] = job
            elif UL == 2: # Unattainable
                row_count = len(unattainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(unattainable.iloc[r,0]) 
                    job.set_Qty(unattainable.iloc[r,1])
                    job.set_ProductionHours(unattainable.iloc[r,2])
                    job.set_Deadline(unattainable.iloc[r,4])
                    job.set_Status(unattainable.iloc[r,5])
                    job.set_PO_Num(unattainable.iloc[r,6])
                    job.set_SO_Num(unattainable.iloc[r,7])
                    job.set_PO_Price(unattainable.iloc[r,8])
                    job.set_Frame(unattainable.iloc[r,9])
                    job.set_Lbs(unattainable.iloc[r,10])
                    job.set_Material_ID(unattainable.iloc[r,11])
                    job.set_Cost_Per_Pound(unattainable.iloc[r,12])
                    job.set_Colorant_ID(unattainable.iloc[r,13])
                    
                    job.set_Overall_Color(None)
                    job.set_Job_Availability(False)
                    job.set_Machine_Assignment(None)
                    job.set_Start(None)
                    job.set_End(None)
                    self.UL_Unattainable[r] = job
            elif UL == 3: # Overdue Unattainable
                row_count = len(overdue_unattainable)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(overdue_unattainable.iloc[r,0]) 
                    job.set_Qty(overdue_unattainable.iloc[r,1])
                    job.set_ProductionHours(overdue_unattainable.iloc[r,2])
                    job.set_Deadline(overdue_unattainable.iloc[r,4])
                    job.set_Status(overdue_unattainable.iloc[r,5])
                    job.set_PO_Num(overdue_unattainable.iloc[r,6])
                    job.set_SO_Num(overdue_unattainable.iloc[r,7])
                    job.set_PO_Price(overdue_unattainable.iloc[r,8])
                    job.set_Frame(overdue_unattainable.iloc[r,9])
                    job.set_Lbs(overdue_unattainable.iloc[r,10])
                    job.set_Material_ID(overdue_unattainable.iloc[r,11])
                    job.set_Cost_Per_Pound(overdue_unattainable.iloc[r,12])
                    job.set_Colorant_ID(overdue_unattainable.iloc[r,13])
                    
                    job.set_Overall_Color(None)
                    job.set_Job_Availability(False)
                    job.set_Machine_Assignment(None)
                    job.set_Start(None)
                    job.set_End(None)
                    self.UL_Overdue_Unattainable[r] = job
            elif UL == 4: # Other
                row_count = len(other_list)
                for r in range(row_count):
                    job = Job()
                    job.set_Job_Num(other_list.iloc[r,0])
                    job.set_Qty(other_list.iloc[r,1])
                    job.set_ProductionHours(other_list.iloc[r,2])
                    job.set_Deadline(other_list.iloc[r,4])
                    job.set_Status(other_list.iloc[r,5])
                    job.set_PO_Num(other_list.iloc[r,6])
                    job.set_SO_Num(other_list.iloc[r,7])
                    job.set_PO_Price(other_list.iloc[r,8])
                    job.set_Frame(other_list.iloc[r,9])
                    job.set_Lbs(other_list.iloc[r,10])
                    job.set_Material_ID(other_list.iloc[r,11])
                    job.set_Cost_Per_Pound(other_list.iloc[r,12])
                    job.set_Colorant_ID(other_list.iloc[r,13])
                    
                    job.set_Overall_Color(None)
                    job.set_Job_Availability(False)
                    job.set_Machine_Assignment(None)
                    job.set_Start(None)
                    job.set_End(None) 
                    self.UL_Other[r] = job
    
    # Getter methods 
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
    
    def get_job_qty(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Qty()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Qty()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Qty()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Qty()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Qty()
        return None # Return None if the job is not found
    
    def get_job_prod_hours(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_ProductionHours()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_ProductionHours()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_ProductionHours()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_ProductionHours()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_ProductionHours()
        return None # Return None if the job is not found
    
    def get_job_deadline(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Deadline()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Deadline()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Deadline()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Deadline()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Deadline()
        return None # Return None if the job is not found
    
    def get_job_status(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Status()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Status()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Status()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Status()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Status()
        return None # Return None if the job is not found
    
    def get_job_po_num(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_PO_Num()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_PO_Num()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_PO_Num()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_PO_Num()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_PO_Num()
        return None # Return None if the job is not found
    
    def get_job_so_num(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_SO_Num()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_SO_Num()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_SO_Num()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_SO_Num()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_SO_Num()
        return None # Return None if the job is not found
    
    def get_job_po_price(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_PO_Price()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_PO_Price()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_PO_Price()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_PO_Price()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_PO_Price()
        return None # Return None if the job is not found
    
    def get_job_frame(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Frame()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Frame()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Frame()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Frame()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Frame()
        return None # Return None if the job is not found
    
    def get_job_lbs(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Lbs()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Lbs()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Lbs()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Lbs()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Lbs()
        return None # Return None if the job is not found
    
    def get_job_material_id(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Material_ID()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Material_ID()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Material_ID()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Material_ID()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Material_ID()
        return None # Return None if the job is not found
    
    def get_job_material_name(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Material_Name()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Material_Name()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Material_Name()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Material_Name()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Material_Name()
        return None # Return None if the job is not found
    
    def get_job_cost_per_pound(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Cost_Per_Pound()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Cost_Per_Pound()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Cost_Per_Pound()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Cost_Per_Pound()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Cost_Per_Pound()
        return None # Return None if the job is not found
    
    def get_job_colorant_id(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Colorant_ID()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Colorant_ID()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Colorant_ID()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Colorant_ID()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Colorant_ID()
        return None # Return None if the job is not found
    
    def get_job_colorant_name(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Colorant_Name()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Colorant_Name()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Colorant_Name()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Colorant_Name()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Colorant_Name()
        return None # Return None if the job is not found

    def get_job_overall_color(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Overall_Color()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Overall_Color()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Overall_Color()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Overall_Color()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Overall_Color()
        return None # Return None if the job is not found

    def get_job_availability(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Job_Availability()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Job_Availability()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Job_Availability()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Job_Availability()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Job_Availability()
        return None # Return None if the job is not found
    
    def get_job_machine_assignment(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Machine_Assignment()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Machine_Assignment()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Machine_Assignment()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Machine_Assignment()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Machine_Assignment()
        return None # Return None if the job is not found
    
    def get_job_start(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_Start()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_Start()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_Start()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_Start()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_Start()
        return None # Return None if the job is not found
    
    def get_job_end(self, list_num, job_index):
        if list_num ==0:
            if job_index in self.UL_Attainable:
                return self.UL_Attainable[job_index].get_End()
        if list_num ==1:
            if job_index in self.UL_Overdue_Attainable:
                return self.UL_Overdue_Attainable[job_index].get_End()
        if list_num ==2:
            if job_index in self.UL_Unattainable:
                return self.UL_Unattainable[job_index].get_End()
        if list_num ==3:
            if job_index in self.UL_Overdue_Unattainable:
                return self.UL_Overdue_Unattainable[job_index].get_End()
        if list_num ==4:
            if job_index in self.UL_Other:
                return self.UL_Other[job_index].get_End()
        return None # Return None if the job is not found
    
    # Setter methods
    def set_job_start(self, list_num, job_index, start_time):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_Start(start_time)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_Start(start_time)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_Start(start_time)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_Start(start_time)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_Start(start_time)

    def set_job_end(self, list_num, job_index, end_time):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_End(end_time)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_End(end_time)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_End(end_time)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_End(end_time)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_End(end_time)

    def set_job_machine_assignment(self, list_num, job_index, machine_assignment):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_Machine_Assignment(machine_assignment)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_Machine_Assignment(machine_assignment)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_Machine_Assignment(machine_assignment)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_Machine_Assignment(machine_assignment)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_Machine_Assignment(machine_assignment)

    def set_job_availability(self, list_num, job_index, availability):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_Job_Availability(availability)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_Job_Availability(availability)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_Job_Availability(availability)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_Job_Availability(availability)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_Job_Availability(availability)

    def set_job_overall_color(self, list_num, job_index, overall_color):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_Overall_Color(overall_color)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_Overall_Color(overall_color)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_Overall_Color(overall_color)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_Overall_Color(overall_color)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_Overall_Color(overall_color)
    
    def set_job_finished(self, list_num, job_index, finished):
        if list_num == 0:
            if job_index in self.UL_Attainable:
                self.UL_Attainable[job_index].set_Finished(finished)
        elif list_num == 1:
            if job_index in self.UL_Overdue_Attainable:
                self.UL_Overdue_Attainable[job_index].set_Finished(finished)
        elif list_num == 2:
            if job_index in self.UL_Unattainable:
                self.UL_Unattainable[job_index].set_Finished(finished)
        elif list_num == 3:
            if job_index in self.UL_Overdue_Unattainable:
                self.UL_Overdue_Unattainable[job_index].set_Finished(finished)
        elif list_num == 4:
            if job_index in self.UL_Other:
                self.UL_Other[job_index].set_Finished(finished)
    
    # getter methd for total job count in an urgency list
    def get_job_count(self, list_num):
        if list_num == 0:
            if len(self.UL_Attainable) == 0:
                print("list ", list_num, " is empty")
                return 0
            else:
                return max(self.UL_Attainable.keys()) + 1
        elif list_num == 1:
            if len(self.UL_Overdue_Attainable) == 0:
                print("list ", list_num, " is empty")
                return 0
            else:
                return max(self.UL_Overdue_Attainable.keys()) + 1
        elif list_num == 2:
            if len(self.UL_Unattainable) == 0:
                print("list ", list_num, " is empty")
                return 0
            else:
                return max(self.UL_Unattainable.keys()) + 1
        elif list_num == 3:
            if len(self.UL_Overdue_Unattainable) == 0:
                print("list ", list_num, " is empty")
                return 0
            else:
                return max(self.UL_Overdue_Unattainable.keys()) + 1
        elif list_num == 4:
            if len(self.UL_Other) == 0:
                print("list ", list_num, " is empty")
                return 0
            else:
                return max(self.UL_Other.keys()) + 1
        return None
    

if __name__ == "__main__":
    urgency_list = UrgencyList()
