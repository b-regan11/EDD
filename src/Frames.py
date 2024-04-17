class Frame:
    def __init__(self):
        self.name = None
        self.tierA1 = 0  # 0 means that by default no machine was assigned tier A1 for this frame
        self.tierA2 = 0
        self.tierB = 0  
    
    # Getters for frame name and machine for tiers A1, A2, & B
    def get_name(self):
        return self.name
    
    def get_tierA1(self):
        return self.tierA1
    
    def get_tierA2(self):
        return self.tierA2
    
    def get_tierB(self):
        return self.tierB

    # Setters for frame name and machine for tiers A1, A2, & B
    def set_name(self, frame_name):
        self.name = frame_name
    
    def set_tierA1(self, machine):
        self.tierA1 = machine

    def set_tierA2(self, machine):
        self.tierA2 = machine

    def set_tierB(self, machine):
        self.tierB = machine
