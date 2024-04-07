from datetime import datetime, timedelta
import os
import pandas as pd
from UrgencyList import UrgencyList
from Machines import Machines

class BinPacking:
    def main(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times, earliest_start, latest_end, sorted_data):
        # Create an instance of UrgencyList
        urgency_list = UrgencyList()
        urgency_list.create(earliest_start, latest_end, sorted_data)
        print("UrgencyList job objects created")
        
        # Create an instance of Machines
        machines = Machines()
        machines.create(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times)
        print("Machine timeslots created")

        mach2_curr_slot = 0

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            for j in range(UL_JobCount):
                print("job j -> ", j)
                print("job_num -> ", urgency_list.get_job_num(UL, j))
                job_slots = machines.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=urgency_list.get_job_prod_hours(UL, j))) # calculate slots based on prod hrs
                print("job slots: ", job_slots)
                urgency_list.set_job_machine_assignment(UL, j, 1) # set the job to be machine 2
                for sc in range(job_slots - 1):
                    # urgency_list.get_job_end(UL, j)
                    if (urgency_list.get_job_end(UL, j) is not None) and (urgency_list.get_job_end(UL, j) == machines.get_last_timeslot(1)):
                        print("Iterations should stop here, machine is full")
                        exit(0)
                    if sc == 0:
                        urgency_list.set_job_start(UL, j, machines.get_start_time(1, mach2_curr_slot)) # set the start time for job j in list UL
                        print("Job Start is set: ", urgency_list.get_job_start(UL, j))
                    print("iteration start")
                    urgency_list.set_job_end(UL, j, machines.get_end_time(1, mach2_curr_slot)) # set the end time for job j in list UL
                    print("Job End is set: ", urgency_list.get_job_end(UL, j))
                    machines.set_availability(1, mach2_curr_slot, True)
                    print("Job Availability is set to True")
                    machines.set_assignment(1, j, urgency_list.get_job(UL, j))
                    print("Job Assignment is set: ")
                    mach2_curr_slot += 1
                    print("Timeslot Iteration: ", sc, " completed")
                machines.assign_job(2, urgency_list.get_job(UL, j)) # add job to the machine 2 job list
        print(machines.get_assigned_jobs())



                #------------- Work Below ------------------
                # # Calculate the number of slots the job should take up based on production hours
                # job_slots = machines.calculate_slot_count(datetime.now, datetime.now + urgency_list.get_job_prod_hours(UL, j))
                # for f in range(8):
                #     for m in range(1, 5):
                #         if machines.get_frame_type(m, f) == urgency_list.get_job_frame(UL, j):
                #             if machines.get_tier_a1(m, f):
                #                 MA1 = m # This represents the machine that is assigned to tier a1 for frame f
                #             if machines.get_tier_a2(m, f):
                #                 MA2 = m # This represents the machine that is assigned to tier a2 for frame f
                #             if machines.get_tier_b(m, f):
                #                 MB = m # This represents the machine that is assigned to tier b for frame f
                                
                # if MA1 == 1:
                #     MA1EarliestSlot = mach2EarliestSlot
                #     MA1Cutoff = mach2Cutoff
                # elif MA1 == 2:
                #     MA1EarliestSlot = mach5EarliestSlot
                #     MA1Cutoff = mach5Cutoff
                # elif MA1 == 3:
                #     MA1EarliestSlot = mach6EarliestSlot
                #     MA1Cutoff = mach6Cutoff
                # elif MA1 == 4:
                #     MA1EarliestSlot = mach9EarliestSlot
                #     MA1Cutoff = mach9Cutoff

                # if MA2 == 1:
                #     MA2EarliestSlot = mach2EarliestSlot
                #     MA2Cutoff = mach2Cutoff
                # elif MA2 == 2:
                #     MA2EarliestSlot = mach5EarliestSlot
                #     MA2Cutoff = mach5Cutoff
                # elif MA2 == 3:
                #     MA2EarliestSlot = mach6EarliestSlot
                #     MA2Cutoff = mach6Cutoff
                # elif MA2 == 4:
                #     MA2EarliestSlot = mach9EarliestSlot
                #     MA2Cutoff = mach9Cutoff

                # if MB == 1:
                #     MBEarliestSlot = mach2EarliestSlot
                #     MBCutoff = mach2Cutoff
                # elif MB == 2:
                #     MBEarliestSlot = mach5EarliestSlot
                #     MBCutoff = mach5Cutoff
                # elif MB == 3:
                #     MBEarliestSlot = mach6EarliestSlot
                #     MBCutoff = mach6Cutoff
                # elif MB == 4:
                #     MBEarliestSlot = mach9EarliestSlot
                #     MBCutoff = mach9Cutoff
                
                # # If the frame has both a tier A2 and tier B
                # if (MA2 is not None) and (MB is not None):
                #     # IF machines MA1 and MA2 are not full
                #         if MA1EarliestSlot == MA2EarliestSlot:
                #             # assign job j to machine MA1
                #             # machines.assign_job(MA1, j) # add to machine job list
                #             # for sc in range(job_slots): # machines.calculate_slot_count()

                            
                #         elif MA1EarliestSlot < MA2EarliestSlot:
                #             # assign job j to machine MA1
                            
                #         elif MA1EarliestSlot > MA2EarliestSlot:
                #             # assign job j to machine MA2
                            
                #     # If MA1 OR MA2 is full
                #         # assign job j to the machine that is not full
                #     # If MA1 AND MA2 are full but MB is not full
                #         # assign job j to machine MB
                #     # If MA1, MA2, and MB are all full
                #         # skip job j, assign to no machine
                
                # # If the frame has a tier A2 but no tier B
                # elif (MA2 is not None) and (MB is None):
                #     # IF machines MA1 and MA2 are not full
                #         if MA1EarliestSlot == MA2EarliestSlot:
                #             # assign job j to machine MA1
                            
                #         elif MA1EarliestSlot < MA2EarliestSlot:
                #             # assign job j to machine MA1
                            
                #         elif MA1EarliestSlot > MA2EarliestSlot:
                #             # assign job j to machine MA2
                            
                #     # If MA1 OR MA2 is full
                #         # assign job j to the machine that is not full
                #     # If MA1 AND MA2 are full
                #         # skip job j, assign to no machine
                
                # # If the frame has a tier B but no tier A2
                # elif (MA2 is None) and (MB is not None):
                #     # If machine MA1 is not full:
                #         # assign job j to machine MA1
                #     # If machine MA1 is full but MB is not full:
                #         # assign job j to machine MB
                #     # If machine MA1 and MB are both full:
                #         # skip job j, assign to no machine

                # # If the frame has no tier A2 and no tier B
                # elif (MA2 is None) and (MB is None):
                #     # If machine MA1 is not full:
                #         # assign job j to machine MA1
                #     # If machine MA1 is full:
                #         # skip job j, assign to no machine
                    