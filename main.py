import tkinter as tk
from functools import partial

daily_data = {
    'day_rating': None,
    'anxiety_level': None,
    'productivity_level': None,
    'shark_week': False
}

habit_data = {
    'exercise': False,
    'shower': False,
    'guitar': False
}

class DailyCheckIn:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Check-In")
        self.current_frame = None
        
        self.frame_day = tk.Frame(root)
        self.frame_anxiety = tk.Frame(root)
        self.frame_productivity = tk.Frame(root)
        self.frame_shark_week = tk.Frame(root)
        self.frame_habits = tk.Frame(root)
        
        self.setup_frame_day()
        self.setup_frame_anxiety()
        self.setup_frame_productivity()
        self.setup_frame_shark_week()
        self.setup_frame_habits()
        
        self.show_frame(self.frame_day)
    

    def show_frame(self, frame):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = frame
        frame.pack()
    
    # Check Day
    def setup_frame_day(self):
        tk.Label(self.frame_day, text="Rate Your Day").pack()
        for i in range(4):
            tk.Button(self.frame_day, text=f"Rating {i+1}", 
                     command=partial(self.rate_day, i+1)).pack()
    
    def rate_day(self, value):
        daily_data['day_rating'] = value
        print(f"Day rating: {value}")
        self.show_frame(self.frame_anxiety)
    
    # Check Anxiety
    def setup_frame_anxiety(self):
        tk.Label(self.frame_anxiety, text="Anxiety Level").pack()
        for i in range(4):
            tk.Button(self.frame_anxiety, text=f"Level {i+1}", 
                     command=partial(self.rate_anxiety, i+1)).pack()
    
    def rate_anxiety(self, value):
        daily_data['anxiety_level'] = value
        print(f"Anxiety level: {value}")
        self.show_frame(self.frame_productivity)
    
    # Check Productivity
    def setup_frame_productivity(self):
        tk.Label(self.frame_productivity, text="Productivity Level").pack()
        for i in range(4):
            tk.Button(self.frame_productivity, text=f"Level {i+1}", 
                     command=partial(self.rate_productivity, i+1)).pack()
    
    def rate_productivity(self, value):
        daily_data['productivity_level'] = value
        print(f"Productivity level: {value}")
        self.show_frame(self.frame_shark_week)
    
    # Check Shark Week
    def setup_frame_shark_week(self):
        tk.Label(self.frame_shark_week, text="Shark Week").pack()
        for i in range(2):
            tk.Button(self.frame_shark_week, text=f"Option {i}", 
                     command=partial(self.check_shark_week, i)).pack()
    
    def check_shark_week(self, value):
        daily_data['shark_week'] = bool(value)
        print(f"Shark week: {value}")
        print("Check-in complete!")
        self.show_frame(self.frame_habits)

    # Habit Tracker
    # Check Exercise
    def check_exercise(self, value):
        habit_data['exercise'] = bool(value)
        print("Exercise checked!") 

    def check_shower(self, value):
        habit_data['shower'] = bool(value)
        print("Shower checked!")

    def check_guitar(self, value):
        habit_data['guitar'] = bool(value)
        print("Guitar checked!")

    def setup_frame_habits(self):
        tk.Label(self.frame_habits, text="Habit Tracker").pack()
        tk.Checkbutton(self.frame_habits, text="Exercise", 
                       command=partial(self.check_exercise, 1)).pack()
        tk.Checkbutton(self.frame_habits, text="Shower", 
                       command=partial(self.check_shower, 1)).pack()
        tk.Checkbutton(self.frame_habits, text="Guitar", 
                       command=partial(self.check_guitar, 1)).pack()
        tk.Button(self.frame_habits, text="Finish", command=self.finish).pack()

root = tk.Tk()
app = DailyCheckIn(root)
root.mainloop()