from datetime import datetime
from Machines import Machines

def main():
    machines = Machines()

    # Create slots for machines
    machines.create(datetime(2024, 3, 22, 6, 0, 0), datetime(2024, 3, 22, 18, 30, 0))

    # Set availability and assignment for a slot in machine 2
    machines.set_availability(1, 0, True)
    machines.set_assignment(1, 0, "Job ABC")

    # Get and print the availability and assignment for the slot in machine 2
    start = machines.get_start_time(1, 0)
    end = machines.get_end_time(1, 0)
    availability = machines.get_availability(1, 0)
    assignment = machines.get_assignment(1, 0)
    print("Start Time:", start)
    print("End Time:", end)
    print("Availability:", availability)
    print("Assignment:", assignment)

if __name__ == "__main__":
    main()
