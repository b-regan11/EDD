package src;

class Frame {
    private String frameType;
    private boolean tierA1; // True means it fits on machine
    private boolean tierA2;
    private boolean tierB; // False means it does not fit on machine

    public Frame() {
        frameType = null;
        tierA1 = false;
        tierA2 = false;
        tierB = false;
    }

    // Getters for frameType, tierA1, tierA2, & tierB
    public String getFrameType() {
        return frameType;
    }
    public boolean getTierA1() {
        return tierA1;
    }
    public boolean getTierA2() {
        return tierA2;
    }
    public boolean getTierB() {
        return tierB;
    }

    // Setters for frameType, tierA1, tierA2, & tierB
    public void setFrameType(String frametype) {
        this.frameType = frametype;
    }
    public void setTierA1(boolean tier_A1) {
        this.tierA1 = tier_A1;
    }
    public void setTierA2(boolean tier_A2) {
        this.tierA2 = tier_A2;
    }
    public void setTierB(boolean tier_B) {
        this.tierB = tier_B;
    }
}

public class Frames {
    public static void main(String[] args) {

    }
}
