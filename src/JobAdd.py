from Machines import Machines
from datetime import datetime

class JobAdd:
    def main(self):
        machines = Machines()

        # Create slots and frame constraints for machines
        machines.create(datetime(2024, 3, 22, 6, 0, 0), datetime(2024, 3, 22, 18, 30, 0))

        # Set availability and assignment for a slot in machine 2
        machines.set_availability(3, 10, True)
        machines.set_assignment(3, 10, "Job ABC")

        # Get and print the availability and assignment for the slot in machine 2
        start = machines.get_start_time(3, 10)
        end = machines.get_end_time(3, 10)
        availability = machines.get_availability(3, 10)
        assignment = machines.get_assignment(3, 10)
        print("Start Time:", start)
        print("End Time:", end)
        print("Availability:", availability)
        print("Assignment:", assignment)

        # Test getting frame type and compatibility properties
        frame_type = machines.get_frame_type(3, 1)
        tier_a1 = machines.get_tier_a1(3, 1)
        tier_a2 = machines.get_tier_a2(3, 1)
        tier_b = machines.get_tier_b(3, 1)
        print("Frame Type for Machine 6:", frame_type)
        print("Tier A1 Compatibility for Frame 0 on Machine 6:", tier_a1)
        print("Tier A2 Compatibility for Frame 0 on Machine 6:", tier_a2)
        print("Tier B Compatibility for Frame 0 on Machine 6:", tier_b)

# Entry point
if __name__ == "__main__":
    JobAdd().main()
