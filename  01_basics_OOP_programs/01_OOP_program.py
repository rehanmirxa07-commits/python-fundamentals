class WaterTracker:
    def __init__(self,name):
        self.name = name 
        self.log = []
    def log_water(self,litres):
        self.log.append(litres)
    def total_water_intake(self):
        total_intake = 0 
        for litres in self.log:
            total_intake+=litres
        return total_intake
            

    def total_water_track(self):
        print(f"{self.name} drank a total of {self.total_water_intake()} liters of water today!")

tracker = WaterTracker("Rehan")
tracker.log_water(int(input("enter the no: ")))
tracker.log_water(int(input("enter the no: ")))
tracker.log_water(int(input("enter the no: ")))
tracker.total_water_track()
name = "rehan"
 