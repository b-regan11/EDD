from datetime import datetime, timedelta
from Timeslot import Slot
from Frames import Frame

class Machines:
    def __init__(self):
        # Create dictionaries with Integer keys and Slot/Frame objects as values for Machines 2, 5, 6, & 9
        self.mach2_slot = {}
        self.mach5_slot = {}
        self.mach6_slot = {}
        self.mach9_slot = {}
        self.mach2_frames = {}
        self.mach5_frames = {}
        self.mach6_frames = {}
        self.mach9_frames = {}

        # Maintain a dictionary to store jobs assigned to each machine
        self.jobs_assigned = {
            1: [], # Machine 2
            2: [], # Machine 5
            3: [], # Machine 6
            4: [] # Machine 9
        }

        # Establish Timeslot duration (30 minutes)
        self.slot_duration = timedelta(minutes=30)

        # Boolean variables to indicate whether a machine is full
        self.machine_full = {
            1: False,  # Machine 2
            2: False,  # Machine 5
            3: False,  # Machine 6
            4: False   # Machine 9
        }
        
    # Method to create slots & establish frame constraints for each machine
    def create(self, mach2_day_times, mach5_day_times, mach6_day_times, mach9_day_times):
        for m in range(1, 5):
            if m == 1:
                day_times = mach2_day_times
            elif m == 2:
                day_times = mach5_day_times
            elif m == 3:
                day_times = mach6_day_times
            elif m == 4:
                day_times = mach9_day_times
            else:
                    print("Error: Not a current machine")
                    exit(0)
            
            prev_loop = 0
            for d in range(len(day_times)):
                start, end = day_times[d]
                slot_count = Machines.calculate_slot_count(self, start, end)

                # Timeslot creation
                for i in range(slot_count - 1):
                    slot = Slot()
                    slot.set_start(start + i * self.slot_duration)
                    slot.set_end(slot.get_start() + self.slot_duration)
                    slot.set_availability(False)  # Set default availability
                    slot.set_assignment(None)  # Set default assignment
                    
                    curr_loop = i
                    if d == 0:
                        index = curr_loop
                        prev_loop = curr_loop + 1
                    else:
                        index = prev_loop
                        prev_loop = prev_loop + 1
                    
                    if m == 1:
                        self.mach2_slot[index] = slot
                    elif m == 2:
                        self.mach5_slot[index] = slot
                    elif m == 3:
                        self.mach6_slot[index] = slot
                    elif m == 4:
                        self.mach9_slot[index] = slot

            # Frame type creation
            for f in range(8):
                frame = Frame()
                # Set Default Tier Values
                frame.set_tier_a1(False)
                frame.set_tier_a2(False)
                frame.set_tier_b(False)

                # Set Frame Types and Tiered Preferences
                if f == 0:
                    frame.set_frame_type("Small")
                    if m == 1:
                        frame.set_tier_a1(True)  # Machine 2
                    elif m == 2:
                        frame.set_tier_b(True)  # Machine 5
                    elif m == 3:
                        frame.set_tier_a2(True)  # Machine 6
                elif f == 1:
                    frame.set_frame_type("Round")
                    if m == 1:
                        frame.set_tier_a2(True)  # Machine 2
                    elif m == 2:
                        frame.set_tier_b(True)  # Machine 5
                    elif m == 3:
                        frame.set_tier_a1(True)  # Machine 6
                elif f == 2:
                    frame.set_frame_type("Rectangle")
                    if m == 1:
                        frame.set_tier_a1(True)  # Machine 2
                    elif m == 2:
                        frame.set_tier_b(True)  # Machine 5
                    elif m == 3:
                        frame.set_tier_a2(True)  # Machine 6
                elif f == 3:
                    frame.set_frame_type("Short Large-T")
                    if m == 2:
                        frame.set_tier_a1(True)  # Machine 5
                elif f == 4:
                    frame.set_frame_type("Large-T")
                    if m == 2:
                        frame.set_tier_a1(True)  # Machine 5
                    elif m == 3:
                        frame.set_tier_a2(True)  # Machine 6
                    elif m == 4:
                        frame.set_tier_b(True)  # Machine 9
                elif f == 5:
                    frame.set_frame_type("Small Self Contain")
                    if m == 2:
                        frame.set_tier_a1(True)  # Machine 5
                    elif m == 3:
                        frame.set_tier_a2(True)  # Machine 6
                elif f == 6:
                    frame.set_frame_type("Self Contain")
                    if m == 4:
                        frame.set_tier_a1(True)  # Machine 9
                elif f == 7:
                    frame.set_frame_type("XL-T")
                    if m == 2:
                        frame.set_tier_b(True)  # Machine 5
                    elif m == 4:
                        frame.set_tier_a1(True)  # Machine 9
                else:
                    print("Error: Not a current frame")
                    exit(0)

                # Adding Frames to Dictionaries
                if m == 1:
                    self.mach2_frames[f] = frame
                elif m == 2:
                    self.mach5_frames[f] = frame
                elif m == 3:
                    self.mach6_frames[f] = frame
                elif m == 4:
                    self.mach9_frames[f] = frame
                else:
                    print("Error: Not a current machine")
                    exit(0)

    # Getter methods for start, end, availability and assignment properties of each machine based on slot index
    def get_start_time(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_start()

    def get_end_time(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_end()

    def get_availability(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_availability()

    def get_assignment(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_assignment()

    # setter methods for availability and assignment properties of each machine
    def set_availability(self, machine_number, slot_number, availability):
        self.get_machine(machine_number)[slot_number].set_availability(availability)

    def set_assignment(self, machine_number, slot_number, assignment):
        self.get_machine(machine_number)[slot_number].set_assignment(assignment)

    # Getter methods for frame type, tier_a1, tier_a2 and tier_b compatibility properties of each machine
    def get_frame_type(self, machine_number, frame_number):
        return self.get_frame_list(machine_number)[frame_number].get_frame_type()

    def get_tier_a1(self, machine_number, frame_number):
        return self.get_frame_list(machine_number)[frame_number].get_tier_a1()

    def get_tier_a2(self, machine_number, frame_number):
        return self.get_frame_list(machine_number)[frame_number].get_tier_a2()

    def get_tier_b(self, machine_number, frame_number):
        return self.get_frame_list(machine_number)[frame_number].get_tier_b()

    # Helper method to get the machine based on the machine number
    def get_machine(self, machine_number):
        if machine_number == 1:
            return self.mach2_slot
        elif machine_number == 2:
            return self.mach5_slot
        elif machine_number == 3:
            return self.mach6_slot
        elif machine_number == 4:
            return self.mach9_slot
        else:
            raise ValueError("Invalid machine number")

    # Helper method to get the frame hashmap based on the machine number
    def get_frame_list(self, machine_number):
        if machine_number == 1:
            return self.mach2_frames
        elif machine_number == 2:
            return self.mach5_frames
        elif machine_number == 3:
            return self.mach6_frames
        elif machine_number == 4:
            return self.mach9_frames
        else:
            raise ValueError("Invalid frame number")
    
    # Getter method for slot count of a machine
    def get_slot_count(self, machine_number):
        day_times = None
        if machine_number == 1:
            day_times = self.mach2_day_times
        elif machine_number == 2:
            day_times = self.mach5_day_times
        elif machine_number == 3:
            day_times = self.mach6_day_times
        elif machine_number == 4:
            day_times = self.mach9_day_times
        else:
            raise ValueError("Invalid machine number")

        total_slot_count = 0
        for start, end in day_times:
            total_slot_count += self.calculate_slot_count(start, end)

        return total_slot_count

    # Method to calculate how many timeslots in a time period
    def calculate_slot_count(self, start, end):
        schedule_duration = end - start
        total_minutes = schedule_duration.total_seconds() / 60
        return int(total_minutes / 30) + 1
    
    # Setter method for assigning a job to a machine
    # This should be called once for each job, this is independent of the timeslots
    def assign_job(self, machine_number, job):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Add the job to the list of jobs assigned to the specified machine
        self.jobs_assigned[machine_number].append(job)

    # Getter method for retrieving the list of jobs assigned to a machine
    def get_assigned_jobs(self, machine_number):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Return the list of jobs assigned to the specified machine
        return self.jobs_assigned[machine_number]

    # Getter method for getting the last timeslot index for a machine
    def get_last_timeslot_index(self, machine_number):
        machine = self.get_machine(machine_number)
        if not machine:
            raise ValueError("Invalid machine number")

        if not machine:
            return None  # Return None if the machine has no timeslots

        last_index = max(machine.keys()) if machine else None
        return last_index
    
    def get_last_timeslot(self, machine_number):
        machine = self.get_machine(machine_number)
        if not machine:
            raise ValueError("Invalid machine number")

        if not machine:
            return None  # Return None if the machine has no timeslots

        last_index = max(machine.keys()) if machine else None
        return self.get_machine(machine_number)[last_index].get_end()
    
    # Getter method for retrieving the job numbers assigned to a machine
    def get_assigned_job_num(self, machine_number, job):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Extract and return the job number from job object
        job_num = job.get_Job_Num()
        return job_num
    
    def get_assigned_job_nums(self, machine_number):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Retrieve the list of jobs assigned to the specified machine
        jobs = self.jobs_assigned[machine_number]

        # Extract and return the job numbers from each job object
        job_nums = [job.get_Job_Num() for job in jobs]
        return job_nums
    
    # Getter method to retrieve whether a machine is full
    def is_machine_full(self, machine_number):
        return self.machine_full[machine_number]

    # Setter method to set whether a machine is full
    def set_machine_full(self, machine_number, is_full):
        self.machine_full[machine_number] = is_full

    def get_assigned_job_start(self, machine_number, job):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Extract and return the job start from job object
        job_start = job.get_Start()
        return job_start

    def get_assigned_job_end(self, machine_number, job):
        if machine_number not in [1, 2, 3, 4]:
            raise ValueError("Invalid machine number")

        # Extract and return the job start from job object
        job_end = job.get_End()
        return job_end
    