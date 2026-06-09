import tkinter as tk
import json
import os
from functools import partial
from datetime import datetime

# Check in script
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

data_map = {
            'day': 'day_rating',
            'anxiety': 'anxiety_level',
            'productivity': 'productivity_level',
            'shark_week': 'shark_week'
        }

class DailyCheckIn:
    frame_config = {
        'day': {'label': 'Rate Your Day', 'buttons': 4, 'next': 'anxiety'},
        'anxiety': {'label': 'Anxiety Level', 'buttons': 4, 'next': 'productivity'},
        'productivity': {'label': 'Productivity Level', 'buttons': 4, 'next': 'shark_week'},
        'shark_week': {'label': 'Shark Week', 'buttons': 2, 'next': None},
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Daily Check-In")
        self.current_frame = None
        self.frames = {}
        
        # Create all frames
        for frame_name, config in self.frame_config.items():
            frame = tk.Frame(self.root)
            tk.Label(frame, text=config['label']).pack(pady=10)
            
            for i in range(config['buttons']):
                tk.Button(
                    frame,
                    text=f"{i+1}",
                    command=partial(self.handle_response, frame_name, i+1)
                ).pack(pady=5)
            
            self.frames[frame_name] = frame
        
        # Show the first frame
        self.show_frame('day')

    def show_frame(self, frame_name):
        if self.current_frame:
            self.current_frame.pack_forget()
        if frame_name in self.frames:
            self.current_frame = self.frames[frame_name]
            self.current_frame.pack()


    def handle_response(self, frame_name, value): 
        # Store the value (convert to bool for shark_week)
        if frame_name == 'shark_week':
            daily_data[data_map[frame_name]] = bool(value - 1)
        else:
            daily_data[data_map[frame_name]] = value
        
        # Print status
        print(f"{self.frame_config[frame_name]['label']}: {value}")
        
        # Move to next frame or end
        next_frame = self.frame_config[frame_name]['next']
        if next_frame:
            self.show_frame(next_frame)
        else:
            self.save_to_json()
            root.destroy()
    
    def save_to_json(self):
        # Create data folder if it doesn't exist
        data_folder = 'data'
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)
        
        # Create filename based on year and month
        filename = os.path.join(data_folder, f"check_in_{datetime.now().strftime('%Y_%m')}.json")
        today = datetime.now().strftime('%Y-%m-%d')
        
        # Create entry for today
        entry = {
            'daily_check_in': daily_data.copy(),
            'habits': habit_data.copy()
        }
        
        # Load existing data or create new
        try:
            with open(filename, 'r') as f:
                all_data = json.load(f)
        except FileNotFoundError:
            all_data = {}
        
        # Add today's entry
        all_data[today] = entry
        
        # Write back to file
        with open(filename, 'w') as f:
            json.dump(all_data, f, indent=2)
        print(f"Data saved to {filename}")

root = tk.Tk()
window_width = 300
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# Create and run the app
app = DailyCheckIn(root)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y - 100}")
root.mainloop()
    