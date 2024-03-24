package src;

import java.util.HashMap;
import java.util.Map;
import java.time.LocalDateTime;
import java.time.Duration;

public class Machines {
    // Create a new instance of the Timeslot class
    private Slot slotA = new Slot();
    
    // Create a HashMap with Integer keys and Slot objects as values for Machines 2, 5, 6, & 9
    public Map<Integer, Slot> mach2 = new HashMap<>();
    public Map<Integer, Slot> mach5 = new HashMap<>();
    public Map<Integer, Slot> mach6 = new HashMap<>();
    public Map<Integer, Slot> mach9 = new HashMap<>();

    // Establish values for earlyStartTime & lateStartTime
    static LocalDateTime earlyStartTime = LocalDateTime.of(2024, 3, 22, 6, 0, 0);
    static LocalDateTime lateEndTime = LocalDateTime.of(2024, 3, 22, 18, 30, 0);

    // Establish Timeslot duration (30 minutes)
    static Duration slotDuration = Duration.ofMinutes(30);

    // Calculation of Total Hours for Slot Count
    static Duration scheduleDuration = Duration.between(earlyStartTime, lateEndTime);
    static float totalMinutes = scheduleDuration.toMinutes();
    static float totalHours = totalMinutes/60;
    static int slotCount = (int)totalHours * 2 + 1;

    // Method to create slots for each machine
    public void create(LocalDateTime earlyStartTime, LocalDateTime lateEndTime) {
        for (int m = 1; m <= 4; m++) {
            for (int i = 0; i <= slotCount - 1; i++) {
                Slot slotB = new Slot();
                slotA.setStart(null); // Set default start time
                slotA.setEnd(null); // Set default end time
                slotA.setAvailability(false); // Set default availability
                slotA.setAssignment(null); // Set default assignment
                slotB.setStart(earlyStartTime.plusMinutes(i * slotDuration.toMinutes()));
                slotB.setEnd(slotB.getStart().plusMinutes(slotDuration.toMinutes()));
                if (m == 1) {
                    mach2.put(i, slotB);
                } else if (m == 2) {
                    mach5.put(i, slotB);
                } else if (m == 3) {
                    mach6.put(i, slotB);
                } else if (m == 4) {
                    mach9.put(i, slotB);
                } else {
                    System.out.println("Error: Not a current machine");
                    System.exit(0);
                }
            }
        }
    }

    // Getter and setter methods for availability and assignment properties of each machine
    public boolean getAvailability(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getAvailability();
    }

    public void setAvailability(int machineNumber, int slotNumber, boolean availability) {
        getMachine(machineNumber).get(slotNumber).setAvailability(availability);
    }

    public String getAssignment(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getAssignment();
    }

    public void setAssignment(int machineNumber, int slotNumber, String assignment) {
        getMachine(machineNumber).get(slotNumber).setAssignment(assignment);
    }

    public LocalDateTime getStartTime(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getStart();
    }
    
    public LocalDateTime getEndTime(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getEnd();
    }
    

    // Helper method to get the machine based on the machine number
    private Map<Integer, Slot> getMachine(int machineNumber) {
        switch (machineNumber) {
            case 1:
                return mach2;
            case 2:
                return mach5;
            case 3:
                return mach6;
            case 4:
                return mach9;
            default:
                throw new IllegalArgumentException("Invalid machine number");
        }
    }
}

// Old Code

// package src;
// import java.util.HashMap;
// import java.util.Map;
// import java.time.LocalDateTime;
// import java.time.Duration;

// public class Machines {
//     // Create a new instance of the Timeslot class
//     private Slot slotA = new Slot();
    
//     // Create a HashMap with Integer keys and Slot objects as values for Machines 2, 5, 6, & 9
//     public Map<Integer, Slot> mach2 = new HashMap<>();
//     public Map<Integer, Slot> mach5 = new HashMap<>();
//     public Map<Integer, Slot> mach6 = new HashMap<>();
//     public Map<Integer, Slot> mach9 = new HashMap<>();

//     // Establish values for earlyStartTime & lateStartTime
//     static LocalDateTime earlyStartTime = LocalDateTime.of(2024, 3, 22, 6, 0, 0);
//     static LocalDateTime lateEndTime = LocalDateTime.of(2024, 3, 22, 18, 30, 0);

//     // Establish Timeslot duration (30 minutes)
//     static Duration slotDuration = Duration.ofMinutes(30);

//     // Calculation of Total Hours for Slot Count
//     static Duration scheduleDuration = Duration.between(earlyStartTime, lateEndTime);
//     static float totalMinutes = scheduleDuration.toMinutes();
//     static float totalHours = totalMinutes/60;
//     static int slotCount = (int)totalHours * 2 + 1;


//     public static void main(String[] args) {
//         Machines machine = new Machines(); // Creates instance of Machine

//         for (int m = 1; m <= 4; m++) {
//             System.out.println("\n" + "Machine: " + m + "\n");
//             for (int i = 0; i <= slotCount - 1; i++) {
//                 // Creates a new slot object
//                 Slot slotB = new Slot();

//                 machine.slotA.setStart(null); // Set default start time
//                 machine.slotA.setEnd(null); // Set default end time
//                 machine.slotA.setAvailability(false); // Set default availability
//                 machine.slotA.setAssignment(null); // Set default assignment

//                 slotB.setStart(earlyStartTime.plusMinutes(i * slotDuration.toMinutes()));
//                 slotB.setEnd(slotB.getStart().plusMinutes(slotDuration.toMinutes()));
//                 if (m == 1) {
//                     machine.mach2.put(i, slotB);
//                 } else if (m == 2) {
//                     machine.mach5.put(i, slotB);
//                 } else if (m == 3) {
//                     machine.mach6.put(i, slotB);
//                 } else if (m == 4) {
//                     machine.mach9.put(i, slotB);
//                 } else {
//                     System.out.println("Error: Not a current machine");
//                     System.exit(0);
//                 }
//                 System.out.println("Start Time: " + slotB.getStart());
//                 System.out.println("End Time: " + slotB.getEnd());
//                 System.out.println("Availability: " + slotB.getAvailability());
//                 System.out.println("Assignment: " + slotB.getAssignment());
//             }
//         }
//     }
// }


