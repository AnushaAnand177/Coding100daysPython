import tkinter as tk
from tkinter import ttk

class PomodoroTimer:
    def __init__(self, master):  # Add master parameter
        self.master = master     # Store the master window
        self.WORK_TIME = 25 * 60
        self.SHORT_BREAK = 5 * 60
        self.LONG_BREAK = 15 * 60
        self.current_time = self.WORK_TIME
        self.timer_running = False
        self.sessions_completed = 0
        self.timer_id = None
        self.current_session = "Work"

    def start_timer(self):
        """Start or resume the timer"""
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()
    
    def pause_timer(self):
        """Pause the timer"""
        self.timer_running = False
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
            self.timer_id = None
    
    def reset_timer(self):
        """Reset the timer to initial state"""
        self.pause_timer()
        self.current_time = self.WORK_TIME
        self.current_session = "Work"
        self.sessions_completed = 0
        self.update_display()
        self.update_session_label()
        self.update_counter()
    
    def update_timer(self):
        """Update timer every second"""
        if self.timer_running and self.current_time > 0:
            self.current_time -= 1
            self.update_display()
            self.timer_id = self.master.after(1000, self.update_timer)
        elif self.current_time <= 0:
            self.check_session_completion()
    
    def switch_session(self):
        """Switch between work and break sessions"""
        if self.current_session == "Work":
            self.sessions_completed += 1
            if self.sessions_completed % 4 == 0:
                self.current_session = "Long Break"
                self.current_time = self.LONG_BREAK
            else:
                self.current_session = "Short Break"
                self.current_time = self.SHORT_BREAK
        else:
            self.current_session = "Work"
            self.current_time = self.WORK_TIME
        
        self.update_session_label()
        self.update_counter()
    
    def countdown(self):
        """Main countdown logic"""
        if self.current_time > 0:
            self.current_time -= 1
            self.update_display()
            if self.timer_running:
                self.master.after(1000, self.countdown)
        else:
            self.check_session_completion()
    
    @staticmethod
    def format_time(seconds):
        """Convert seconds to MM:SS format"""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def check_session_completion(self):
        """Check if current session is complete and handle transition"""
        self.pause_timer()
        # Play notification sound (if implemented)
        self.switch_session()
        # Optional: Auto-start next session
        self.start_timer()
    
    def update_display(self):
        """Update the timer display"""
        formatted_time = self.format_time(self.current_time)
        self.timer_label.config(text=formatted_time)
        
        # Update progress bar if implemented
        progress = (self.WORK_TIME - self.current_time) / self.WORK_TIME * 100
        self.progress_bar['value'] = progress
    
    def update_session_label(self):
        """Update the session type label"""
        self.session_label.config(
            text=f"Current Session: {self.current_session}",
            fg="green" if self.current_session != "Work" else "red"
        )
    
    def update_counter(self):
        """Update the sessions counter"""
        self.counter_label.config(
            text=f"Sessions Completed: {self.sessions_completed}"
        )

# Update the main section:
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pomodoro Timer")
    
    # Pass root to PomodoroTimer
    app = PomodoroTimer(root)
    
    # Create basic GUI elements
    app.timer_label = tk.Label(
        root, 
        text="25:00", 
        font=("Arial", 30)
    )
    app.timer_label.pack(pady=20)
    
    app.session_label = tk.Label(
        root, 
        text="Current Session: Work",
        font=("Arial", 12)
    )
    app.session_label.pack()
    
    app.counter_label = tk.Label(
        root, 
        text="Sessions Completed: 0",
        font=("Arial", 12)
    )
    app.counter_label.pack()
    
    app.progress_bar = ttk.Progressbar(
        root,
        length=300,
        mode='determinate'
    )
    app.progress_bar.pack(pady=10)
    
    # Control buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)
    
    tk.Button(
        button_frame,
        text="Start",
        command=app.start_timer
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame,
        text="Pause",
        command=app.pause_timer
    ).pack(side=tk.LEFT, padx=5)
    
    tk.Button(
        button_frame,
        text="Reset",
        command=app.reset_timer
    ).pack(side=tk.LEFT, padx=5)
    
    root.mainloop()