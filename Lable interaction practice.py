import tkinter as tk

# Create the main window
root = tk.Tk()

# Function to handle the label click
def on_label_click(event):
    label = event.widget  # Get the clicked label widget
    effect1(label)  # Pass the label to effect1
    effect2(label)  # Pass the label to effect2
    effect3(label)  # Pass the label to effect3
    # You can add more effects as needed

# Example effect functions
def effect1(label):
    label.config(fg="red")  # Change the text color to red

def effect2(label):
    label.config(text="Clicked!")  # Change the label text

def effect3(label):
    label.destroy()  # Destroy the label (optional)

# Function to create multiple labels
def create_labels():
    for i in range(5):  # Creating 5 labels for demonstration
        label = tk.Label(root, text=f"Label {i+1}", fg="blue", cursor="hand2")
        label.bind("<Button-1>", on_label_click)  # Bind the click event
        label.pack(pady=5)  # Add some vertical spacing

# Call the function to create labels
create_labels()

# Start the main loop
root.mainloop()
