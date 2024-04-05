from datetime import datetime, timedelta
import os
import pandas as pd
from UrgencyList import UrgencyList
from Machines import Machines

class BinPacking:
    def main(start_date, end_date, sorted_data):
        # Create an instance of UrgencyList
        urgency_list = UrgencyList()

        # Call the create method
        urgency_list.create(start_date, end_date, sorted_data)

        machines = Machines()
        machines.create(start_date, end_date)

        # Establishes default earliest values for each machine
        mach2EarliestSlot = 0
        mach5EarliestSlot = 0
        mach6EarliestSlot = 0
        mach9EarliestSlot = 0

        # Creates list of earliest open timeslots for each machine
        EarliestTimeslots = list()
        EarliestTimeslots.append(mach2EarliestSlot)
        EarliestTimeslots.append(mach5EarliestSlot)
        EarliestTimeslots.append(mach6EarliestSlot)
        EarliestTimeslots.append(mach9EarliestSlot)

        #for UL in [urgency_list.UL_Attainable, urgency_list.UL_Overdue_Attainable, urgency_list.UL_Unattainable, urgency_list.UL_Overdue_Unattainable, urgency_list.UL_Other]:

        for f in range(8):
            for m in range(1, 5):
                # If frame type for (m, f) is equal to the current job.get_frame value
                
                # Find the earliest timeslot among all machines
                while any(machines.get_availability(1, slot) for slot in range(mach2EarliestSlot, machines.slot_count)):
                    mach2EarliestSlot += 1
                    EarliestTimeslots.append(mach2EarliestSlot)
                    EarliestTimeslots.sort()

                while any(machines.get_availability(2, slot) for slot in range(mach5EarliestSlot, machines.slot_count)):
                    mach5EarliestSlot += 1
                    EarliestTimeslots.append(mach5EarliestSlot)
                    EarliestTimeslots.sort()

                while any(machines.get_availability(3, slot) for slot in range(mach6EarliestSlot, machines.slot_count)):
                    mach6EarliestSlot += 1
                    EarliestTimeslots.append(mach6EarliestSlot)
                    EarliestTimeslots.sort()

                while any(machines.get_availability(4, slot) for slot in range(mach9EarliestSlot, machines.slot_count)):
                    mach9EarliestSlot += 1
                    EarliestTimeslots.append(mach9EarliestSlot)
                    EarliestTimeslots.sort()

        # TESTING
        # Access and print jobs in each urgency list 
        print("Attainable Jobs:")
        for job in urgency_list.UL_Attainable.values():
            print("Job Num: ", job.get_Job_Num(), " | Job Hours: ", job.get_ProductionHours(), " | Job Frame: ", job.get_Frame())

        print("\nOverdue Attainable Jobs:")
        for job in urgency_list.UL_Overdue_Attainable.values():
            print("Job Num: ", job.get_Job_Num(), " | Job Hours: ", job.get_ProductionHours(), " | Job Frame: ", job.get_Frame())

        print("\nUnattainable Jobs:")
        for job in urgency_list.UL_Unattainable.values():
            print("Job Num: ", job.get_Job_Num(), " | Job Hours: ", job.get_ProductionHours(), " | Job Frame: ", job.get_Frame())

        print("\nOverdue Unattainable Jobs:")
        for job in urgency_list.UL_Overdue_Unattainable.values():
            print("Job Num: ", job.get_Job_Num(), " | Job Hours: ", job.get_ProductionHours(), " | Job Frame: ", job.get_Frame())

        print("\nOther Jobs:")
        for job in urgency_list.UL_Other.values():
            print("Job Num: ", job.get_Job_Num(), " | Job Hours: ", job.get_ProductionHours(), " | Job Frame: ", job.get_Frame())
        