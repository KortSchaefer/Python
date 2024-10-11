import tkinter as tk

class ScrollingButtonWheel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create a canvas for scrolling
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.button_frame = tk.Frame(self.canvas)

        # Configure the canvas
        self.button_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create a window in the canvas
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")

        # Set up the scrollbar
        self.canvas.config(xscrollcommand=self.scrollbar.set)

        # Pack the canvas and scrollbar
        self.scrollbar.pack(side="bottom", fill="x")
        self.canvas.pack(side="top", fill="both", expand=True)

        # Initialize button counter and maximum buttons
        self.button_count = 0
        self.max_buttons = 20  # Change this to the desired number of buttons

        # Button to add the next button
        self.add_button = tk.Button(self, text="Add Button", command=self.add_next_button)
        self.add_button.pack(pady=10)

    def add_next_button(self):
        if self.button_count < self.max_buttons:
            button = tk.Button(self.button_frame, text=f"Button {self.button_count + 1}", 
                               command=lambda i=self.button_count: self.on_button_click(i))
            button.pack(side="left", padx=5, pady=5)  # Pack buttons horizontally
            self.button_count += 1  # Increment the counter

    def on_button_click(self, index):
        print(f"Button {index + 1} clicked!")

# Main application
root = tk.Tk()
root.title("Dynamic Horizontal Scrolling Button Wheel")

# Create an instance of the scrolling button wheel
scrolling_button_wheel = ScrollingButtonWheel(root)
scrolling_button_wheel.pack(fill="both", expand=True)

# Start the main loop
root.mainloop()
