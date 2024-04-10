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
        
        # Create an instance of Machines
        machines = Machines()
        machines.create(mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times)

        mach2_curr_slot = 0
        mach5_curr_slot = 0
        mach6_curr_slot = 0
        mach9_curr_slot = 0

        mach2curr_start = None
        mach5curr_start = None
        mach6curr_start = None
        mach9curr_start = None

        current_machine = 1 # No machine by default

        machine_start_times = []

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            for j in range(UL_JobCount):
                # calculate slots based on prod hrs
                job_slots = machines.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=urgency_list.get_job_prod_hours(UL, j)))
                # find the machine with the earliest start time, until frames are implemented ...
                # ... if there is a tie, go with smallest number: m2 -> m5 -> m6 -> m9.
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

                machine_start_times.sort(key=lambda tup: tup[1])
                if len(machine_start_times) == 0:
                    break
                first_mach, first_start = machine_start_times[0]

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

                urgency_list.set_job_machine_assignment(UL, j, current_machine) # set the job to be machine 2
                for sc in range(job_slots - 1):
                    if sc == 0:
                        # set the start time for job j in list UL
                        if first_mach == "M2":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach2_curr_slot))
                        elif first_mach == "M5":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach5_curr_slot))
                        elif first_mach == "M6":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach6_curr_slot))
                        elif first_mach == "M9":
                            urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach9_curr_slot))
                    # set the end time for job j in list UL
                    if first_mach == "M2":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach2_curr_slot)) 
                    elif first_mach == "M5":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach5_curr_slot)) 
                    elif first_mach == "M6":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach6_curr_slot)) 
                    elif first_mach == "M9":
                        urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach9_curr_slot)) 

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
            
                # add job to the machine job list
                machines.assign_job(current_machine, urgency_list.get_job(UL, j))
                
        print("\nAlgorithm Finished\n")
        print("Below is the full list of assigned jobs: \n")
        print("jobs on machine 2: ", machines.get_assigned_job_nums(1))
        print("jobs on machine 5: ", machines.get_assigned_job_nums(2))
        print("jobs on machine 6: ", machines.get_assigned_job_nums(3))
        print("jobs on machine 9: ", machines.get_assigned_job_nums(4))
        
        for m in range (1, 5):
            machine_jobs = machines.get_assigned_job_nums(m)
            if m == 1:
                print("\nMachine 2\n")
            elif m == 2:
                print("\nMachine 5\n")
            elif m == 3:
                print("\nMachine 6\n")
            elif m == 4:
                print("\nMachine 9\n")
            for j in range(len(machine_jobs)):
                jobObj = machines.jobs_assigned[m]
                print("Job: ", machine_jobs[j], " | StartTime -> ", machines.get_assigned_job_start(m, jobObj[j]), " | EndTime -> ", machines.get_assigned_job_end(m, jobObj[j]))


# PLEASE READ...
        # Everything above works fine
        # Each job is cycled through and assigned to a machine until each machine is full
        # Next step is to add in the changeover time
        # After that, frame constraints should be implemented
        # When all machines are implemented, including frame constraints, solution0 is complete