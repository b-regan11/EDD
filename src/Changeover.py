from datetime import datetime

class Changeover:
    def __init__(self):
        self.Name = "Changeover"
        self.Start = None
        self.End = None
        self.Job = None
        self.Job_Num = None
        self.Lbs = None
        self.Material_ID = None
        self.Cost_Per_Pound = None


        self.JobA_Num = None  # Job object being changed from
        self.JobB_Num = None  # Job object being changed into

    def get_name(self):
        return self.Name
    
    def get_Start(self):
        return self.Start
    
    def get_End(self):
        return self.End
    
    def get_Frame(self):
        job = self.get_Job()
        return job.get_Frame()
    
    def get_Overall_Color(self):
        job = self.get_Job()
        return job.get_Overall_Color()
    
    def get_Qty(self):
        job = self.get_Job()
        return job.get_Qty()
    
    def get_ProductionHours(self):
        job = self.get_Job()
        return job.get_ProductionHours()
    
    def get_Deadline(self):
        job = self.get_Job()
        return job.get_Deadline()
    
    def get_Status(self):
        job = self.get_Job()
        return job.get_Status()
    
    def get_PO_Num(self):
        job = self.get_Job()
        return job.get_PO_Num()
    
    def get_SO_Num(self):
        job = self.get_Job()
        return job.get_SO_Num()
    
    def get_PO_Price(self):
        job = self.get_Job()
        return job.get_PO_Price()
    
    def get_Frame(self):
        job = self.get_Job()
        return job.get_Frame()
    
    def get_Lbs(self):
        job = self.get_Job()
        return job.get_Lbs()
    
    def get_Material_ID(self):
        job = self.get_Job()
        return job.get_Material_ID()
    
    def get_Material_Name(self):
        job = self.get_Job()
        return job.get_Material_Name()
    
    def get_Cost_Per_Pound(self):
        job = self.get_Job()
        return job.get_Cost_Per_Pound()
    
    def get_Colorant_ID(self):
        job = self.get_Job()
        return job.get_Colorant_ID()
    
    def get_Colorant_Name(self):
        job = self.get_Job()
        return job.get_Colorant_Name()
    
    def get_Overall_Color(self):
        job = self.get_Job()
        return job.get_Overall_Color()
    
    def get_Machine_Assignment(self):
        job = self.get_Job()
        return job.get_Machine_Assignment()
    
    def get_Finished(self):
        job = self.get_Job()
        return job.get_Finished()
    


    def get_jobA_num(self):
        return self.JobA_Num

    def get_jobB_num(self):
        return self.JobB_Num

    def set_name(self, name):
        self.Name = name

    def set_start(self, start):
        self.Start = start

    def set_end(self, end):
        self.End = end

    def set_jobA_num(self, jobA_num):
        self.JobA_Num = jobA_num

    def set_jobB_num(self, jobB_num):
        self.JobB_Num = jobB_num



    def set_Job(self, job_obj):
        self.Job = job_obj

    def set_Job_Num(self):
        job = self.Job
        job_num = job.get_Job_Num()
        if job_num.endswith(" (Changeover)"):
            self.Job_Num = job_num
        else:    
            self.Job_Num = job_num + " (Changeover)" 

    def set_Lbs(self):
        job = self.Job
        lbs = job.get_Lbs()
        self.Lbs = lbs
    
    def set_Material_ID(self):
        job = self.Job
        material = job.get_Material_ID()
        self.Lbs = material
    
    def set_Cost_Per_Pound(self):
        job = self.Job
        cost = job.get_Cost_Per_Pound()
        self.Lbs = cost

    def get_Job(self):
        return self.Job
    
    def get_Job_Num(self):
        return self.Job_Num
    
    def get_Lbs(self):
        return self.Lbs
    
    def get_Material_ID(self):
        return self.Lbs
    
    def get_Cost_Per_Pound(self):
        return self.Lbs
    
    def get_Job_Start(self):
        job = self.Job
        job_start = job.get_Job_Start()
        return job_start

    def get_Job_End(self):
        job = self.Job
        job_end = job.get_Job_End()
        return job_end