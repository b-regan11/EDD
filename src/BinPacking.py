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

        # Establishes earliest timeslot times for each machine
        mach2EarliestSlot = machines.get_start_time(1,0)
        mach5EarliestSlot = machines.get_start_time(2,0)
        mach6EarliestSlot = machines.get_start_time(3,0)
        mach9EarliestSlot = machines.get_start_time(4,0)

        # Establishes cutoff time for timeslots for each machine
        mach2Cutoff = machines.get_end_time(1, machines.get_last_timeslot_index(1))
        mach5Cutoff = machines.get_end_time(2, machines.get_last_timeslot_index(2))
        mach6Cutoff = machines.get_end_time(3, machines.get_last_timeslot_index(3))
        mach9Cutoff = machines.get_end_time(4, machines.get_last_timeslot_index(4))

        # Creates list of earliest open timeslots for each machine
        EarliestTimeslots = list()
        EarliestTimeslots.append(mach2EarliestSlot)
        EarliestTimeslots.append(mach5EarliestSlot)
        EarliestTimeslots.append(mach6EarliestSlot)
        EarliestTimeslots.append(mach9EarliestSlot)
        EarliestTimeslots.sort()

        MA1 = None
        MA2 = None
        MB = None

        for UL in range(5):
            UL_JobCount = urgency_list.get_job_count(UL)
            for j in range(UL_JobCount):
                for f in range(8):
                    for m in range(1, 5):
                        if machines.get_frame_type(m, f) == urgency_list.get_job_frame(UL, j):
                            if machines.get_tier_a1(m, f):
                                MA1 = m # This represents the machine that is assigned to tier a1 for frame f
                            if machines.get_tier_a2(m, f):
                                MA2 = m # This represents the machine that is assigned to tier a2 for frame f
                            if machines.get_tier_b(m, f):
                                MB = m # This represents the machine that is assigned to tier b for frame f
                                
                if MA1 == 1:
                    MA1EarliestSlot = mach2EarliestSlot
                    MA1Cutoff = mach2Cutoff
                elif MA1 == 2:
                    MA1EarliestSlot = mach5EarliestSlot
                    MA1Cutoff = mach5Cutoff
                elif MA1 == 3:
                    MA1EarliestSlot = mach6EarliestSlot
                    MA1Cutoff = mach6Cutoff
                elif MA1 == 4:
                    MA1EarliestSlot = mach9EarliestSlot
                    MA1Cutoff = mach9Cutoff

                if MA2 == 1:
                    MA2EarliestSlot = mach2EarliestSlot
                    MA2Cutoff = mach2Cutoff
                elif MA2 == 2:
                    MA2EarliestSlot = mach5EarliestSlot
                    MA2Cutoff = mach5Cutoff
                elif MA2 == 3:
                    MA2EarliestSlot = mach6EarliestSlot
                    MA2Cutoff = mach6Cutoff
                elif MA2 == 4:
                    MA2EarliestSlot = mach9EarliestSlot
                    MA2Cutoff = mach9Cutoff

                if MB == 1:
                    MBEarliestSlot = mach2EarliestSlot
                    MBCutoff = mach2Cutoff
                elif MB == 2:
                    MBEarliestSlot = mach5EarliestSlot
                    MBCutoff = mach5Cutoff
                elif MB == 3:
                    MBEarliestSlot = mach6EarliestSlot
                    MBCutoff = mach6Cutoff
                elif MB == 4:
                    MBEarliestSlot = mach9EarliestSlot
                    MBCutoff = mach9Cutoff
                
                # If the frame has both a tier A2 and tier B
                if (MA2 != None) and (MB != None):
                    # IF machines MA1 and MA2 are not full
                        if MA1EarliestSlot == MA2EarliestSlot:
                            # assign job j to machine MA1
                            print()
                        elif MA1EarliestSlot < MA2EarliestSlot:
                            # assign job j to machine MA1
                            print()
                        elif MA1EarliestSlot > MA2EarliestSlot:
                            # assign job j to machine MA2
                            print()
                    # If MA1 OR MA2 is full
                        # assign job j to the machine that is not full
                    # If MA1 AND MA2 are full but MB is not full
                        # assign job j to machine MB
                    # If MA1, MA2, and MB are all full
                        # skip job j, assign to no machine
                
                # If the frame has a tier A2 but no tier B
                elif (MA2 != None) and (MB == None):
                    # IF machines MA1 and MA2 are not full
                        if MA1EarliestSlot == MA2EarliestSlot:
                            # assign job j to machine MA1
                            print()
                        elif MA1EarliestSlot < MA2EarliestSlot:
                            # assign job j to machine MA1
                            print()
                        elif MA1EarliestSlot > MA2EarliestSlot:
                            # assign job j to machine MA2
                            print()
                    # If MA1 OR MA2 is full
                        # assign job j to the machine that is not full
                    # If MA1 AND MA2 are full
                        # skip job j, assign to no machine
                
                # If the frame has a tier B but no tier A2
                elif (MA2 == None) and (MB != None):
                    # If machine MA1 is not full:
                        # assign job j to machine MA1
                    # If machine MA1 is full but MB is not full:
                        # assign job j to machine MB
                    # If machine MA1 and MB are both full:
                        # skip job j, assign to no machine

                # If the frame has no tier A2 and no tier B
                    # If machine MA1 is not full:
                        # assign job j to machine MA1
                    # If machine MA1 is full:
                        # skip job j, assign to no machine
                    print()