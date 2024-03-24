from datetime import datetime

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


class Timeslot:
    def __init__(self):
        pass

    @staticmethod
    def main():
        pass
