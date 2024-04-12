from datetime import datetime

class Changeover:
    def __init__(self):
        self.Name = "Changeover"
        self.Start = None
        self.End = None
        self.JobA_Num = None  # Job object being changed from
        self.JobB_Num = None  # Job object being changed into

    def get_name(self):
        return self.Name
    
    def get_start(self):
        return self.Start
    
    def get_end(self):
        return self.End

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
