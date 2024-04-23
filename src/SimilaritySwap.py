from datetime import datetime, timedelta
import os
import pandas as pd
from UrgencyList import UrgencyList
from Machines import Machines
from Changeover import Changeover
from BinPacking import BinPacking

class SimilaritySwap:
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

            # This is a method for verifying jobs by job_num
            for i in range(len(FromTo_MachJobs)):
                for j in range(len(FromTo_MachJobs[i])):
                    # if (FromTo_MachJobs[i][j] is not int) and (FromTo_MachJobs[i][j] is not "FromTo"):
                    if ((i >= 1) and (j == 0)) or ((i == 0) and (j >= 1)):
                        Job_Obj = FromTo_MachJobs[i][j]
                        Job_Num = machines.get_assigned_job_num(m, Job_Obj)
                        if m == 1:
                            FromTo_Mach2Jobs[i][j] = Job_Num
                        elif m == 2:
                            FromTo_Mach5Jobs[i][j] = Job_Num
                        elif m == 3:
                            FromTo_Mach6Jobs[i][j] = Job_Num
                        elif m == 4:
                            FromTo_Mach9Jobs[i][j] = Job_Num
        
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
        
    def reorder(FromTo_Mach2Jobs, FromTo_Mach5Jobs, FromTo_Mach6Jobs, FromTo_Mach9Jobs, iteration):
        if isinstance(iteration, int):
            print("This will be solution-", iteration)
        else:
            print("Iteration value needs to be an integer")
            exit(0)
        
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
            print("------- Machine ", mach_name, " -------------------------")
            print("Here is the original earliest due date job order -> ", Original_Job_Order)
            print("Here is the proposed alternative job order -> ", New_Job_Order)
            if m == 1:
                Mach2_New_Order = New_Job_Order
            elif m == 2:
                Mach5_New_Order = New_Job_Order
            elif m == 3:
                Mach6_New_Order = New_Job_Order
            elif m == 4:
                Mach9_New_Order = New_Job_Order
            
        return Mach2_New_Order, Mach5_New_Order, Mach6_New_Order, Mach9_New_Order


