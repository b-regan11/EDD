package src;

class Frame {
    private String frameType;
    private boolean tierA; // True means it fits on machine
    private boolean tierB; // False means it does not fit on machine

    public Frame() {
        frameType = null;
        tierA = false;
        tierB = false;
    }

    // Getters for frameType, tierA, & tierB
    public String getFrameType() {
        return frameType;
    }
    public boolean getTierA() {
        return tierA;
    }
    public boolean getTierB() {
        return tierB;
    }

    // Setters for frameType, tierA, & tierB
    public void setFrameType(String frametype) {
        this.frameType = frametype;
    }
    public void setTierA(boolean tier_A) {
        this.tierA = tier_A;
    }
    public void setTierB(boolean tier_B) {
        this.tierB = tier_B;
    }
}

public class Frames {
    public static void main(String[] args) {

    }
}
