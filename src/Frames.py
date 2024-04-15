# class Frame:
#     def __init__(self):
#         self.frameType = None
#         self.tierA1 = False  # True means it fits on machine
#         self.tierA2 = False
#         self.tierB = False  # False means it does not fit on machine

#     # Getters for frameType, tierA1, tierA2, & tierB
#     def get_frame_type(self):
#         return self.frameType

#     def get_tier_a1(self):
#         return self.tierA1

#     def get_tier_a2(self):
#         return self.tierA2

#     def get_tier_b(self):
#         return self.tierB

#     # Setters for frameType, tierA1, tierA2, & tierB
#     def set_frame_type(self, frame_type):
#         self.frameType = frame_type

#     def set_tier_a1(self, tier_a1):
#         self.tierA1 = tier_a1

#     def set_tier_a2(self, tier_a2):
#         self.tierA2 = tier_a2

#     def set_tier_b(self, tier_b):
#         self.tierB = tier_b
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
