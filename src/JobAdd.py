from Machines import Machines
from datetime import datetime
from FileSelection import FileSelection
class JobAdd:
    def SortUrgencyList(sorted_data):
        # Start & End dates for production week
        start_date = datetime(2023, 4, 24, 6, 0, 0)
        end_date = datetime(2023, 4, 30, 18, 30, 0) #both of these should be user input later on

        # Urgency List for Job Priorities
        UrgencyList = sorted_data[(sorted_data['due_date'] >= start_date) & (sorted_data['due_date'] <= end_date)]
        UL_Attainable = UrgencyList.query('production_hrs <= 25') # 1
        UL_Unattainable = UrgencyList.query('production_hrs > 25') # 3
        UrgencyList = sorted_data[(sorted_data['due_date'] > '2020-1-01') & (sorted_data['due_date'] < start_date)]
        UL_Overdue_Attainable = UrgencyList.query('production_hrs <= 25') # 2
        UL_Overdue_Unattainable = UrgencyList.query('production_hrs > 25') # 4
        OtherList = sorted_data[(sorted_data['due_date'] > end_date) & (sorted_data['due_date'] < '2099-1-01')] # 5

        # Calculate the remainder number of jobs to fill in the other list to total 40 jobs
        Remainder = 40 - (len(UL_Attainable) + len(UL_Overdue_Attainable) + len(UL_Unattainable) + len(UL_Overdue_Unattainable))
        OtherList = OtherList.iloc[:Remainder] # Return extra rows to make sure there isn't more than 40 rows of data

        return start_date, end_date, UL_Attainable, UL_Unattainable, UL_Overdue_Attainable, UL_Overdue_Unattainable, OtherList
    
    def JobAssignment(start_date, end_date, UL_Attainable, UL_Unattainable, UL_Overdue_Attainable, UL_Overdue_Unattainable, OtherList):
        # Create slots and frame constraints for machines
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

        # Find the earliest timeslot among all machines
        while machines.get_availability(1, mach2EarliestSlot) == True:
            EarliestTimeslots.remove(mach2EarliestSlot)
            mach2EarliestSlot += 1
            EarliestTimeslots.append(mach2EarliestSlot)
            EarliestTimeslots.sort
            # Write an IF statement for if the machine is full
        while machines.get_availability(2, mach2EarliestSlot) == True:
            EarliestTimeslots.remove(mach2EarliestSlot)
            mach2EarliestSlot += 1
            EarliestTimeslots.append(mach2EarliestSlot)
            EarliestTimeslots.sort
            # Write an IF statement for if the machine is full
        while machines.get_availability(3, mach2EarliestSlot) == True:
            EarliestTimeslots.remove(mach2EarliestSlot)
            mach2EarliestSlot += 1
            EarliestTimeslots.append(mach2EarliestSlot)
            EarliestTimeslots.sort
            # Write an IF statement for if the machine is full
        while machines.get_availability(4, mach2EarliestSlot) == True:
            EarliestTimeslots.remove(mach2EarliestSlot)
            mach2EarliestSlot += 1
            EarliestTimeslots.append(mach2EarliestSlot)
            EarliestTimeslots.sort
            # Write an IF statement for if the machine is full

        
        # For lists 1 - 5:
            # Count the # of jobs / rows in List X
            # For each job in List X
                # 



        # Set availability and assignment for a slot in machine 2
#         machines.set_availability(3, 10, True)
#         machines.set_assignment(3, 10, "Job ABC")

#         # Get and print the availability and assignment for the slot in machine 2
#         start = machines.get_start_time(3, 10)
#         end = machines.get_end_time(3, 10)
#         availability = machines.get_availability(3, 10)
#         assignment = machines.get_assignment(3, 10)
#         print("Start Time:", start)
#         print("End Time:", end)
#         print("Availability:", availability)
#         print("Assignment:", assignment)

#         # Test getting frame type and compatibility properties
#         frame_type = machines.get_frame_type(3, 1)
#         tier_a1 = machines.get_tier_a1(3, 1)
#         tier_a2 = machines.get_tier_a2(3, 1)
#         tier_b = machines.get_tier_b(3, 1)
#         print("Frame Type for Machine 6:", frame_type)
#         print("Tier A1 Compatibility for Frame 0 on Machine 6:", tier_a1)
#         print("Tier A2 Compatibility for Frame 0 on Machine 6:", tier_a2)
#         print("Tier B Compatibility for Frame 0 on Machine 6:", tier_b)

# Entry point
if __name__ == "__main__":
    JobAdd().main()
