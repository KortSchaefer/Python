import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re
#%% THIS DIDNT WORK
class SyntaxNotepad(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Syntax Notepad")
        self.geometry("800x800")

        # Text widget with Scrollbar
        self.text_widget = tk.Text(self, wrap="word", undo=True, font=("Courier", 12))
        self.text_widget.pack(expand=True, fill="both", side="left")

        self.scrollbar = ttk.Scrollbar(self, command=self.text_widget.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_widget.config(yscrollcommand=self.scrollbar.set)

        # Menubar
        self.create_menubar()

        # Syntax highlighting setup
        self.text_widget.bind("<KeyRelease>", self.on_key_release)

        # Python keywords for highlighting
        self.keywords = [
            "def", "class", "if", "else", "elif", "return", "import", "from", 
            "for", "while", "try", "except", "with", "as", "pass", "break", 
            "continue", "lambda", "in", "is", "and", "or", "not"
        ]

    def create_menubar(self):
        """Creates the menu bar with file operations."""
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        menubar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menubar)

    def new_file(self):
        """Clears the text widget for a new file."""
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        """Opens a text file and loads its content."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        """Saves the content of the text widget to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_widget.get(1.0, tk.END))

    def on_key_release(self, event):
        """Syntax highlighting after a key is released."""
        self.highlight_keywords()

    def highlight_keywords(self):
        """Highlights Python keywords in the text widget."""
        self.text_widget.tag_remove("keyword", "1.0", tk.END)

        # Search for keywords using regex
        pattern = r'\b(' + '|'.join(self.keywords) + r')\b'
        text = self.text_widget.get("1.0", tk.END)

        for match in re.finditer(pattern, text):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            self.text_widget.tag_add("keyword", start, end)

        # Styling the highlighted keywords
        self.text_widget.tag_config("keyword", foreground="blue", font=("Courier", 12, "bold"))

# Run the application
if __name__ == "__main__":
    app = SyntaxNotepad()
    app.mainloop()
