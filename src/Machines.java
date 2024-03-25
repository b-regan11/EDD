package src;

import java.util.HashMap;
import java.util.Map;
import java.time.LocalDateTime;
import java.time.Duration;

public class Machines {
    // Create a new instance of the Timeslot class
    
    // Create a HashMap with Integer keys and Slot objects as values for Machines 2, 5, 6, & 9
    public Map<Integer, Slot> mach2Slot = new HashMap<>();
    public Map<Integer, Slot> mach5Slot = new HashMap<>();
    public Map<Integer, Slot> mach6Slot = new HashMap<>();
    public Map<Integer, Slot> mach9Slot = new HashMap<>();

    // Create a HashMap with Integer keys and Frame objects as values for Machines 2, 5, 6, & 9
    public Map<Integer, Frame> mach2Frames = new HashMap<>();
    public Map<Integer, Frame> mach5Frames = new HashMap<>();
    public Map<Integer, Frame> mach6Frames = new HashMap<>();
    public Map<Integer, Frame> mach9Frames = new HashMap<>();

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

    // Method to create slots & establish frame constraints for each machine
    public void create(LocalDateTime earlyStartTime, LocalDateTime lateEndTime) {
        for (int m = 1; m <= 4; m++) {
            // Timeslot creation
            for (int i = 0; i <= slotCount - 1; i++) {
                Slot slot = new Slot();
                slot.setStart(earlyStartTime.plusMinutes(i * slotDuration.toMinutes()));
                slot.setEnd(slot.getStart().plusMinutes(slotDuration.toMinutes()));
                slot.setAvailability(false); // Set default availability
                slot.setAssignment(null); // Set default assignment
                if (m == 1) {
                    mach2Slot.put(i, slot);
                } else if (m == 2) {
                    mach5Slot.put(i, slot);
                } else if (m == 3) {
                    mach6Slot.put(i, slot);
                } else if (m == 4) {
                    mach9Slot.put(i, slot);
                } else {
                    System.out.println("Error: Not a current machine");
                    System.exit(0);
                }
            }

            // Frame type creation
            for (int f = 0; f <= 7; f++) {
                Frame frame = new Frame();
                // Set Default Tier Values
                frame.setTierA1(false);
                frame.setTierA2(false);
                frame.setTierB(false);

                // Set Frame Types and Tiered Preferences
                if (f == 0) {
                    frame.setFrameType("Small");
                    if (m == 1) {
                        // Machine 2
                        frame.setTierA1(true);
                    } else if (m == 2) {
                        // Machine 5
                        frame.setTierB(true);
                    } else if (m == 3) {
                        // Machine 6
                        frame.setTierA2(true);
                    }
                } else if (f == 1) {
                    frame.setFrameType("Round");
                    if (m == 1) {
                        // Machine 2
                        frame.setTierA2(true);
                    } else if (m == 2) {
                        // Machine 5
                        frame.setTierB(true);
                    } else if (m == 3) {
                        // Machine 6
                        frame.setTierA1(true);
                    }
                } else if (f == 2) {
                    frame.setFrameType("Rectangle");
                    if (m == 1) {
                        // Machine 2
                        frame.setTierA1(true);
                    } else if (m == 2) {
                        // Machine 5
                        frame.setTierB(true);
                    } else if (m == 3) {
                        // Machine 6
                        frame.setTierA2(true);
                    }
                } else if (f == 3) {
                    frame.setFrameType("Short Large-T");
                    if (m == 2) {
                        // Machine 5
                        frame.setTierA1(true);
                    }
                } else if (f == 4) {
                    frame.setFrameType("Large-T");
                    if (m == 2) {
                        // Machine 5
                        frame.setTierA1(true);
                    } else if (m == 3) {
                        // Machine 6
                        frame.setTierA2(true);
                    } else if (m == 4) {
                        // Machine 9
                        frame.setTierB(true);
                    }
                } else if (f == 5) {
                    frame.setFrameType("Small Self Contain");
                    if (m == 2) {
                        // Machine 5
                        frame.setTierA1(true);
                    } else if (m == 3) {
                        // Machine 6
                        frame.setTierA2(true);
                    }
                } else if (f == 6) {
                    frame.setFrameType("Self Contain");
                    if (m == 4) {
                        // Machine 9
                        frame.setTierA1(true);
                    }
                } else if (f == 7) {
                    frame.setFrameType("XL-T");
                    if (m == 2) {
                        // Machine 5
                        frame.setTierB(true);
                    } else if (m == 4) {
                        // Machine 9
                        frame.setTierA1(true);
                    }
                } else {
                    System.out.println("Error: Not a current frame");
                    System.exit(0);
                }
                // Adding Frames to Hashmaps
                if (m == 1) {
                    mach2Frames.put(f, frame);
                } else if (m == 2) {
                    mach5Frames.put(f, frame);
                } else if (m == 3) {
                    mach6Frames.put(f, frame);
                } else if (m == 4) {
                    mach9Frames.put(f, frame);
                } else {
                    System.out.println("Error: Not a current machine");
                    System.exit(0);
                }
            }

        }
    }

    // Getter methods for start, end, availability and assignment properties of each machine
    public LocalDateTime getStartTime(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getStart();
    }

    public LocalDateTime getEndTime(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getEnd();
    }

    public boolean getAvailability(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getAvailability();
    }

    public String getAssignment(int machineNumber, int slotNumber) {
        return getMachine(machineNumber).get(slotNumber).getAssignment();
    }

    // setter methods for availability and assignment properties of each machine
    public void setAvailability(int machineNumber, int slotNumber, boolean availability) {
        getMachine(machineNumber).get(slotNumber).setAvailability(availability);
    }

    public void setAssignment(int machineNumber, int slotNumber, String assignment) {
        getMachine(machineNumber).get(slotNumber).setAssignment(assignment);
    }

    // Getter methods for frame type, tierA1, tierA2 and tierB compatibility properties of each machine
    public String getFrameType(int machineNumber, int frameNumber) {
        return getFrameList(machineNumber).get(frameNumber).getFrameType();
    }
    public boolean getTierA1(int machineNumber, int frameNumber) {
        return getFrameList(machineNumber).get(frameNumber).getTierA1();
    }
    public boolean getTierA2(int machineNumber, int frameNumber) {
        return getFrameList(machineNumber).get(frameNumber).getTierA2();
    }
    public boolean getTierB(int machineNumber, int frameNumber) {
        return getFrameList(machineNumber).get(frameNumber).getTierB();
    }
    

    // Helper method to get the machine based on the machine number
    private Map<Integer, Slot> getMachine(int machineNumber) {
        switch (machineNumber) {
            case 1:
                return mach2Slot;
            case 2:
                return mach5Slot;
            case 3:
                return mach6Slot;
            case 4:
                return mach9Slot;
            default:
                throw new IllegalArgumentException("Invalid machine number");
        }
    }

    // Helper method to get the frame hashmap based on the machine number
    private Map<Integer, Frame> getFrameList(int machineNumber) {
        switch (machineNumber) {
            case 1:
                return mach2Frames;
            case 2:
                return mach5Frames;
            case 3:
                return mach6Frames;
            case 4:
                return mach9Frames;
            default:
                throw new IllegalArgumentException("Invalid frane number");
        }
    }
}