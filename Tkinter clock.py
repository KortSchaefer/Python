import tkinter as tk
from tkinter import ttk
from time import strftime

class ThemedClock(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Themed Clock")
        self.geometry("300x150")
        self.overrideredirect(True)  # Removes default window decorations (border, title)
        self.config(bg="#333333")

        # Transparent window support
        self.attributes("-alpha", 0.9)  # Slight transparency

        # Enable dragging the window by holding the label
        self.bind("<ButtonPress-1>", self.start_drag)
        self.bind("<B1-Motion>", self.do_drag)

        # Clock Label with custom font and style
        self.clock_label = ttk.Label(
            self, text="", font=("Helvetica", 48), background="#333333", foreground="#FFD700"
        )
        self.clock_label.pack(expand=True, pady=10)

        # Transparency Control Slider
        self.transparency_slider = ttk.Scale(
            self, from_=0.3, to=1.0, value=0.9, orient="horizontal", command=self.adjust_transparency
        )
        self.transparency_slider.pack(fill="x", padx=10)

        # Call the function to update the clock every second
        self.update_clock()

    def update_clock(self):
        """Update the time every second."""
        current_time = strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.after(1000, self.update_clock)

    def start_drag(self, event):
        """Store the initial position when dragging starts."""
        self._drag_data = {'x': event.x, 'y': event.y}

    def do_drag(self, event):
        """Reposition the window when dragging."""
        x = self.winfo_pointerx() - self._drag_data['x']
        y = self.winfo_pointery() - self._drag_data['y']
        self.geometry(f"+{x}+{y}")

    def adjust_transparency(self, value):
        """Adjust the window transparency using the slider value."""
        self.attributes("-alpha", float(value))

# Run the application
if __name__ == "__main__":
    clock_app = ThemedClock()
    clock_app.mainloop()
