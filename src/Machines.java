package src;
import java.util.HashMap;
import java.util.Map;
import java.time.LocalDateTime;
import java.time.Duration;

public class Machines {
    // Create a new instance of the Timeslot class
    private Slot slot = new Slot();
    
    // Create a HashMap with Integer keys and Slot objects as values for Machines 2, 5, 6, & 9
    private Map<Integer, Slot> mach2 = new HashMap<>();
    private Map<Integer, Slot> mach5 = new HashMap<>();
    private Map<Integer, Slot> mach6 = new HashMap<>();
    private Map<Integer, Slot> mach9 = new HashMap<>();

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


    public static void main(String[] args) {
        Machines machine = new Machines(); // Creates instance of Machine

        for (int m = 1; m <= 4; m++) {
            System.out.println("\n" + "Machine: " + m + "\n");
            for (int i = 0; i <= slotCount - 1; i++) {
                // Creates a new slot object
                Slot slot = new Slot();

                machine.slot.setStart(null); // Set default start time
                machine.slot.setEnd(null); // Set default end time
                machine.slot.setAvailability(false); // Set default availability
                machine.slot.setAssignment(null); // Set default assignment

                slot.setStart(earlyStartTime.plusMinutes(i * slotDuration.toMinutes()));
                slot.setEnd(slot.getStart().plusMinutes(slotDuration.toMinutes()));
                if (m == 1) {
                    machine.mach2.put(i, slot);
                } else if (m == 2) {
                    machine.mach5.put(i, slot);
                } else if (m == 3) {
                    machine.mach6.put(i, slot);
                } else if (m == 4) {
                    machine.mach9.put(i, slot);
                } else {
                    System.out.println("Error: Not a current machine");
                    System.exit(0);
                }
                System.out.println("Start Time: " + slot.getStart());
                System.out.println("End Time: " + slot.getEnd());
                System.out.println("Availability: " + slot.getAvailability());
                System.out.println("Assignment: " + slot.getAssignment());
            }
        }
    }
}


