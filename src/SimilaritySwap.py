from datetime import datetime, timedelta
import os
import pandas as pd
from UrgencyList import UrgencyList
from Timeslot import Slot
from Machines import Machines
from Changeover import Changeover
from BinPacking import BinPacking
from Job import Job

class SimilaritySwap:
    # the create method is used to create job to job matrices for each machine
    def create(machines):
        # From / To Chart for Frame Ranking
        FromTo_Frames = [
            ["FromTo", "Small-T", "Round", "Rectangle", "Short Large-T", "Small Self-Contained", "Large-T", "Self Contained", "XL-T"],
            ["Small-T", 1.0, 1.300, 1.600, 1.800, 2.100, 2.400, 2.700, 3.000],
            ["Round", 1.300, 1.0, 1.300, 1.600, 1.800, 2.100, 2.400, 2.700],
            ["Rectangle", 1.600, 1.300, 1.0, 1.300, 1.600, 1.800, 2.100, 2.400],
            ["Short Large-T", 1.800, 1.600, 1.300, 1.0, 1.300, 1.600, 1.800, 2.100],
            ["Small Self-Contained", 2.100, 1.800, 1.600, 1.300, 1.0, 1.300, 1.600, 1.800],
            ["Large-T", 2.400, 2.100, 1.800, 1.600, 1.300, 1.0, 1.300, 1.600],
            ["Self Contained", 2.700, 2.400, 2.100, 1.800, 1.600, 1.300, 1.0, 1.300],
            ["XL-T", 3.000, 2.700, 2.400, 2.100, 1.800, 1.600, 1.300, 1.0]
        ]

        # From / To Chart for Color Ranking
        FromTo_Colors = [
            ["FromTo", "unknown", "clear/natural", "white", "grey/gray/lightgrey/softgrey/silver", "aqua/blue/lightblue/skyblue", "weatherbronze/teal", "green", "darkblue", "purple/violet", "red", "magenta/pink", "lightcoral", "orange/tangerine", "yellow", "tan/beige", "brown", "weatheredbrown", "darkgrey/smoke", "black"],
            ["unknown", 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90],
            ["clear/natural", 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85],
            ["white", 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80],
            ["grey/gray/lightgrey/softgrey/silver", 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75],
            ["aqua/blue/lightblue/skyblue", 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70],
            ["weatherbronze/teal", 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65],
            ["green", 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60],
            ["darkblue", 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55],
            ["purple/violet", 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50],
            ["red", 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45],
            ["magenta/pink", 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40],
            ["lightcoral", 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30, 1.35],
            ["orange/tangerine", 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25, 1.30],
            ["yellow", 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20, 1.25],
            ["tan/beige", 2.40, 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15, 1.20],
            ["brown", 2.50, 2.40, 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10, 1.15],
            ["weatheredbrown", 2.60, 2.50, 2.40, 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05, 1.10],
            ["darkgrey/smoke", 2.70, 2.60, 2.50, 2.40, 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00, 1.05],
            ["black", 2.80, 2.70, 2.60, 2.50, 2.40, 2.30, 2.20, 2.10, 2.00, 1.90, 1.80, 1.70, 1.60, 1.50, 1.40, 1.30, 1.20, 1.10, 1.00]
        ]

        FromTo_Mach2Jobs = [
            ["FromTo"]
        ]
        FromTo_Mach5Jobs = [
            ["FromTo"]
        ]
        FromTo_Mach6Jobs = [
            ["FromTo"]
        ]
        FromTo_Mach9Jobs = [
            ["FromTo"]
        ]

        mach2_jobs = machines.get_assigned_jobs(1)
        mach5_jobs = machines.get_assigned_jobs(2)
        mach6_jobs = machines.get_assigned_jobs(3)
        mach9_jobs = machines.get_assigned_jobs(4)
        
        # Access the element at row i and column j
        # Will be used to assign a value to each cell (excluding headers) based on Frame
        for m in range(1, 5):
            if m == 1:
                FromTo_MachJobs = FromTo_Mach2Jobs
                mach_jobs = mach2_jobs
            elif m == 2:
                FromTo_MachJobs = FromTo_Mach5Jobs
                mach_jobs = mach5_jobs
            elif m == 3:
                FromTo_MachJobs = FromTo_Mach6Jobs
                mach_jobs = mach6_jobs
            elif m == 4:
                FromTo_MachJobs = FromTo_Mach9Jobs
                mach_jobs = mach9_jobs

            # Filling in matrix w/ None values for the appropriate number of jobs
            for k in range(len(mach_jobs)):
                FromTo_MachJobs[0].append(mach_jobs[k])
            mach_num_columns = len(FromTo_MachJobs[0])

            for h in range(len(mach_jobs)):
                mach_row_values = [0] * mach_num_columns 
                mach_row_values[0] = mach_jobs[h]
                FromTo_MachJobs.append(mach_row_values)

            # Replacing the None values w/ values from the FromTo_Frames matrix based on each job's frame
            for i in range(len(FromTo_MachJobs)):
                for j in range(len(FromTo_MachJobs[i])):
                    if FromTo_MachJobs[i][j] == 0:    
                        # Find the From/To job combination for each cell
                        From_Job = FromTo_MachJobs[i][0]
                        To_Job = FromTo_MachJobs[0][j]

                        # Find the From/To frame combination for each cell
                        From_Job_Frame = machines.get_assigned_job_frame(m, From_Job)
                        To_Job_Frame = machines.get_assigned_job_frame(m, To_Job)

                        # Find the From/To color combination for each cell
                        From_Job_Color = machines.get_assigned_job_color(m, From_Job)
                        To_Job_Color = machines.get_assigned_job_color(m, To_Job)
                        
                        # Cycle through each row header to find Job Color in the header
                        for row_index in range(1, len(FromTo_Colors)):
                            From_ColorGroup = FromTo_Colors[row_index][0]
                            if From_Job_Color in From_ColorGroup:
                                From_Job_ColorGroup = From_ColorGroup

                        # Cycle through each column header to find Job Color in the header
                        for col_index in range(1, len(FromTo_Colors[0])):
                            To_ColorGroup = FromTo_Colors[0][col_index]
                            if To_Job_Color in To_ColorGroup:
                                To_Job_ColorGroup = To_ColorGroup

                        # Frame Compatibility Value (Higher value means less compatible)
                        FrameCV = FromTo_Frames[FromTo_Frames[0].index(From_Job_Frame)][FromTo_Frames[0].index(To_Job_Frame)]

                        # Color Compatibility Value (Higher value means less compatible)
                        ColorCV = FromTo_Colors[FromTo_Colors[0].index(From_Job_ColorGroup)][FromTo_Colors[0].index(To_Job_ColorGroup)]

                        TotalCV = round((2*FrameCV) + ColorCV, 2)
                        
                        if m == 1:
                            FromTo_Mach2Jobs[i][j] = TotalCV
                        elif m == 2:
                            FromTo_Mach5Jobs[i][j] = TotalCV
                        elif m == 3:
                            FromTo_Mach6Jobs[i][j] = TotalCV
                        elif m == 4:
                            FromTo_Mach9Jobs[i][j] = TotalCV

            # # This is a method for verifying jobs by job_num
            # for i in range(len(FromTo_MachJobs)):
            #     for j in range(len(FromTo_MachJobs[i])):
            #         # if (FromTo_MachJobs[i][j] is not int) and (FromTo_MachJobs[i][j] is not "FromTo"):
            #         if ((i >= 1) and (j == 0)) or ((i == 0) and (j >= 1)):
            #             Job_Obj = FromTo_MachJobs[i][j]
            #             Job_Num = machines.get_assigned_job_num(m, Job_Obj)
            #             if m == 1:
            #                 FromTo_Mach2Jobs[i][j] = Job_Num
            #             elif m == 2:
            #                 FromTo_Mach5Jobs[i][j] = Job_Num
            #             elif m == 3:
            #                 FromTo_Mach6Jobs[i][j] = Job_Num
            #             elif m == 4:
            #                 FromTo_Mach9Jobs[i][j] = Job_Num
        
        #--------------------- Print the tables -----------------------
        # print("Here is the Machine 2 From / To Job Matrix")
        # print(machines.get_assigned_job_nums(1))
        # for row in FromTo_Mach2Jobs:
        #     print(row)

        # print("Here is the Machine 5 From / To Job Matrix")
        # print(machines.get_assigned_job_nums(2))
        # for row in FromTo_Mach5Jobs:
        #     print(row)

        # print("Here is the Machine 6 From / To Job Matrix")
        # print(machines.get_assigned_job_nums(3))
        # for row in FromTo_Mach6Jobs:
        #     print(row)

        # print("Here is the Machine 9 From / To Job Matrix")
        # print(machines.get_assigned_job_nums(4))
        # for row in FromTo_Mach9Jobs:
        #     print(row)
        
        print("\nJob Compatibility Value Matrices Created\n")

        return FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs
        
    def job_reorder(FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs):
        
        for m in range(1, 5):
            if m == 1:
                temp_matrix = [row[:] for row in FromTo_Mach2Jobs]
                mach_name = 2
            elif m == 2:
                temp_matrix = [row[:] for row in FromTo_Mach5Jobs]
                mach_name = 5
            elif m == 3:
                temp_matrix = [row[:] for row in FromTo_Mach6Jobs]
                mach_name = 6
            elif m == 4:
                temp_matrix = [row[:] for row in FromTo_Mach9Jobs]
                mach_name = 9
        
            Original_Job_Order = temp_matrix[0][1:]
            New_Job_Order = []

            # this keeps the last job as the last job in the first loop iteration
            Prev_CV = temp_matrix[0][-1]
            New_Job_Order.append(Prev_CV)

            # iterate through each job
            for _ in range(len(temp_matrix[0]) - 2):
                # identify the starting column
                From_Job_Column = Prev_CV
                
                # find the index of the column header matching the previous CV
                column_index = temp_matrix[0].index(From_Job_Column)
        
                # Delete row starting with Smallest_To_Job
                del temp_matrix[column_index]

                # find the job / row with the smallest CV
                Smallest_CV = float('inf')
                Smallest_From_Job = None
                for r in range(1, len(temp_matrix)):
                    CV = temp_matrix[r][column_index]
                    if CV <= Smallest_CV:
                        Smallest_CV = CV
                        Smallest_From_Job = temp_matrix[r][0]

                # delete the corresponding row and column
                del temp_matrix[0][column_index]
                for row in temp_matrix[1:]:
                    del row[column_index]

                Prev_CV = Smallest_From_Job
                New_Job_Order.append(Prev_CV)

            New_Job_Order = New_Job_Order[::-1]
            if m == 1:
                Mach2_New_Order = New_Job_Order
            elif m == 2:
                Mach5_New_Order = New_Job_Order
            elif m == 3:
                Mach6_New_Order = New_Job_Order
            elif m == 4:
                Mach9_New_Order = New_Job_Order
            
        # below is where the new job order will be assigned to timeslots for each machine
        return Mach2_New_Order, Mach5_New_Order, Mach6_New_Order, Mach9_New_Order
    
    def time_assignment(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, Mach2_New_Order, Mach5_New_Order, Mach6_New_Order, Mach9_New_Order):
        machines_alt = Machines()
        machines_alt.create(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times)

        mach2_curr_slot = 0
        mach5_curr_slot = 0
        mach6_curr_slot = 0
        mach9_curr_slot = 0

        mach2curr_start = None
        mach5curr_start = None
        mach6curr_start = None
        mach9curr_start = None

        machine_start_times = []

        for m in range(1, 5):
            if m == 1:
                New_Job_Order = Mach2_New_Order
            elif m == 2:
                New_Job_Order = Mach5_New_Order
            elif m == 3:
                New_Job_Order = Mach6_New_Order
            elif m == 4:
                New_Job_Order = Mach9_New_Order

            New_Job_Order_Count = len(New_Job_Order)
            for j in range(New_Job_Order_Count):
                # create new job object for this new machine obj
                job_obj_orig = New_Job_Order[j]
                job_obj = Job()

                # transfer the job values except start and end times
                new_job_num = job_obj_orig.get_Job_Num()
                new_qty = job_obj_orig.get_Qty()
                new_prod_hrs = job_obj_orig.get_ProductionHours()
                new_deadline = job_obj_orig.get_Deadline()
                new_status = job_obj_orig.get_Status()
                new_po_num = job_obj_orig.get_PO_Num()
                new_so_num = job_obj_orig.get_SO_Num()
                new_po_price = job_obj_orig.get_PO_Price()
                new_frame = job_obj_orig.get_Frame()
                new_lbs = job_obj_orig.get_Lbs()
                new_material_id = job_obj_orig.get_Material_ID()
                new_material_name = job_obj_orig.get_Material_Name()
                new_cost_per_lb = job_obj_orig.get_Cost_Per_Pound()
                new_colorant_id = job_obj_orig.get_Colorant_ID()
                new_colorant_name = job_obj_orig.get_Colorant_Name()
                new_overall_color = job_obj_orig.get_Overall_Color()
                new_machine_assignment = job_obj_orig.get_Machine_Assignment()

                job_obj.set_Job_Num(new_job_num)
                job_obj.set_Qty(new_qty)
                job_obj.set_ProductionHours(new_prod_hrs)
                job_obj.set_Deadline(new_deadline)
                job_obj.set_Status(new_status)
                job_obj.set_PO_Num(new_po_num)
                job_obj.set_SO_Num(new_so_num)
                job_obj.set_PO_Price(new_po_price)
                job_obj.set_Frame(new_frame)
                job_obj.set_Lbs(new_lbs)
                job_obj.set_Material_ID(new_material_id)
                job_obj.set_Material_Name(new_material_name)
                job_obj.set_Cost_Per_Pound(new_cost_per_lb)
                job_obj.set_Colorant_ID(new_colorant_id)
                job_obj.set_Colorant_Name(new_colorant_name)
                job_obj.set_Overall_Color(new_overall_color)
                job_obj.set_Machine_Assignment(new_machine_assignment)
                
                # calculate slots based on prod hrs for job j
                job_slots = machines_alt.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=job_obj.get_ProductionHours()))

                # frame implementation
                frame_name = job_obj.get_Frame()
                frame_num = machines_alt.get_frame_index_by_name(frame_name)
                if frame_num == None:
                    continue # frame_num should never equal None but just incase it does

                if machines_alt.is_machine_full(m) == False:
                    if m == 1:
                        mach2curr_start = machines_alt.get_start_time(m, mach2_curr_slot)
                    elif m == 2:
                        mach5curr_start = machines_alt.get_start_time(m, mach5_curr_slot)
                    elif m == 3:
                        mach6curr_start = machines_alt.get_start_time(m, mach6_curr_slot)
                    elif m == 4:
                        mach9curr_start = machines_alt.get_start_time(m, mach9_curr_slot)
                
                # if machine is full, it will not be selectable
                machine_start_times.clear()
                if machines_alt.is_machine_full(m) == False:
                    if m == 1:
                        machine_start_times.append(mach2curr_start)
                    elif m == 2:
                        machine_start_times.append(mach5curr_start)
                    elif m == 3:
                        machine_start_times.append(mach6curr_start)
                    elif m == 4:
                        machine_start_times.append(mach9curr_start)
                
                # if machine_start_times is empty, end loop
                if len(machine_start_times) == 0:
                    continue

                for ch in range(4):
                    if ch == 0:
                        if m == 1:
                            changeover_start = machines_alt.get_start_time(m, mach2_curr_slot)
                        elif m == 2:
                            changeover_start = machines_alt.get_start_time(m, mach5_curr_slot)
                        elif m == 3:
                            changeover_start = machines_alt.get_start_time(m, mach6_curr_slot)
                        elif m == 4:
                            changeover_start = machines_alt.get_start_time(m, mach9_curr_slot)
                    if m == 1:
                        changeover_end = machines_alt.get_end_time(m, mach2_curr_slot)
                    elif m == 2:
                        changeover_end = machines_alt.get_end_time(m, mach5_curr_slot)
                    elif m == 3:
                        changeover_end = machines_alt.get_end_time(m, mach6_curr_slot)
                    elif m == 4:
                        changeover_end = machines_alt.get_end_time(m, mach9_curr_slot)
                    
                    changeover = Changeover()
                    changeover.set_start(changeover_start)
                    changeover.set_end(changeover_end)
                    changeover.set_jobB_num(job_obj)
                    changeover.set_Job(job_obj)
                    changeover.set_Job_Num()

                    if m == 1:
                        machines_alt.set_availability(m, mach2_curr_slot, True)
                        machines_alt.set_assignment(m, mach2_curr_slot, changeover)
                    elif m == 2:
                        machines_alt.set_availability(m, mach5_curr_slot, True)
                        machines_alt.set_assignment(m, mach5_curr_slot, changeover)
                    elif m == 3:
                        machines_alt.set_availability(m, mach6_curr_slot, True)
                        machines_alt.set_assignment(m, mach6_curr_slot, changeover)
                    elif m == 4:
                        machines_alt.set_availability(m, mach9_curr_slot, True)
                        machines_alt.set_assignment(m, mach9_curr_slot, changeover)

                    if machines_alt.get_last_timeslot(m) == changeover.End:
                        if m == 1:
                            print("Machine 2 is full")
                        elif m == 2:
                            print("Machine 5 is full")
                        elif m == 3:
                            print("Machine 6 is full")
                        elif m == 4:
                            print("Machine 9 is full")
                        machines_alt.set_machine_full(m,True)

                        if m == 1:
                            mach2_curr_slot += 1
                        elif m == 2:
                            mach5_curr_slot += 1
                        elif m == 3:
                            mach6_curr_slot += 1
                        elif m == 4:
                            mach9_curr_slot += 1
                        
                        job_obj.set_Start(changeover_start)
                        job_obj.set_End(changeover_end)
                        job_obj.set_Machine_Assignment(m)
                        job_obj.set_Finished(False)
                        machines_alt.assign_job(m, job_obj)
                        break

                    if m == 1:
                        mach2_curr_slot += 1
                    elif m == 2:
                        mach5_curr_slot += 1
                    elif m == 3:
                        mach6_curr_slot += 1
                    elif m == 4:
                        mach9_curr_slot += 1
                
                # if machine is full, it will not be selectable
                machine_start_times.clear()
                if machines_alt.is_machine_full(m) == False:
                    if m == 1:
                        machine_start_times.append(mach2curr_start)
                    elif m == 2:
                        machine_start_times.append(mach5curr_start)
                    elif m == 3:
                        machine_start_times.append(mach6curr_start)
                    elif m == 4:
                        machine_start_times.append(mach9curr_start)
                
                # if machine_start_times is empty, end loop
                if len(machine_start_times) == 0:
                    continue
                # changeover ends

                job_obj.set_Machine_Assignment(m)
                for sc in range(job_slots - 1):
                    if sc == 0:
                        # set the start time for job j
                        if m == 1:
                            job_obj.set_Start(machines_alt.get_start_time(m, mach2_curr_slot))
                        elif m == 2:
                            job_obj.set_Start(machines_alt.get_start_time(m, mach5_curr_slot))
                        elif m == 3:
                            job_obj.set_Start(machines_alt.get_start_time(m, mach6_curr_slot))
                        elif m == 4:
                            job_obj.set_Start(machines_alt.get_start_time(m, mach9_curr_slot))
                    
                    # set the end time for job j
                    if m == 1:
                        job_obj.set_End(machines_alt.get_end_time(m, mach2_curr_slot))
                    elif m == 2:
                        job_obj.set_End(machines_alt.get_end_time(m, mach5_curr_slot))
                    elif m == 3:
                        job_obj.set_End(machines_alt.get_end_time(m, mach6_curr_slot))
                    elif m == 4:
                        job_obj.set_End(machines_alt.get_end_time(m, mach9_curr_slot))

                    if m == 1:
                        machines_alt.set_availability(m, mach2_curr_slot, True)
                        machines_alt.set_assignment(m, mach2_curr_slot, job_obj)
                    elif m == 2:
                        machines_alt.set_availability(m, mach5_curr_slot, True)
                        machines_alt.set_assignment(m, mach5_curr_slot, job_obj)
                    elif m == 3:
                        machines_alt.set_availability(m, mach6_curr_slot, True)
                        machines_alt.set_assignment(m, mach6_curr_slot, job_obj)
                    elif m == 4:
                        machines_alt.set_availability(m, mach9_curr_slot, True)
                        machines_alt.set_assignment(m, mach9_curr_slot, job_obj)

                    # print("Here is the last timeslot -> ", machines_alt.get_last_timeslot(m), " | and Here is job_obj Start -> ", job_obj.get_Start(), " | and Here is job_obj End -> ", job_obj.get_End())
                    if machines_alt.get_last_timeslot(m) == job_obj.get_End():
                        if m == 1:
                            print("Machine 2 is full")
                        elif m == 2:
                            print("Machine 5 is full")
                        elif m == 3:
                            print("Machine 6 is full")
                        elif m == 4:
                            print("Machine 9 is full")
                        machines_alt.set_machine_full(m,True)
                        job_obj.set_Finished(False)

                        if m == 1:
                            mach2_curr_slot += 1
                        elif m == 2:
                            mach5_curr_slot += 1
                        elif m == 3:
                            mach6_curr_slot += 1
                        elif m == 4:
                            mach9_curr_slot += 1
                        break
                    
                    if m == 1:
                        mach2_curr_slot += 1
                    elif m == 2:
                        mach5_curr_slot += 1
                    elif m == 3:
                        mach6_curr_slot += 1
                    elif m == 4:
                        mach9_curr_slot += 1
                
                job_obj.set_Finished(True)
                machines_alt.assign_job(m, job_obj)
        print("\nNew Job Time Calculations Done\n")
        
        return machines_alt
    
    def comparison(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, machines_orig, machines_alt, latest_end_date):
        latest_end_date = datetime.combine(latest_end_date, datetime.min.time())
        # print("nothing to see here")
        # machines_orig = Machines()
        # machines_alt = Machines()
        machines_os = Machines() # optimal solution
        machines_os.create(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times)


        # time_assignment messes up the original machine job times

        latest_end_date = latest_end_date + timedelta(days=2)
        for m in range(1, 5):
            # if m == 1:
            #     print("MACHINE 2")
            # elif m == 2:
            #     print("MACHINE 5")
            # elif m == 3:
            #     print("MACHINE 6")
            # elif m == 4:
            #     print("MACHINE 9")
            jobs_orig = machines_orig.get_assigned_jobs(m)
            jobs_alt = machines_alt.get_assigned_jobs(m)
            overdue_count = 0
            for s in range(2):
                if s == 0:
                    jobs_list = jobs_orig
                elif s == 1:
                    jobs_list = jobs_alt
                total_late = 0
                total_on_time = 0
                for j in range(len(jobs_list)):
                    job = jobs_list[j]
                    # job = Job()
                    job_deadline = job.get_Deadline()
                    job_end = job.get_End()
                    job_finished = job.get_Finished()
                    # find list of jobs that could be overdue
                    if job_deadline <= latest_end_date:
                        if (job_finished == False) or (job_end > job_deadline):
                            # job is late
                            # status = "late"
                            total_late += 1
                        else:
                            # job is on-time
                            # status = "on-time"
                            total_on_time += 1
                # print("Solution -", s, "Total Late -> ", total_late, "Total OnTime -> ", total_on_time)
                if s == 0:
                    solution0_late = total_late
                    solution0_ontime = total_on_time
                elif s == 1:
                    solution1_late = total_late
                    solution1_ontime = total_on_time
            
            # choose solution 0 if there are less late jobs, otherwise, choose solution 1
            if solution0_late < solution1_late:
                os_jobs = machines_orig.get_assigned_jobs(m)
                os_slots = machines_orig.get_timeslots_for_machine(m)
            elif solution0_late >= solution1_late:
                os_jobs = machines_alt.get_assigned_jobs(m)
                os_slots = machines_alt.get_timeslots_for_machine(m)
            
            for j in range(len(os_jobs)):
                curr_job = os_jobs[j]
                new_job = Job()

                new_job_num = curr_job.get_Job_Num()
                new_qty = curr_job.get_Qty()
                new_prod_hrs = curr_job.get_ProductionHours()
                new_deadline = curr_job.get_Deadline()
                new_status = curr_job.get_Status()
                new_po_num = curr_job.get_PO_Num()
                new_so_num = curr_job.get_SO_Num()
                new_po_price = curr_job.get_PO_Price()
                new_frame = curr_job.get_Frame()
                new_lbs = curr_job.get_Lbs()
                new_material_id = curr_job.get_Material_ID()
                new_material_name = curr_job.get_Material_Name()
                new_cost_per_lb = curr_job.get_Cost_Per_Pound()
                new_colorant_id = curr_job.get_Colorant_ID()
                new_colorant_name = curr_job.get_Colorant_Name()
                new_overall_color = curr_job.get_Overall_Color()
                new_machine_assignment = curr_job.get_Machine_Assignment()
                new_start = curr_job.get_Start()
                new_end = curr_job.get_End()
                new_finished = curr_job.get_Finished()

                new_job.set_Job_Num(new_job_num)
                new_job.set_Qty(new_qty)
                new_job.set_ProductionHours(new_prod_hrs)
                new_job.set_Deadline(new_deadline)
                new_job.set_Status(new_status)
                new_job.set_PO_Num(new_po_num)
                new_job.set_SO_Num(new_so_num)
                new_job.set_PO_Price(new_po_price)
                new_job.set_Frame(new_frame)
                new_job.set_Lbs(new_lbs)
                new_job.set_Material_ID(new_material_id)
                new_job.set_Material_Name(new_material_name)
                new_job.set_Cost_Per_Pound(new_cost_per_lb)
                new_job.set_Colorant_ID(new_colorant_id)
                new_job.set_Colorant_Name(new_colorant_name)
                new_job.set_Overall_Color(new_overall_color)
                new_job.set_Machine_Assignment(new_machine_assignment)
                new_job.set_Start(new_start)
                new_job.set_End(new_end)
                new_job.set_Finished(new_finished)

                machines_os.assign_job(m, new_job)

            for s in range(len(os_slots)):
                curr_slot = os_slots[s]
                new_slot = Slot()

                new_slot_start = curr_slot.get_start()
                new_slot_end = curr_slot.get_end()
                new_slot_availability = curr_slot.get_availability()
                new_slot_assignment = curr_slot.get_assignment()

                new_slot.set_start(new_slot_start)
                new_slot.set_end(new_slot_end)
                new_slot.set_availability(new_slot_availability)
                new_slot.set_assignment(new_slot_assignment)

                if m == 1:
                    machines_os.mach2_slot[s] = new_slot
                elif m == 2:
                    machines_os.mach5_slot[s] = new_slot
                elif m == 3:
                    machines_os.mach6_slot[s] = new_slot
                elif m == 4:
                    machines_os.mach9_slot[s] = new_slot
                
        return machines_os
    # need to change the 25 hr thing