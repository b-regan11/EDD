from datetime import datetime

class Slot:
    def __init__(self):
        self.slotStart = None
        self.slotEnd = None
        self.slotAvailability = False  # This shows whether it's filled or not, False meaning it can be assigned a job.
        self.slotAssignment = None

    # Getters for Start Time, End Time, Availability, and Assignment
    def get_start(self):
        return self.slotStart

    def get_end(self):
        return self.slotEnd

    def get_availability(self):
        return self.slotAvailability

    def get_assignment(self):
        return self.slotAssignment

    # Setters for Start Time, End Time, Availability, and Assignment
    def set_start(self, start):
        self.slotStart = start

    def set_end(self, end):
        self.slotEnd = end

    def set_availability(self, availability):
        self.slotAvailability = availability

    def set_assignment(self, assignment):
        self.slotAssignment = assignment
