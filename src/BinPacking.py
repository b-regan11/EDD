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
        mach5_curr_slot = 0
        mach6_curr_slot = 0
        mach9_curr_slot = 0

        mach2curr_start = None
        mach5curr_start = None
        mach6curr_start = None
        mach9curr_start = None

        current_machine = 1 # No machine by default

        prev_UL = 0
        prev_job_index = 0

        machine_start_times = []

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            print("UL List: ", UL)
            print("UL Job Count: ", UL_JobCount)
            for j in range(UL_JobCount):
                # calculate slots based on prod hrs
                job_slots = machines.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=urgency_list.get_job_prod_hours(UL, j)))
                print("Job j, # of job_slots = ", job_slots)
                # find the machine with the earliest start time, if there is a tie, go with smallest number: m2 -> m5 -> m6 -> m9.
                # get the start time of each machine
                if machines.is_machine_full(1) == False:
                    mach2curr_start = machines.get_start_time(1, mach2_curr_slot)
                if machines.is_machine_full(2) == False:
                    mach5curr_start = machines.get_start_time(2, mach5_curr_slot)
                if machines.is_machine_full(3) == False:
                    mach6curr_start = machines.get_start_time(3, mach6_curr_slot)
                if machines.is_machine_full(4) == False:
                    mach9curr_start = machines.get_start_time(4, mach9_curr_slot)
                
                # find earliest start time of all machines
                machine_start_times.clear()
                # if a machine is full, it will not be selectable
                if machines.is_machine_full(1) == False:
                    machine_start_times.append(('M2', mach2curr_start))
                if machines.is_machine_full(2) == False:
                    machine_start_times.append(('M5', mach5curr_start))
                if machines.is_machine_full(3) == False:
                    machine_start_times.append(('M6', mach6curr_start))
                if machines.is_machine_full(4) == False:
                    machine_start_times.append(('M9', mach9curr_start))

                #machine_start_times = [('M2', mach2curr_start), ('M5', mach5curr_start), ('M6', mach6curr_start), ('M9', mach9curr_start), ]
                machine_start_times.sort(key=lambda tup: tup[1])
                print()
                if len(machine_start_times) == 0:
                    break
                print(machine_start_times[0])
                print()
                print("machine start times -> ", machine_start_times)
                
                # display the machine with the earliest timeslot
                first_mach, first_start = machine_start_times[0]
                # second_mach, second_start = machine_start_times[1]
                # third_mach, third_start = machine_start_times[2]
                # fourth_mach, fourth_start = machine_start_times[3]

                if first_mach == "M2":
                    current_machine = 1
                    current_machine_slot = mach2_curr_slot
                elif first_mach == "M5":
                    current_machine = 2
                    current_machine_slot = mach5_curr_slot
                elif first_mach == "M6":
                    current_machine = 3
                    current_machine_slot = mach6_curr_slot
                elif first_mach == "M9":
                    current_machine = 4
                    current_machine_slot = mach9_curr_slot
                
                # print(f"Machine: {first_mach} has the earliest start time: {first_start}")
                # print(f"Machine: {second_mach} has the earliest start time: {second_start}")
                # print(f"Machine: {third_mach} has the earliest start time: {third_start}")
                # print(f"Machine: {fourth_mach} has the earliest start time: {fourth_start}")

                urgency_list.set_job_machine_assignment(UL, j, current_machine) # set the job to be machine 2
                for sc in range(job_slots - 1):
                    print("Earliest Start to choose: ", current_machine)
                    # if the last job's end time is equal to the last timeslot's end time, stop the loop
                    
                    # if (urgency_list.get_job_end(prev_UL, prev_job_index) is not None) and (urgency_list.get_job_end(prev_UL, prev_job_index) == machines.get_last_timeslot(current_machine)):
                    #     print("------------- Exit Loop ------------")
                    #     print("Machine 2 Jobs -> ", machines.get_assigned_job_nums(1))
                    #     print("Machine 5 Jobs -> ", machines.get_assigned_job_nums(2))
                    #     print("Machine 6 Jobs -> ", machines.get_assigned_job_nums(3))
                    #     print("Machine 9 Jobs -> ", machines.get_assigned_job_nums(4))
                    #     # machine_start_times = [(name, value) for name, value in machine_start_times if name != first_mach]
                    #     # if len(machine_start_times) == 0:
                    #     #     exit(0)
                    #     exit(0)
                    if sc == 0:
                        # set the start time for job j in list UL
                        print("Right before line")
                        if first_mach == "M2":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach2_curr_slot))
                        elif first_mach == "M5":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach5_curr_slot))
                        elif first_mach == "M6":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach6_curr_slot))
                        elif first_mach == "M9":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach9_curr_slot))
                        print("Past the line")
                        print("Job Start: ", urgency_list.get_job_start(UL ,j))
                    # set the end time for job j in list UL
                    if first_mach == "M2":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach2_curr_slot)) 
                        print("Job End: ", urgency_list.get_job_end(UL ,j))
                    elif first_mach == "M5":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach5_curr_slot)) 
                        print("Job End: ", urgency_list.get_job_end(UL ,j))
                    elif first_mach == "M6":
                        print(machines.get_end_time(current_machine, mach6_curr_slot)) # this and the line below don't work when the machine is full
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach6_curr_slot)) 
                    elif first_mach == "M9":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach9_curr_slot)) 
                        print("Job End: ", urgency_list.get_job_end(UL ,j))

                    if first_mach == "M2":
                        machines.set_availability(current_machine, mach2_curr_slot, True)
                    elif first_mach == "M5":
                        machines.set_availability(current_machine, mach5_curr_slot, True)
                    elif first_mach == "M6":
                        machines.set_availability(current_machine, mach6_curr_slot, True)
                    elif first_mach == "M9":
                        machines.set_availability(current_machine, mach9_curr_slot, True)
                    
                    machines.set_assignment(current_machine, j, urgency_list.get_job(UL, j))
                    if machines.get_last_timeslot(current_machine) == urgency_list.get_job_end(UL ,j):
                        print("Should stop here")
                        if current_machine == 1:
                            print("Machine 2 is full")
                        elif current_machine == 2:
                            print("Machine 5 is full")
                        elif current_machine == 3:
                            print("Machine 6 is full")
                        elif current_machine == 4:
                            print("Machine 9 is full")

                        machines.set_machine_full(current_machine,True)

                        if first_mach == "M2":
                            mach2_curr_slot += 1    
                        elif first_mach == "M5":
                            mach5_curr_slot += 1
                        elif first_mach == "M6":
                            mach6_curr_slot += 1
                        elif first_mach == "M9":
                            mach9_curr_slot += 1
                        
                        break

                    if first_mach == "M2":
                        mach2_curr_slot += 1    
                    elif first_mach == "M5":
                        mach5_curr_slot += 1
                    elif first_mach == "M6":
                        mach6_curr_slot += 1
                    elif first_mach == "M9":
                        mach9_curr_slot += 1

                    prev_job_index = j
                # add job to the machine 2 job list
                machines.assign_job(current_machine, urgency_list.get_job(UL, j))
            prev_UL = UL
        print("jobs on machine 2: ", machines.get_assigned_job_nums(1))
        print("jobs on machine 5: ", machines.get_assigned_job_nums(2))
        print("jobs on machine 6: ", machines.get_assigned_job_nums(3))
        print("jobs on machine 9: ", machines.get_assigned_job_nums(4))
        print("\nAlgorithm Finished")


# PLEASE READ...
        # Everything above works fine
        # Next step is to add multiple machines. Multiple machines should be filled.
        # Also need to add in the changeover time
        # After that, frame constraints should be implemented
        # When all machines are implemented, including frame constraints, solution0 is complete



#-------------Previous Work Below ------------------
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
