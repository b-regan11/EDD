from datetime import datetime, timedelta
import os
import pandas as pd
from UrgencyList import UrgencyList
from Machines import Machines
from Changeover import Changeover

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
        
        machine_start_times = []    # this should be obsolete by the time solution0 is done
        # machineA start times should be used until its empty, then machineB start times

        machineA_start_times = []
        machineB_start_times = []

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            # print("Urgency List -> ", UL)
            for j in range(UL_JobCount):
                # print("Job Before-> ", j, " | List -> ", UL)
                # calculate slots based on prod hrs
                job_slots = machines.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=urgency_list.get_job_prod_hours(UL, j)))
                # print("Job Slots -> ", job_slots)

                # ---------- Frame Implementation --------------------
                frame_name = urgency_list.get_job_frame(UL, j)
                frame_num = machines.get_frame_index_by_name(frame_name)
                if frame_num == None:
                    # print("no frame so it should skip")
                    continue
                else:
                    # print(frame_name, " -> is index -> ", frame_num)
                    MA1 = machines.get_frame_tierA1_machine(frame_num)
                    MA2 = machines.get_frame_tierA2_machine(frame_num)
                    MB = machines.get_frame_tierB_machine(frame_num)
                    # if MA1 != 0:
                    #     print("Machine -> ", MA1, " | is Tier A1 for frame -> ", frame_name)
                    # if MA2 != 0:
                    #     print("Machine -> ", MA2, " | is Tier A2 for frame -> ", frame_name)
                    # if MB != 0:
                    #     print("Machine -> ", MB, " | is Tier B for frame -> ", frame_name)
                
                # ---------- Frame Implementation Done --------------------
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
                
                machine_start_times.clear()
                # if a machine is full, it will not be selectable
                if machines.is_machine_full(1) == False:
                    if MA1 == 1:
                        machine_start_times.append(('MA1', mach2curr_start))
                    if MA2 == 1:
                        machine_start_times.append(('MA2', mach2curr_start))
                    if MB == 1: # If MB == 1 && MA1 & MA2 are full
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2): #if MA1 and MA2 are full
                                machine_start_times.append(('MB', mach2curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): #if MA1 is full
                                machine_start_times.append(('MB', mach2curr_start))
        
                if machines.is_machine_full(2) == False:
                    if MA1 == 2:
                        machine_start_times.append(('MA1', mach5curr_start))
                    if MA2 == 2:
                        machine_start_times.append(('MA2', mach5curr_start))
                    if MB == 2:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach5curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach5curr_start))

                if machines.is_machine_full(3) == False:
                    if MA1 == 3:
                        machine_start_times.append(('MA1', mach6curr_start))
                    if MA2 == 3:
                        machine_start_times.append(('MA2', mach6curr_start))
                    if MB == 3:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach6curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach6curr_start))

                if machines.is_machine_full(4) == False:
                    if MA1 == 4:
                        machine_start_times.append(('MA1', mach9curr_start))
                    if MA2 == 4:
                        machine_start_times.append(('MA2', mach9curr_start))
                    if MB == 4:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach9curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach9curr_start))

                # find earliest start time of all machines
                machine_start_times.sort(key=lambda tup: tup[1])
                if len(machine_start_times) == 0:
                    break
                first_mach, first_start = machine_start_times[0]

                if first_mach == "MA1":
                    if MA1 == 1:
                        current_machine = 1
                    elif MA1 == 2:
                        current_machine = 2
                    elif MA1 == 3:
                        current_machine = 3
                    elif MA1 == 4:
                        current_machine = 4

                elif first_mach == "MA2":
                    if MA2 == 1:
                        current_machine = 1
                    elif MA2 == 2:
                        current_machine = 2
                    elif MA2 == 3:
                        current_machine = 3
                    elif MA2 == 4:
                        current_machine = 4
                    
                elif first_mach == "MB":
                    if MB == 1:
                        current_machine = 1
                    elif MB == 2:
                        current_machine = 2
                    elif MB == 3:
                        current_machine = 3
                    elif MB == 4:
                        current_machine = 4
                
                    
                # print("current machine before changeover -> ", current_machine)
                # ----------Changeover should be implemented here-----------

                for ch in range(4):
                    if ch == 0:
                        if first_mach == "MA1":
                            if MA1 == 1:
                                changeover_start = machines.get_start_time(current_machine, mach2_curr_slot)    
                            elif MA1 == 2:
                                changeover_start = machines.get_start_time(current_machine, mach5_curr_slot)    
                            elif MA1 == 3:
                                changeover_start = machines.get_start_time(current_machine, mach6_curr_slot)    
                            elif MA1 == 4:
                                changeover_start = machines.get_start_time(current_machine, mach9_curr_slot)    

                        elif first_mach == "MA2":
                            if MA2 == 1:
                                changeover_start = machines.get_start_time(current_machine, mach2_curr_slot)    
                            elif MA2 == 2:
                                changeover_start = machines.get_start_time(current_machine, mach5_curr_slot)    
                            elif MA2 == 3:
                                changeover_start = machines.get_start_time(current_machine, mach6_curr_slot)    
                            elif MA2 == 4:
                                changeover_start = machines.get_start_time(current_machine, mach9_curr_slot)    
                        
                        elif first_mach == "MB":
                            if MB == 1:
                                changeover_start = machines.get_start_time(current_machine, mach2_curr_slot)    
                            elif MB == 2:
                                changeover_start = machines.get_start_time(current_machine, mach5_curr_slot)    
                            elif MB == 3:
                                changeover_start = machines.get_start_time(current_machine, mach6_curr_slot)    
                            elif MB == 4:
                                changeover_start = machines.get_start_time(current_machine, mach9_curr_slot)    

                    if first_mach == "MA1":
                        if MA1 == 1:
                            changeover_end = machines.get_end_time(current_machine, mach2_curr_slot)    
                        elif MA1 == 2:
                            changeover_end = machines.get_end_time(current_machine, mach5_curr_slot)    
                        elif MA1 == 3:
                            changeover_end = machines.get_end_time(current_machine, mach6_curr_slot)    
                        elif MA1 == 4:
                            changeover_end = machines.get_end_time(current_machine, mach9_curr_slot)    

                    elif first_mach == "MA2":
                        if MA2 == 1:
                            changeover_end = machines.get_end_time(current_machine, mach2_curr_slot)    
                        elif MA2 == 2:
                            changeover_end = machines.get_end_time(current_machine, mach5_curr_slot)    
                        elif MA2 == 3:
                            changeover_end = machines.get_end_time(current_machine, mach6_curr_slot)    
                        elif MA2 == 4:
                            changeover_end = machines.get_end_time(current_machine, mach9_curr_slot)
                    
                    elif first_mach == "MB":
                        if MB == 1:
                            changeover_end = machines.get_end_time(current_machine, mach2_curr_slot)    
                        elif MB == 2:
                            changeover_end = machines.get_end_time(current_machine, mach5_curr_slot)    
                        elif MB == 3:
                            changeover_end = machines.get_end_time(current_machine, mach6_curr_slot)    
                        elif MB == 4:
                            changeover_end = machines.get_end_time(current_machine, mach9_curr_slot)
                
                    changeover = Changeover()
                    changeover.set_start(changeover_start)
                    changeover.set_end(changeover_end)
                    changeover.set_jobB_num(urgency_list.get_job(UL, j))
                    # print("Changeover Start: ", changeover.Start)
                    # print("Changeover End: ", changeover.End) 
                
                    if first_mach == "MA1":
                        if MA1 == 1:
                            machines.set_availability(current_machine, mach2_curr_slot, True)
                            machines.set_assignment(current_machine, mach2_curr_slot, changeover)
                        elif MA1 == 2:
                            machines.set_availability(current_machine, mach5_curr_slot, True)
                            machines.set_assignment(current_machine, mach5_curr_slot, changeover)
                        elif MA1 == 3:
                            machines.set_availability(current_machine, mach6_curr_slot, True)
                            machines.set_assignment(current_machine, mach6_curr_slot, changeover)
                        elif MA1 == 4:
                            machines.set_availability(current_machine, mach9_curr_slot, True)
                            machines.set_assignment(current_machine, mach9_curr_slot, changeover)
                            #machines.set_assignment(current_machine, mach9_curr_slot, urgency_list.get_job(UL, j))
                    
                    elif first_mach == "MA2":
                        if MA2 == 1:
                            machines.set_availability(current_machine, mach2_curr_slot, True)
                            machines.set_assignment(current_machine, mach2_curr_slot, changeover)
                        elif MA2 == 2:
                            machines.set_availability(current_machine, mach5_curr_slot, True)
                            machines.set_assignment(current_machine, mach5_curr_slot, changeover)
                        elif MA2 == 3:
                            machines.set_availability(current_machine, mach6_curr_slot, True)
                            machines.set_assignment(current_machine, mach6_curr_slot, changeover)
                        elif MA2 == 4:
                            machines.set_availability(current_machine, mach9_curr_slot, True)
                            machines.set_assignment(current_machine, mach9_curr_slot, changeover)

                    elif first_mach == "MB":
                        if MB == 1:
                            machines.set_availability(current_machine, mach2_curr_slot, True)
                            machines.set_assignment(current_machine, mach2_curr_slot, )
                        elif MB == 2:
                            machines.set_availability(current_machine, mach5_curr_slot, True)
                            machines.set_assignment(current_machine, mach5_curr_slot, changeover)
                        elif MB == 3:
                            machines.set_availability(current_machine, mach6_curr_slot, True)
                            machines.set_assignment(current_machine, mach6_curr_slot, changeover)
                        elif MB == 4:
                            machines.set_availability(current_machine, mach9_curr_slot, True)
                            machines.set_assignment(current_machine, mach9_curr_slot, changeover)
                    
                    if machines.get_last_timeslot(current_machine) == changeover.End:
                        if current_machine == 1:
                            print("Machine 2 is full")
                        elif current_machine == 2:
                            print("Machine 5 is full")
                        elif current_machine == 3:
                            print("Machine 6 is full")
                        elif current_machine == 4:
                            print("Machine 9 is full")
                        machines.set_machine_full(current_machine,True)
                        # machines.assign_job(current_machine, urgency_list.get_job(UL, j))

                        if first_mach == "MA1":
                            if MA1 == 1:
                                mach2_curr_slot += 1
                            elif MA1 == 2:
                                mach5_curr_slot += 1
                            elif MA1 == 3:
                                mach6_curr_slot += 1
                            elif MA1 == 4:
                                mach9_curr_slot += 1
                        
                        elif first_mach == "MA2":
                            if MA2 == 1:
                                mach2_curr_slot += 1
                            elif MA2 == 2:
                                mach5_curr_slot += 1
                            elif MA2 == 3:
                                mach6_curr_slot += 1
                            elif MA2 == 4:
                                mach9_curr_slot += 1

                        elif first_mach == "MB":
                            if MB == 1:
                                mach2_curr_slot += 1
                            elif MB == 2:
                                mach5_curr_slot += 1
                            elif MB == 3:
                                mach6_curr_slot += 1
                            elif MB == 4:
                                mach9_curr_slot += 1
                        break

                    if first_mach == "MA1":
                        if MA1 == 1:
                            mach2_curr_slot += 1
                        elif MA1 == 2:
                            mach5_curr_slot += 1
                        elif MA1 == 3:
                            mach6_curr_slot += 1
                        elif MA1 == 4:
                            mach9_curr_slot += 1
                    
                    elif first_mach == "MA2":
                        if MA2 == 1:
                            mach2_curr_slot += 1
                        elif MA2 == 2:
                            mach5_curr_slot += 1
                        elif MA2 == 3:
                            mach6_curr_slot += 1
                        elif MA2 == 4:
                            mach9_curr_slot += 1

                    elif first_mach == "MB":
                        if MB == 1:
                            mach2_curr_slot += 1
                        elif MB == 2:
                            mach5_curr_slot += 1
                        elif MB == 3:
                            mach6_curr_slot += 1
                        elif MB == 4:
                            mach9_curr_slot += 1
                
                machine_start_times.clear()
                # if a machine is full, it will not be selectable
                if machines.is_machine_full(1) == False:
                    if MA1 == 1:
                        machine_start_times.append(('MA1', mach2curr_start))
                    if MA2 == 1:
                        machine_start_times.append(('MA2', mach2curr_start))
                    if MB == 1:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach2curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach2curr_start))

                if machines.is_machine_full(2) == False:
                    if MA1 == 2:
                        machine_start_times.append(('MA1', mach5curr_start))
                    if MA2 == 2:
                        machine_start_times.append(('MA2', mach5curr_start))
                    if MB == 2:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach5curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach5curr_start))

                if machines.is_machine_full(3) == False:
                    if MA1 == 3:
                        machine_start_times.append(('MA1', mach6curr_start))
                    if MA2 == 3:
                        machine_start_times.append(('MA2', mach6curr_start))
                    if MB == 3:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach6curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach6curr_start))

                if machines.is_machine_full(4) == False:
                    if MA1 == 4:
                        machine_start_times.append(('MA1', mach9curr_start))
                    if MA2 == 4:
                        machine_start_times.append(('MA2', mach9curr_start))
                    if MB == 4:
                        if MA2 > 0: 
                            if machines.is_machine_full(MA1) and machines.is_machine_full(MA2):
                                machine_start_times.append(('MB', mach9curr_start))
                        elif MA2 == 0: 
                            if machines.is_machine_full(MA1): 
                                machine_start_times.append(('MB', mach9curr_start))
                
                # find earliest start time of all machines
                machine_start_times.sort(key=lambda tup: tup[1])
                if len(machine_start_times) == 0:
                    break
                first_mach, first_start = machine_start_times[0]
                
                prev_machine = current_machine
                if first_mach == "MA1":
                    if MA1 == 1:
                        current_machine = 1
                    elif MA1 == 2:
                        current_machine = 2
                    elif MA1 == 3:
                        current_machine = 3
                    elif MA1 == 4:
                        current_machine = 4
                
                elif first_mach == "MA2":
                    if MA2 == 1:
                        current_machine = 1
                    elif MA2 == 2:
                        current_machine = 2
                    elif MA2 == 3:
                        current_machine = 3
                    elif MA2 == 4:
                        current_machine = 4
                
                elif first_mach == "MB":
                    if MB == 1:
                        current_machine = 1
                    elif MB == 2:
                        current_machine = 2
                    elif MB == 3:
                        current_machine = 3
                    elif MB == 4:
                        current_machine = 4

                # print("current machine after changeover -> ", current_machine)

                # ----------Changeover should be ended here-----------
                # print("Job After-> ", j, " | List -> ", UL)
                if prev_machine == current_machine:
                    urgency_list.set_job_machine_assignment(UL, j, current_machine) # set the job to machine 
                    for sc in range(job_slots - 1):
                        if sc == 0:
                            # set the start time for job j in list UL
                            if first_mach == "MA1":
                                if MA1 == 1:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach2_curr_slot))
                                elif MA1 == 2:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach5_curr_slot))
                                elif MA1 == 3:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach6_curr_slot))
                                elif MA1 == 4:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach9_curr_slot))
                            
                            elif first_mach == "MA2":
                                if MA2 == 1:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach2_curr_slot))
                                elif MA2 == 2:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach5_curr_slot))
                                elif MA2 == 3:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach6_curr_slot))
                                elif MA2 == 4:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach9_curr_slot))
                            
                            elif first_mach == "MB":
                                if MB == 1:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach2_curr_slot))
                                elif MB == 2:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach5_curr_slot))
                                elif MB == 3:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach6_curr_slot))
                                elif MB == 4:
                                    urgency_list.set_job_start(UL, j, machines.get_start_time(current_machine, mach9_curr_slot))
                            
                        # set the end time for job j in list UL
                        if first_mach == "MA1":
                            if MA1 == 1:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach2_curr_slot))
                            elif MA1 == 2:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach5_curr_slot))
                            elif MA1 == 3:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach6_curr_slot))
                            elif MA1 == 4:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach9_curr_slot))
                        
                        elif first_mach == "MA2":
                            if MA2 == 1:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach2_curr_slot))
                            elif MA2 == 2:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach5_curr_slot))
                            elif MA2 == 3:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach6_curr_slot))
                            elif MA2 == 4:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach9_curr_slot))
                        
                        elif first_mach == "MB":
                            if MB == 1:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach2_curr_slot))
                            elif MB == 2:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach5_curr_slot))
                            elif MB == 3:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach6_curr_slot))
                            elif MB == 4:
                                urgency_list.set_job_end(UL, j, machines.get_end_time(current_machine, mach9_curr_slot))
                        # print("Job -> ", urgency_list.get_job_num(UL, j), " | Start -> ", urgency_list.get_job_start(UL, j), " | End -> ", urgency_list.get_job_end(UL, j))


                        if first_mach == "MA1":
                            if MA1 == 1:
                                machines.set_availability(current_machine, mach2_curr_slot, True)
                                machines.set_assignment(current_machine, mach2_curr_slot, urgency_list.get_job(UL, j))    
                            elif MA1 == 2:
                                machines.set_availability(current_machine, mach5_curr_slot, True)
                                machines.set_assignment(current_machine, mach5_curr_slot, urgency_list.get_job(UL, j))
                            elif MA1 == 3:
                                machines.set_availability(current_machine, mach6_curr_slot, True)
                                machines.set_assignment(current_machine, mach6_curr_slot, urgency_list.get_job(UL, j))
                            elif MA1 == 4:
                                machines.set_availability(current_machine, mach9_curr_slot, True)
                                machines.set_assignment(current_machine, mach9_curr_slot, urgency_list.get_job(UL, j))
                        
                        elif first_mach == "MA2":
                            if MA2 == 1:
                                machines.set_availability(current_machine, mach2_curr_slot, True)
                                machines.set_assignment(current_machine, mach2_curr_slot, urgency_list.get_job(UL, j))    
                            elif MA2 == 2:
                                machines.set_availability(current_machine, mach5_curr_slot, True)
                                machines.set_assignment(current_machine, mach5_curr_slot, urgency_list.get_job(UL, j))
                            elif MA2 == 3:
                                machines.set_availability(current_machine, mach6_curr_slot, True)
                                machines.set_assignment(current_machine, mach6_curr_slot, urgency_list.get_job(UL, j))
                            elif MA2 == 4:
                                machines.set_availability(current_machine, mach9_curr_slot, True)
                                machines.set_assignment(current_machine, mach9_curr_slot, urgency_list.get_job(UL, j))
                        
                        elif first_mach == "MB":
                            if MB == 1:
                                machines.set_availability(current_machine, mach2_curr_slot, True)
                                machines.set_assignment(current_machine, mach2_curr_slot, urgency_list.get_job(UL, j))    
                            elif MB == 2:
                                machines.set_availability(current_machine, mach5_curr_slot, True)
                                machines.set_assignment(current_machine, mach5_curr_slot, urgency_list.get_job(UL, j))
                            elif MB == 3:
                                machines.set_availability(current_machine, mach6_curr_slot, True)
                                machines.set_assignment(current_machine, mach6_curr_slot, urgency_list.get_job(UL, j))
                            elif MB == 4:
                                machines.set_availability(current_machine, mach9_curr_slot, True)
                                machines.set_assignment(current_machine, mach9_curr_slot, urgency_list.get_job(UL, j))
                        
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

                            if first_mach == "MA1":
                                if MA1 == 1:
                                    mach2_curr_slot += 1
                                elif MA1 == 2:
                                    mach5_curr_slot += 1
                                elif MA1 == 3:
                                    mach6_curr_slot += 1
                                elif MA1 == 4:
                                    mach9_curr_slot += 1

                            elif first_mach == "MA2":
                                if MA2 == 1:
                                    mach2_curr_slot += 1
                                elif MA2 == 2:
                                    mach5_curr_slot += 1
                                elif MA2 == 3:
                                    mach6_curr_slot += 1
                                elif MA2 == 4:
                                    mach9_curr_slot += 1

                            elif first_mach == "MB":
                                if MB == 1:
                                    mach2_curr_slot += 1
                                elif MB == 2:
                                    mach5_curr_slot += 1
                                elif MB == 3:
                                    mach6_curr_slot += 1
                                elif MB == 4:
                                    mach9_curr_slot += 1
                            break

                        if first_mach == "MA1":
                            if MA1 == 1:
                                mach2_curr_slot += 1
                            elif MA1 == 2:
                                mach5_curr_slot += 1
                            elif MA1 == 3:
                                mach6_curr_slot += 1
                            elif MA1 == 4:
                                mach9_curr_slot += 1

                        elif first_mach == "MA2":
                            if MA2 == 1:
                                mach2_curr_slot += 1
                            elif MA2 == 2:
                                mach5_curr_slot += 1
                            elif MA2 == 3:
                                mach6_curr_slot += 1
                            elif MA2 == 4:
                                mach9_curr_slot += 1

                        elif first_mach == "MB":
                            if MB == 1:
                                mach2_curr_slot += 1
                            elif MB == 2:
                                mach5_curr_slot += 1
                            elif MB == 3:
                                mach6_curr_slot += 1
                            elif MB == 4:
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
