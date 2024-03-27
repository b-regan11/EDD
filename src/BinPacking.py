class BinPacking:
  def SortUrgencyList(sorted_data):
    # Start & End dates for production week
    start_date = '2023-4-24' # datetime.date(2023,4,24)
    end_date = '2023-4-30' # datetime.date(2023,4,30)         #both of these should be user input later on
 
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
    
    # Print Urgency Listings for testing purposes
    print(UL_Attainable)
    print(UL_Overdue_Attainable)
    print(UL_Unattainable)
    print(UL_Overdue_Unattainable)
    print(OtherList)
    # For all rows in UL_Attainable, check Frame

# class BinPacking_MachineAvailability:
#    def __init__(self):
#         # Initialize an empty dictionary to represent machine schedules
#         self.machine_schedules = {} 