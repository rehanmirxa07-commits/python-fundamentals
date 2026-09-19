class WorkoutTracker:
    def __init__(self,day):
        self.day = day 
        self.exercise = []
    def add_exercise(self, name):
        self.exercise.append(name)
    def show_workout(self):
        print(f"Wokouts for: {self.day}")
        for exercise in self.exercise:
            print(f" - {exercise}")

my_workout = WorkoutTracker("Monday")
my_workout.add_exercise("Bench Press")
my_workout.add_exercise("Incline Dumbbell Press")

my_workout.show_workout()

        

    