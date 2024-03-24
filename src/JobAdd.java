package src;

import java.time.LocalDateTime;

public class JobAdd {
    public static void main(String[] args) {
        Machines machines = new Machines();

        // Create slots and frame constraints for machines
        machines.create(LocalDateTime.of(2024, 3, 22, 6, 0, 0), LocalDateTime.of(2024, 3, 22, 18, 30, 0));

        // Set availability and assignment for a slot in machine 2
        machines.setAvailability(1, 0, true);
        machines.setAssignment(1, 0, "Job ABC");

        // Get and print the availability and assignment for the slot in machine 2
        LocalDateTime start = machines.getStartTime(1, 0);
        LocalDateTime end = machines.getEndTime(1, 0);
        boolean availability = machines.getAvailability(1, 0);
        String assignment = machines.getAssignment(1, 0);
        System.out.println("Start Time: " + start);
        System.out.println("End Time: " + end);
        System.out.println("Availability: " + availability);
        System.out.println("Assignment: " + assignment);

        // Test getting frame type and compatibility properties
        String frameType = machines.getFrameType(1, 0);
        boolean tierA = machines.getTierA(1, 0);
        boolean tierB = machines.getTierB(1, 0);
        System.out.println("Frame Type for Machine 2: " + frameType);
        System.out.println("Tier A Compatibility for Frame 0 on Machine 2: " + tierA);
        System.out.println("Tier B Compatibility for Frame 0 on Machine 2: " + tierB);
    }
}