from datetime import datetime

class Job:
    def __init__(self):
        self.Job_Num = None
        self.Qty = None
        self.ProductionHours = None
        self.Deadline = None
        self.Status = None
        self.PO_Num = None
        self.SO_Num = None
        self.PO_Price = None
        self.Frame = None
        self.Lbs = None
        self.Material_ID = None
        self.Material_Name = None # Color Name
        self.Cost_Per_Pound = None
        self.Colorant_ID = None
        self.Colorant_Name = None # Color Name
        
        self.Overall_Color = None
        self.Job_Availability = False # This shows whether it's assigned to a timeslot, False meaning it can be assigned to a timeslot.
        self.Machine_Assignment = None
        self.Start = None
        self.End = None

    # Getters for each variable
    def get_Job_Num(self):
        return self.Job_Num
    
    def get_Qty(self):
        return self.Qty
    
    def get_ProductionHours(self):
        return self.ProductionHours
    
    def get_Deadline(self):
        return self.Deadline
    
    def get_Status(self):
        return self.Status
    
    def get_PO_Num(self):
        return self.PO_Num
    
    def get_SO_Num(self):
        return self.SO_Num
    
    def get_PO_Price(self):
        return self.PO_Price
    
    def get_Frame(self):
        return self.Frame
    
    def get_Lbs(self):
        return self.Lbs
    
    def get_Material_ID(self):
        return self.Material_ID
    
    def get_Material_Name(self):
        return self.Material_Name
    
    def get_Cost_Per_Pound(self):
        return self.Cost_Per_Pound
    
    def get_Colorant_ID(self):
        return self.Colorant_ID
    
    def get_Colorant_Name(self):
        return self.Colorant_Name

    def get_Overall_Color(self):
        return self.Overall_Color

    def get_Job_Availability(self):
        return self.Job_Availability
    
    def get_Machine_Assignment(self):
        return self.Machine_Assignment
    
    def get_Start(self):
        return self.Start
    
    def get_End(self):
        return self.End

    # Setters for each variable
    def set_Job_Num(self, job_num):
        self.Job_Num = job_num
    
    def set_Qty(self, qty):
        self.Qty = qty

    def set_ProductionHours(self, productionhours):
        self.ProductionHours = productionhours

    def set_Deadline(self, deadline):
        self.Deadline = deadline

    def set_Status(self, status):
        self.Status = status

    def set_PO_Num(self, po_num):
        self.PO_Num = po_num

    def set_SO_Num(self, so_num):
        self.SO_Num = so_num

    def set_PO_Price(self, po_price):
        self.PO_Price = po_price

    def set_Frame(self, frame):
        self.Frame = frame

    def set_Lbs(self, lbs):
        self.Lbs = lbs

    def set_Material_ID(self, material_id):
        self.Material_ID = material_id

    def set_Material_Name(self, material_name):
        self.Material_Name = material_name

    def set_Cost_Per_Pound(self, cost_per_pound):
        self.Cost_Per_Pound = cost_per_pound

    def set_Colorant_ID(self, colorant_id):
        self.Colorant_ID = colorant_id

    def set_Colorant_Name(self, colorant_name):
        self.Colorant_Name = colorant_name

    def set_Overall_Color(self, overall_color):
        self.Overall_Color = overall_color

    def set_Job_Availability(self, job_availability):
        self.Job_Availability = job_availability
    
    def set_Machine_Assignment(self, machine_assignment):
        self.Machine_Assignment = machine_assignment

    def set_Start(self, start):
        self.Start = start

    def set_End(self, end):
        self.End = end