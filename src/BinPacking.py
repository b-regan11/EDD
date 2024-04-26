from datetime import datetime, timedelta
import os
import pandas as pd
import numpy as np
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

        current_machine = 1 # default
        
        machine_start_times = []

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            # print("Urgency List -> ", UL)
            for j in range(UL_JobCount):
                # print("Job Before-> ", j, " | List -> ", UL)
                # calculate slots based on prod hrs for job j
                job_slots = machines.calculate_slot_count(datetime.now(), datetime.now() + timedelta(hours=urgency_list.get_job_prod_hours(UL, j)))
                # print("Job -> ", urgency_list.get_job_num(UL, j), " | Job Slots -> ", job_slots)

                # ---------- Frame Implementation --------------------
                frame_name = urgency_list.get_job_frame(UL, j)
                frame_num = machines.get_frame_index_by_name(frame_name)
                # if there is no frame for the job
                if frame_num == None:
                    continue
                else:
                    # print(frame_name, " -> is index -> ", frame_num)
                    MA1 = machines.get_frame_tierA1_machine(frame_num)
                    MA2 = machines.get_frame_tierA2_machine(frame_num)
                    MB = machines.get_frame_tierB_machine(frame_num)

                # ---------- Frame Implementation Done --------------------
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
                    continue
                first_mach, first_start = machine_start_times[0]
                # print("Here is the first machine -> ", first_mach)
                # print("MA1 -> ", MA1, " | MA2 -> ", MA2, " | MB -> ", MB)

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
                        urgency_list.set_job_start(UL, j, changeover_start)
                        urgency_list.set_job_end(UL, j, changeover_end)
                        urgency_list.set_job_machine_assignment(UL, j, current_machine)
                        urgency_list.set_job_finished(UL, j, False)
                        if pd.isna(urgency_list.get_job_colorant_id(UL, j)):
                            if "light gray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "light grey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "lightgray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "lightgrey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "soft gray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "soft grey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "softgray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "softgrey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "light blue" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightblue")
                            elif "lightblue" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightblue")
                            elif "sky blue" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "skyblue" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "weathered bronze" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                            elif "weatheredbronze" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                            elif "light coral" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "lightcoral" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "dark gray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "dark grey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "darkgray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "darkgrey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "weathered brown" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                            elif "weatheredbrown" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                            elif "clear" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "clear")
                            elif "natural" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "natural")
                            elif "white" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "white")
                            elif "gray" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "gray")
                            elif "grey" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "grey")
                            elif "silver" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "silver")
                            elif "aqua" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "aqua")
                            elif "blue" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "blue")
                            elif "teal" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "teal")
                            elif "green" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "green")
                            elif "purple" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "purple")
                            elif "violet" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "violet")
                            elif "red" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "red")
                            elif "magenta" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "magenta")
                            elif "pink" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "pink")
                            elif "orange" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "orange")
                            elif "tangerine" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "tangerine")
                            elif "yellow" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "yellow")
                            elif "tan" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "tan")
                            elif "biege" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "biege")
                            elif "brown" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "brown")
                            elif "smoke" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "smoke")
                            elif "black" in urgency_list.get_job_material_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "black")
                            else:
                                urgency_list.set_job_overall_color(UL, j, "unknown")
                        else:
                            if "light gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "light grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "lightgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "lightgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightgrey")
                            elif "soft gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "soft grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "softgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "softgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "softgrey")
                            elif "light blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightblue")
                            elif "lightblue" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "lightblue")
                            elif "sky blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "skyblue" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "weathered bronze" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                            elif "weatheredbronze" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                            elif "light coral" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "lightcoral" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "skyblue")
                            elif "dark gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "dark grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "darkgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "darkgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "darkgrey")
                            elif "weathered brown" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                            elif "weatheredbrown" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                            elif "clear" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "clear")
                            elif "natural" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "natural")
                            elif "white" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "white")
                            elif "gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "gray")
                            elif "grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "grey")
                            elif "silver" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "silver")
                            elif "aqua" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "aqua")
                            elif "blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "blue")
                            elif "teal" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "teal")
                            elif "green" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "green")
                            elif "purple" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "purple")
                            elif "violet" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "violet")
                            elif "red" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "red")
                            elif "magenta" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "magenta")
                            elif "pink" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "pink")
                            elif "orange" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "orange")
                            elif "tangerine" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "tangerine")
                            elif "yellow" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "yellow")
                            elif "tan" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "tan")
                            elif "biege" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "biege")
                            elif "brown" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "brown")
                            elif "smoke" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "smoke")
                            elif "black" in urgency_list.get_job_colorant_id(UL, j).lower():
                                urgency_list.set_job_overall_color(UL, j, "black")
                            else:
                                urgency_list.set_job_overall_color(UL, j, "unknown")

                        machines.assign_job(current_machine, urgency_list.get_job(UL, j))
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
                    continue
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

                    # Should also find the overall color value for each job within bin-packing
                    # Need to add this to every point that uses assign_job
                    # add job to the machine job list
                    
                    if (pd.isna(urgency_list.get_job_material_id(UL, j))) and (pd.isna(urgency_list.get_job_colorant_id(UL, j))):
                        urgency_list.set_job_overall_color(UL, j, "unknown")
                    elif pd.isna(urgency_list.get_job_colorant_id(UL, j)):
                        if "light gray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "light grey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "lightgray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "lightgrey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "soft gray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "soft grey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "softgray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "softgrey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "light blue" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightblue")
                        elif "lightblue" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightblue")
                        elif "sky blue" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "skyblue" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "weathered bronze" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                        elif "weatheredbronze" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                        elif "light coral" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "lightcoral" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "dark gray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "dark grey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "darkgray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "darkgrey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "weathered brown" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                        elif "weatheredbrown" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                        elif "clear" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "clear")
                        elif "natural" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "natural")
                        elif "white" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "white")
                        elif "gray" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "gray")
                        elif "grey" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "grey")
                        elif "silver" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "silver")
                        elif "aqua" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "aqua")
                        elif "blue" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "blue")
                        elif "teal" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "teal")
                        elif "green" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "green")
                        elif "purple" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "purple")
                        elif "violet" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "violet")
                        elif "red" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "red")
                        elif "magenta" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "magenta")
                        elif "pink" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "pink")
                        elif "orange" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "orange")
                        elif "tangerine" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "tangerine")
                        elif "yellow" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "yellow")
                        elif "tan" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "tan")
                        elif "biege" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "biege")
                        elif "brown" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "brown")
                        elif "smoke" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "smoke")
                        elif "black" in urgency_list.get_job_material_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "black")
                        else:
                            urgency_list.set_job_overall_color(UL, j, "unknown")
                    else:
                        if "light gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "light grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "lightgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "lightgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightgrey")
                        elif "soft gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "soft grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "softgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "softgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "softgrey")
                        elif "light blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightblue")
                        elif "lightblue" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "lightblue")
                        elif "sky blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "skyblue" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "weathered bronze" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                        elif "weatheredbronze" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbronze")
                        elif "light coral" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "lightcoral" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "skyblue")
                        elif "dark gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "dark grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "darkgray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "darkgrey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "darkgrey")
                        elif "weathered brown" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                        elif "weatheredbrown" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "weatheredbrown")
                        elif "clear" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "clear")
                        elif "natural" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "natural")
                        elif "white" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "white")
                        elif "gray" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "gray")
                        elif "grey" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "grey")
                        elif "silver" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "silver")
                        elif "aqua" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "aqua")
                        elif "blue" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "blue")
                        elif "teal" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "teal")
                        elif "green" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "green")
                        elif "purple" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "purple")
                        elif "violet" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "violet")
                        elif "red" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "red")
                        elif "magenta" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "magenta")
                        elif "pink" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "pink")
                        elif "orange" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "orange")
                        elif "tangerine" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "tangerine")
                        elif "yellow" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "yellow")
                        elif "tan" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "tan")
                        elif "biege" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "biege")
                        elif "brown" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "brown")
                        elif "smoke" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "smoke")
                        elif "black" in urgency_list.get_job_colorant_id(UL, j).lower():
                            urgency_list.set_job_overall_color(UL, j, "black")
                        else:
                            urgency_list.set_job_overall_color(UL, j, "unknown")
                    # print("JobNum -> ", urgency_list.get_job_num(UL, j), " | Overall Color -> ", urgency_list.get_job_overall_color(UL, j))
                    # This should be reformatted in order to make it easier for the user to add colors
                    
                    urgency_list.set_job_finished(UL, j, True)
                    machines.assign_job(current_machine, urgency_list.get_job(UL, j))
                
        print("\nBin Packing Finished\n")
        
        return machines

    
