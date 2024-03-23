package src;
import java.time.LocalDateTime;

class Slot {
    private LocalDateTime slotStart;
    private LocalDateTime slotEnd;
    private boolean slotAvailability;
    private String slotAssignment;

    public Slot() {
        slotStart = null;
        slotEnd = null;
        slotAvailability = false; // This is showing whether its filled or not, false meaning, it can be assigned a job.
        slotAssignment = null;
    }

    // Getters for Start Time, End Time, Availability, and Assignment
    public LocalDateTime getStart() {
        return slotStart;
    }
    public LocalDateTime getEnd() {
        return slotEnd;
    }
    public boolean getAvailability() {
        return slotAvailability;
    }
    public String getAssignment() {
        return slotAssignment;
    }

    // Setters for Start Time, End Time, Availability, and Assignment
    public void setStart(LocalDateTime start) {
        this.slotStart = start;
    }
    public void setEnd(LocalDateTime end) {
        this.slotEnd = end;
    }
    public void setAvailability(boolean availability) {
        this.slotAvailability = availability;
    }
    public void setAssignment(String assignment) {
        this.slotAssignment = assignment;
    }
}

public class Timeslot {
    public static void main(String[] args) {

    }
}