from datetime import datetime, timedelta

class Machines:
    def __init__(self):
        # Create a new instance of the Timeslot class
        self.slot_a = Slot()

        # Create a dictionary with integer keys and Slot objects as values for Machines 2, 5, 6, & 9
        self.mach2 = {}
        self.mach5 = {}
        self.mach6 = {}
        self.mach9 = {}

        # Establish values for early_start_time & late_end_time
        self.early_start_time = datetime(2024, 3, 22, 6, 0, 0)
        self.late_end_time = datetime(2024, 3, 22, 18, 30, 0)

        # Establish Timeslot duration (30 minutes)
        self.slot_duration = timedelta(minutes=30)

        # Calculation of Total Hours for Slot Count
        self.schedule_duration = self.late_end_time - self.early_start_time
        self.total_minutes = self.schedule_duration.total_seconds() / 60
        self.total_hours = self.total_minutes / 60
        self.slot_count = int(self.total_hours * 2) + 1

    # Method to create slots for each machine
    def create(self, early_start_time, late_end_time):
        for m in range(1, 5):
            for i in range(self.slot_count):
                slot_b = Slot()
                self.slot_a.set_start(None)  # Set default start time
                self.slot_a.set_end(None)  # Set default end time
                self.slot_a.set_availability(False)  # Set default availability
                self.slot_a.set_assignment(None)  # Set default assignment
                start_time = early_start_time + timedelta(minutes=i * self.slot_duration.total_seconds() / 60)
                end_time = start_time + self.slot_duration
                slot_b.set_start(start_time)
                slot_b.set_end(end_time)
                if m == 1:
                    self.mach2[i] = slot_b
                elif m == 2:
                    self.mach5[i] = slot_b
                elif m == 3:
                    self.mach6[i] = slot_b
                elif m == 4:
                    self.mach9[i] = slot_b
                else:
                    print("Error: Not a current machine")
                    exit(0)

    # Getter and setter methods for availability and assignment properties of each machine
    def get_availability(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_availability()

    def set_availability(self, machine_number, slot_number, availability):
        self.get_machine(machine_number)[slot_number].set_availability(availability)

    def get_assignment(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_assignment()

    def set_assignment(self, machine_number, slot_number, assignment):
        self.get_machine(machine_number)[slot_number].set_assignment(assignment)

    def get_start_time(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_start()

    def get_end_time(self, machine_number, slot_number):
        return self.get_machine(machine_number)[slot_number].get_end()

    # Helper method to get the machine based on the machine number
    def get_machine(self, machine_number):
        machines = {1: self.mach2, 2: self.mach5, 3: self.mach6, 4: self.mach9}
        return machines.get(machine_number, None)


class Slot:
    def __init__(self):
        self.slot_start = None
        self.slot_end = None
        self.slot_availability = False
        self.slot_assignment = None

    # Getters for Start Time, End Time, Availability, and Assignment
    def get_start(self):
        return self.slot_start

    def get_end(self):
        return self.slot_end

    def get_availability(self):
        return self.slot_availability

    def get_assignment(self):
        return self.slot_assignment

    # Setters for Start Time, End Time, Availability, and Assignment
    def set_start(self, start):
        self.slot_start = start

    def set_end(self, end):
        self.slot_end = end

    def set_availability(self, availability):
        self.slot_availability = availability

    def set_assignment(self, assignment):
        self.slot_assignment = assignment
