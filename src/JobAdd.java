package src;

import java.time.LocalDateTime;

public class JobAdd {
    public static void main(String[] args) {
        Machines machines = new Machines();

        // Create slots and frame constraints for machines
        machines.create(LocalDateTime.of(2024, 3, 22, 6, 0, 0), LocalDateTime.of(2024, 3, 22, 18, 30, 0));

        // Set availability and assignment for a slot in machine 2
        machines.setAvailability(3, 10, true);
        machines.setAssignment(3, 10, "Job ABC");

        // Get and print the availability and assignment for the slot in machine 2
        LocalDateTime start = machines.getStartTime(3, 10);
        LocalDateTime end = machines.getEndTime(3, 10);
        boolean availability = machines.getAvailability(3, 10);
        String assignment = machines.getAssignment(3, 10);
        System.out.println("Start Time: " + start);
        System.out.println("End Time: " + end);
        System.out.println("Availability: " + availability);
        System.out.println("Assignment: " + assignment);

        // Test getting frame type and compatibility properties
        String frameType = machines.getFrameType(3, 1);
        boolean tierA1 = machines.getTierA1(3, 1);
        boolean tierA2 = machines.getTierA2(3, 1);
        boolean tierB = machines.getTierB(3, 1);
        System.out.println("Frame Type for Machine 6: " + frameType);
        System.out.println("Tier A1 Compatibility for Frame 0 on Machine 6: " + tierA1);
        System.out.println("Tier A2 Compatibility for Frame 0 on Machine 6: " + tierA2);
        System.out.println("Tier B Compatibility for Frame 0 on Machine 6: " + tierB);
    }
}