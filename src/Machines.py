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

        # Establish values for earlyStartTime & lateStartTime
        self.early_start_time = datetime(2024, 3, 22, 6, 0, 0)
        self.late_end_time = datetime(2024, 3, 22, 18, 30, 0)

        # Establish Timeslot duration (30 minutes)
        self.slot_duration = timedelta(minutes=30)

        # Calculation of Total Hours for Slot Count
        schedule_duration = self.late_end_time - self.early_start_time
        total_minutes = schedule_duration.total_seconds() / 60
        self.slot_count = int(total_minutes / 30) + 1

    # Method to create slots & establish frame constraints for each machine
    def create(self, early_start_time, late_end_time):
        for m in range(1, 5):
            # Timeslot creation
            for i in range(self.slot_count):
                slot = Slot()
                slot.set_start(early_start_time + i * self.slot_duration)
                slot.set_end(slot.get_start() + self.slot_duration)
                slot.set_availability(False)  # Set default availability
                slot.set_assignment(None)  # Set default assignment
                if m == 1:
                    self.mach2_slot[i] = slot
                elif m == 2:
                    self.mach5_slot[i] = slot
                elif m == 3:
                    self.mach6_slot[i] = slot
                elif m == 4:
                    self.mach9_slot[i] = slot
                else:
                    print("Error: Not a current machine")
                    exit(0)

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

    # Getter methods for start, end, availability and assignment properties of each machine
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
