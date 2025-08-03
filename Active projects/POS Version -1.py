"""
Program: POS Version -1.py
Author: Kort Schaefer 
Date: 08/03/2025
Desc: This program is a point of sale system designed for a restaurant. A tutorial is provided in the zip file as tutorial.pdf
Note: This program is not fully functional and is a work in progress, some features are not implemented yet, and are not ment to work yet.
"""

from tkinter import *
from PIL import ImageTk, Image

class POSSystem:
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        self.root.title("POS System")
        self.root.iconbitmap(r"C:\Users\Kingc\Documents\Code\Python\Practice Images\code.ico")
        self.root.configure(bg="lightblue")
        
        # Screen configuration
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.attributes('-fullscreen', True)
        self.root.bind("<Escape>", lambda event: self.root.attributes('-fullscreen', False))
        
        # UI sizing variables
        self.font_size = int(self.screen_width/160)
        self.button_width = int(self.screen_width/180)
        self.button_height = int(self.screen_height/300)
        
        # Order management variables
        self.order_cost_total = 0
        self.current_order = []
        self.highlighted_labels = []
        self.current_seat = "table"
        self.current_row = 0
        self.current_column = 0
        self.max_rows = 60
        
        # Price configuration
        self.soft_drinks_price = 3.49
        self.apps_price = 8.99
        self.tea_special_price = 4.49
        self.apps_meal_price = 12.99
        self.side_salads_price = 6.99
        self.steaks_price = 24.99
        
        # Initialize seat orders
        self.seat_orders = {
            "table": {},
            **{f"seat{i}": {} for i in range(1, 21)}
        }
        
        # Create UI components
        self.create_frames()
        self.create_buttons()
        self.setup_layout()
        
    def create_frames(self):
        """Create all the UI frames"""
        # Order frame wrapper
        self.order_frame_wrapper = LabelFrame(self.root, text="Order Box", relief='raised', bg='white')
        self.order_frame_wrapper.grid_propagate(False)
        self.order_frame_wrapper.grid(column=0, row=1)
        self.order_frame_wrapper.grid_columnconfigure(0, weight=1)
        self.order_frame_wrapper.grid_rowconfigure((0), weight=10)
        self.order_frame_wrapper.grid_rowconfigure((1), weight=1)

        self.order_frame = LabelFrame(self.order_frame_wrapper, text="Order Box", relief='raised', bg='white')
        # Remove grid_propagate(False) to allow the frame to expand with content
        self.order_frame.grid(column=0, row=0, sticky='nsew')
        self.order_frame.grid_columnconfigure(0, weight=1)

        self.order_scroll_frame = LabelFrame(self.order_frame_wrapper, text="scroll Box", relief='raised', bg='white')
        self.order_scroll_frame.grid_propagate(False)
        self.order_scroll_frame.grid(column=0, row=1, padx=2, pady=2)

        # Entry frame
        self.entry_frame = LabelFrame(self.root, text="Entry Box", relief='raised')
        self.entry_frame.grid(column=2, row=1, padx=(2,15), pady=2)
        Label(self.entry_frame, text='Box').pack()

        # Scroll frame
        self.scroll_frame = LabelFrame(self.root, text="Scroll Box", relief='raised')
        self.scroll_frame.grid_propagate(False)
        self.scroll_frame.grid(column=1, row=1, padx=2, pady=2)
        self.scroll_frame.grid_columnconfigure(0, weight=1)

        # Top frame
        self.top_frame = LabelFrame(self.root, text="Top Box", relief='raised')
        self.top_frame.grid(column=0, row=0, padx=2, pady=2, columnspan=4)
        
        # Create a frame to hold logo and buttons horizontally
        top_content_frame = Frame(self.top_frame)
        top_content_frame.pack(expand=True, fill='both')
        
        # Add logo to the left side
        try:
            # Load and resize the logo image
            logo_image = Image.open("logos_roadhouse_logo.png")
            
            # Handle different PIL versions for resizing
            try:
                # Try newer PIL version first
                logo_image = logo_image.resize((150, 80), Image.Resampling.LANCZOS)
            except AttributeError:
                try:
                    # Try older PIL version
                    logo_image = logo_image.resize((150, 80), Image.ANTIALIAS)
                except AttributeError:
                    # Fallback to basic resize
                    logo_image = logo_image.resize((150, 80))
            
            logo_photo = ImageTk.PhotoImage(logo_image)
            
            logo_label = Label(top_content_frame, image=logo_photo)
            logo_label.image = logo_photo  # Keep a reference
            logo_label.pack(side='left', padx=10, pady=5)
        except Exception as e:
            # If image not found or any error, create a text placeholder
            logo_label = Label(top_content_frame, text="LOGOS\nROADHOUSE", 
                             font=("Arial", 12, "bold"), fg="red", bg="white")
            logo_label.pack(side='left', padx=10, pady=5)
            print(f"Logo loading error: {e}")
        
        # Create a frame to hold buttons horizontally
        button_frame = Frame(top_content_frame)
        button_frame.pack(side='right', expand=True, fill='both')
        
        # Add exit button to top frame (centered)
        exit_button = Button(button_frame, text="EXIT", command=self.root.quit, 
                           font=("Arial", self.font_size + 4, "bold"), 
                           bg="red", fg="white", padx=30, pady=10)
        exit_button.pack(side='left', expand=True, pady=10)
        
        # Add order button to top frame (right side)
        order_button = Button(button_frame, text="ORDER", command=self.get_check, 
                            font=("Arial", self.font_size + 4, "bold"), 
                            bg="green", fg="white", padx=30, pady=10)
        order_button.pack(side='right', pady=10, padx=10)

        # Bottom frames
        self.bottom_left_frame = LabelFrame(self.root, text="Bottom Box", relief='raised')
        self.bottom_left_frame.grid(column=0, row=2, padx=2, pady=2)
        Label(self.bottom_left_frame, text='Box').grid(column=0, row=0)

        self.bottom_frame = LabelFrame(self.root, text="Bottom Box", relief='raised')
        self.bottom_frame.grid(column=1, row=2, padx=2, pady=2)
        Label(self.bottom_frame, text='Box').grid(column=0, row=0)

        self.bottom_right_frame = LabelFrame(self.root, text="Bottom Box", relief='raised')
        self.bottom_right_frame.grid(column=2, row=2, padx=2, pady=2)
        Label(self.bottom_right_frame, text='Box').grid(column=0, row=0)

    def create_buttons(self):
        """Create all the buttons"""
        # Bottom left buttons
        bottom_left_buttons = [
            {"name": "Close", "command": self.close},
            {"name": "Next Seat", "command": self.next_seat}
        ]
        
        for i, button_info in enumerate(bottom_left_buttons):
            button = Button(self.bottom_left_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5)
            button.grid(row=0, column=i, padx=5, pady=5, sticky="W")

        # Bottom right buttons
        bottom_right_buttons = [
            {"name": "Get Check", "command": self.get_check},
            {"name": "Recipe", "command": self.get_recipe},
            {"name": "Quantity", "command": self.get_quantity},
            {"name": "Repeat", "command": self.repeat},
            {"name": "Modify", "command": self.modify},
            {"name": "Delete", "command": self.delete},
            {"name": "Rapid Fire", "command": self.rapid_fire}
        ]
        
        for i, button_info in enumerate(bottom_right_buttons):
            button = Button(self.bottom_right_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5)
            button.grid(row=0, column=abs(i-12), padx=5, pady=5, sticky='EN')

        # Scroll frame buttons
        scroll_buttons = [
            {"name": "Soft Drinks", "command": self.soft_drinks},
            {"name": "Tea & Special", "command": self.tea_special},
            {"name": "Apps", "command": self.apps},
            {"name": "Apps\nas meal", "command": self.apps_meal},
            {"name": "Side\nsalads", "command": self.side_salads},
            {"name": "Steaks", "command": self.steaks},
        ]
        
        for i, button_info in enumerate(scroll_buttons):
            button = Button(self.scroll_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size))
            button.grid(row=i, column=0, padx=5, pady=5, sticky='WEN')

    def setup_layout(self):
        """Setup the layout configuration"""
        # Frame anchoring
        frames = [self.entry_frame, self.scroll_frame, self.top_frame, self.bottom_frame, 
                 self.bottom_left_frame, self.bottom_right_frame, 
                 self.order_scroll_frame, self.order_frame_wrapper]
        
        for frame in frames:
            frame.grid(sticky='NSWE')
            frame.grid_propagate(0)

        # Root configuration
        self.root.rowconfigure(0, weight=1)  # Reduced from weight=2
        self.root.columnconfigure(0, weight=12)
        self.root.rowconfigure(1, weight=24)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(2, weight=2)
        self.root.columnconfigure(2, weight=24)

    def if_clicked(self, event):
        """Handle label click events for highlighting"""
        label = event.widget
        
        if label in self.highlighted_labels:
            # If it is highlighted, reset its appearance and remove from the list
            label.config(bg="SystemButtonFace", highlightthickness=0)
            self.highlighted_labels.remove(label)
        else:
            # If it is not highlighted, highlight it and add to the list
            label.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
            label.config(bg="yellow")
            self.highlighted_labels.append(label)

    def add_to_order(self, name, price, sides=None):
        """Add an item to the current order"""
        if self.current_seat not in self.seat_orders:
            self.seat_orders[self.current_seat] = {}

        entree_num = len(self.seat_orders[self.current_seat]) + 1
        entree_key = f"Entree {entree_num}"

        self.seat_orders[self.current_seat][entree_key] = {
            "name": name,
            "price": price,
            "sides": sides if sides else {}
        }

        # Add seat label if first item
        if len(self.seat_orders[self.current_seat]) == 1:
            seat_label = Label(self.order_frame, text=f"{self.current_seat}", 
                             font=("Arial", self.font_size + 2, "bold"))
            seat_label.grid(row=len(self.order_frame.winfo_children()), column=0, 
                          padx=10, pady=5, sticky="w")

        # Display the entree
        display_name = name + " " * (100 - 2 * len(name)) + "$" + str(price)
        order_label = Label(self.order_frame, text=display_name, cursor="hand2")
        order_label.grid(row=len(self.order_frame.winfo_children()), column=0, 
                        padx=10, pady=5, sticky="w")
        order_label.bind("<Button-1>", self.if_clicked)

        self.order_cost_total += price
        
        # Force update the order frame
        self.order_frame.update()

    def set_current_seat(self, seat_number):
        """Set the current seat"""
        if seat_number in self.seat_orders:
            self.current_seat = seat_number
            print(f"Current seat set to {self.current_seat}")
        else:
            print(f"Seat {seat_number} does not exist")

    def soft_drinks(self):
        """Display soft drinks menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for soft drinks
        soft_drinks_data = [
            {"name": "Coke", "command": lambda: self.add_to_order('Coke', self.soft_drinks_price)},
            {"name": "Diet Coke", "command": lambda: self.add_to_order('Diet Coke', self.soft_drinks_price)},
            {"name": "Sprite", "command": lambda: self.add_to_order('Sprite', self.soft_drinks_price)},
            {"name": "Mr. Pib", "command": lambda: self.add_to_order('Mr. Pib', self.soft_drinks_price)},
            {"name": "Lemonade", "command": lambda: self.add_to_order('Lemonade', self.soft_drinks_price)},
            {"name": "Mellow\nYellow", "command": lambda: self.add_to_order('Mellow Yellow', self.soft_drinks_price)},
            {"name": "Coke\nZero", "command": lambda: self.add_to_order('Coke Zero', self.soft_drinks_price)},
            {"name": "Fruit\nPunch", "command": lambda: self.add_to_order('Fruit Punch', self.soft_drinks_price)},
            {"name": "Tonic Water", "command": lambda: self.add_to_order('Tonic Water', self.soft_drinks_price)},    
            {"name": "Root Beer", "command": lambda: self.add_to_order('Root Beer', self.soft_drinks_price)},        
            {"name": "Dr Pepper", "command": lambda: self.add_to_order('Dr Pepper', self.soft_drinks_price)},        
            {"name": "Rasp Tea Ftn", "command": lambda: self.add_to_order('Rasp Tea Ftn', self.soft_drinks_price)},
            {"name": " ", "command": lambda: None}, 
            {"name": " ", "command": lambda: None}, 
            {"name": " ", "command": lambda: None}, 
            {"name": " ", "command": lambda: None}, 
            {"name": "Sweet Tea", "command": lambda: self.add_to_order('Sweet Tea', self.soft_drinks_price)},
            {"name": "Hot Tea", "command": lambda: self.add_to_order('Hot Tea', self.soft_drinks_price)},  
            {"name": "Coffee", "command": lambda: self.add_to_order('Coffee', self.soft_drinks_price)},    
            {"name": "Iced Tea", "command": lambda: self.add_to_order('Iced Tea', self.soft_drinks_price)},
            {"name": " ", "command": lambda: None},   
            {"name": "Hot Cocoa", "command": lambda: self.add_to_order('Hot Cocoa', self.soft_drinks_price)},    
            {"name": "Decaf Coffee", "command": lambda: self.add_to_order('Decaf Coffee', self.soft_drinks_price)},
            {"name": " ", "command": lambda: None},  
            {"name": "No Bev", "command": lambda: self.add_to_order('No Bev', self.soft_drinks_price)},
            {"name": " ", "command": lambda: None},  
            {"name": " ", "command": lambda: None},  
            {"name": "Water", "command": lambda: self.add_to_order('Water', self.soft_drinks_price)}     
        ]

        # Create buttons
        for button_info in soft_drinks_data:
            if button_info["name"] == " ":
                col_offset += 1
                button = Button(self.entry_frame, text=button_info["name"], 
                              command=button_info["command"], font=("Arial", self.font_size), 
                              padx=20, pady=5, width=self.button_width, height=self.button_height, 
                              state=DISABLED, highlightthickness=0, borderwidth=0)
                button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
                if col_offset == 4:
                    col_offset = 0
                    row_offset += 1
            else:
                col_offset += 1
                button = Button(self.entry_frame, text=button_info["name"], 
                              command=button_info["command"], font=("Arial", self.font_size), 
                              padx=20, pady=5, width=self.button_width, height=self.button_height)
                button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
                if col_offset == 4:
                    col_offset = 0
                    row_offset += 1

    def tea_special(self):
        """Display tea and special menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for tea and special
        tea_special_data = [
            # Unsweet Tea variants
            {"name": "Blue Crush\nUnsweet", "command": lambda: self.add_to_order('Blue Crush Unsweet Tea', self.tea_special_price)},
            {"name": "Strawberry\nUnsweet", "command": lambda: self.add_to_order('Strawberry Unsweet Tea', self.tea_special_price)},
            {"name": "Raspberry\nUnsweet", "command": lambda: self.add_to_order('Raspberry Unsweet Tea', self.tea_special_price)},
            {"name": "Peach\nUnsweet", "command": lambda: self.add_to_order('Peach Unsweet Tea', self.tea_special_price)},
            
            # Sweet Tea variants
            {"name": "Blue Crush\nSweet", "command": lambda: self.add_to_order('Blue Crush Sweet Tea', self.tea_special_price)},
            {"name": "Strawberry\nSweet", "command": lambda: self.add_to_order('Strawberry Sweet Tea', self.tea_special_price)},
            {"name": "Raspberry\nSweet", "command": lambda: self.add_to_order('Raspberry Sweet Tea', self.tea_special_price)},
            {"name": "Peach\nSweet", "command": lambda: self.add_to_order('Peach Sweet Tea', self.tea_special_price)},
            
            # Lemonade variants
            {"name": "Blue Crush\nLemonade", "command": lambda: self.add_to_order('Blue Crush Lemonade', self.tea_special_price)},
            {"name": "Strawberry\nLemonade", "command": lambda: self.add_to_order('Strawberry Lemonade', self.tea_special_price)},
            {"name": "Raspberry\nLemonade", "command": lambda: self.add_to_order('Raspberry Lemonade', self.tea_special_price)},
            {"name": "Peach\nLemonade", "command": lambda: self.add_to_order('Peach Lemonade', self.tea_special_price)}
        ]

        # Create buttons
        for button_info in tea_special_data:
            col_offset += 1
            button = Button(self.entry_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5, width=self.button_width, height=self.button_height)
            button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
            if col_offset == 4:
                col_offset = 0
                row_offset += 1

    def apps(self):
        """Display apps menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for apps (using the existing apps_data list)
        apps_data = [
            {"name": "Cactus\nBlossom", "command": lambda: self.add_to_order('Cactus Blossom', self.apps_price)},
            {"name": "Potato\nSkins", "command": lambda: self.add_to_order('Potato Skins', self.apps_price)},
            {"name": "Mozzorela\nTwists", "command": lambda: self.add_to_order('Mozzorela Twists', self.apps_price)},
            {"name": "Rattlesnake\nBites", "command": lambda: self.add_to_order('Rattlesnake Bites', self.apps_price)},
            {"name": "Cheese\nFries", "command": lambda: self.add_to_order('Cheese Fries', self.apps_price)},
            {"name": "Boneless\nWings", "command": lambda: self.add_to_order('Boneless Wings', self.apps_price)},
            {"name": "Fried\nPickles", "command": lambda: self.add_to_order('Fried Pickles', self.apps_price)},
            {"name": "Rib App", "command": lambda: self.add_to_order('Rib App', self.apps_price)},
            {"name": "Chili", "command": lambda: self.add_to_order('Chili', self.apps_price)},
            {"name": "Combo\nApp", "command": lambda: self.add_to_order('Combo App', self.apps_price)},
            {"name": "Shrimp\nApp", "command": lambda: self.add_to_order('Shrimp App', self.apps_price)}
        ]

        # Create buttons
        for button_info in apps_data:
            col_offset += 1
            button = Button(self.entry_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5, width=self.button_width, height=self.button_height)
            button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
            if col_offset == 4:
                col_offset = 0
                row_offset += 1

    def apps_meal(self):
        """Display apps as meal menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for apps as meal (using the same apps data but with meal price)
        apps_meal_data = [
            {"name": "Cactus\nBlossom\nMeal", "command": lambda: self.add_to_order('Cactus Blossom Meal', self.apps_meal_price)},
            {"name": "Potato\nSkins\nMeal", "command": lambda: self.add_to_order('Potato Skins Meal', self.apps_meal_price)},
            {"name": "Mozzorela\nTwists\nMeal", "command": lambda: self.add_to_order('Mozzorela Twists Meal', self.apps_meal_price)},
            {"name": "Rattlesnake\nBites\nMeal", "command": lambda: self.add_to_order('Rattlesnake Bites Meal', self.apps_meal_price)},
            {"name": "Cheese\nFries\nMeal", "command": lambda: self.add_to_order('Cheese Fries Meal', self.apps_meal_price)},
            {"name": "Boneless\nWings\nMeal", "command": lambda: self.add_to_order('Boneless Wings Meal', self.apps_meal_price)},
            {"name": "Fried\nPickles\nMeal", "command": lambda: self.add_to_order('Fried Pickles Meal', self.apps_meal_price)},
            {"name": "Rib App\nMeal", "command": lambda: self.add_to_order('Rib App Meal', self.apps_meal_price)},
            {"name": "Chili\nMeal", "command": lambda: self.add_to_order('Chili Meal', self.apps_meal_price)},
            {"name": "Combo\nApp\nMeal", "command": lambda: self.add_to_order('Combo App Meal', self.apps_meal_price)},
            {"name": "Shrimp\nApp\nMeal", "command": lambda: self.add_to_order('Shrimp App Meal', self.apps_meal_price)}
        ]

        # Create buttons
        for button_info in apps_meal_data:
            col_offset += 1
            button = Button(self.entry_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5, width=self.button_width, height=self.button_height)
            button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
            if col_offset == 4:
                col_offset = 0
                row_offset += 1

    def side_salads(self):
        """Display side salads menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for side salads
        side_salads_data = [
            {"name": "House\nApp", "command": lambda: self.add_to_order('House App', self.side_salads_price)},
            {"name": "Cezar\nApp", "command": lambda: self.add_to_order('Cezar App', self.side_salads_price)},
            {"name": "LG House\nApp", "command": lambda: self.add_to_order('LG House App', self.side_salads_price)},
            {"name": "LG Cezar\nApp", "command": lambda: self.add_to_order('LG Cezar App', self.side_salads_price)}
        ]

        # Create buttons
        for button_info in side_salads_data:
            col_offset += 1
            button = Button(self.entry_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5, width=self.button_width, height=self.button_height)
            button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
            if col_offset == 4:
                col_offset = 0
                row_offset += 1

    def steaks(self):
        """Display steaks menu"""
        # Clear previous buttons
        for widget in self.entry_frame.winfo_children():
            if isinstance(widget, Button):
                widget.destroy()
        
        # Setting buttons to middle
        self.entry_frame.columnconfigure((0,5), weight=1)
        
        # Row and column offset variables for positioning
        row_offset = 0
        col_offset = 0
        
        # Button data for steaks
        steaks_data = [
            {"name": "6oz\nSirloin", "command": lambda: self.add_to_order('6oz Sirloin', self.steaks_price)},
            {"name": "8oz\nSirloin", "command": lambda: self.add_to_order('8oz Sirloin', self.steaks_price)},
            {"name": "11oz\nSirloin", "command": lambda: self.add_to_order('11oz Sirloin', self.steaks_price)},
            {"name": "16oz\nSirloin", "command": lambda: self.add_to_order('16oz Sirloin', self.steaks_price)},
            {"name": "6oz\nFilet", "command": lambda: self.add_to_order('6oz Filet', self.steaks_price)},
            {"name": "8oz\nFilet", "command": lambda: self.add_to_order('8oz Filet', self.steaks_price)},
            {"name": "8oz\nStrip", "command": lambda: self.add_to_order('8oz Strip', self.steaks_price)},
            {"name": "12oz\nStrip", "command": lambda: self.add_to_order('12oz Strip', self.steaks_price)},
            {"name": "12oz\nRibeye", "command": lambda: self.add_to_order('12oz Ribeye', self.steaks_price)},
            {"name": "14oz\nRibeye", "command": lambda: self.add_to_order('14oz Ribeye', self.steaks_price)},
            {"name": "16oz\nRibeye", "command": lambda: self.add_to_order('16oz Ribeye', self.steaks_price)},
            {"name": "Bone in", "command": lambda: self.add_to_order('Bone in', self.steaks_price)},
            {"name": "Porterhouse", "command": lambda: self.add_to_order('Porterhouse', self.steaks_price)}
        ]

        # Create buttons
        for button_info in steaks_data:
            col_offset += 1
            button = Button(self.entry_frame, text=button_info["name"], 
                          command=button_info["command"], font=("Arial", self.font_size), 
                          padx=20, pady=5, width=self.button_width, height=self.button_height)
            button.grid(row=row_offset, column=col_offset, padx=15, pady=15, sticky="W")
            if col_offset == 4:
                col_offset = 0
                row_offset += 1

    def get_check(self):
        """Generate order check and save to text file"""
        import datetime
        
        # Get current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"order_{timestamp}.txt"
        
        # Create order summary
        order_summary = []
        order_summary.append("=" * 50)
        order_summary.append("RESTAURANT ORDER RECEIPT")
        order_summary.append("=" * 50)
        order_summary.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        order_summary.append("")
        
        total_cost = 0
        
        # Process each seat's orders
        for seat, orders in self.seat_orders.items():
            if orders:  # Only process seats with orders
                order_summary.append(f"--- {seat.upper()} ---")
                
                for entree_key, entree_data in orders.items():
                    name = entree_data["name"]
                    price = entree_data["price"]
                    total_cost += price
                    
                    # Format the line with proper spacing
                    price_str = f"${price:.2f}"
                    line = f"{name:<30} {price_str:>10}"
                    order_summary.append(line)
                
                order_summary.append("")
        
        # Add total
        order_summary.append("=" * 50)
        order_summary.append(f"TOTAL: ${total_cost:.2f}")
        order_summary.append("=" * 50)
        
        # Write to file
        try:
            with open(filename, 'w') as f:
                for line in order_summary:
                    f.write(line + '\n')
            
            print(f"Order saved to: {filename}")
            print("Order Summary:")
            for line in order_summary:
                print(line)
                
        except Exception as e:
            print(f"Error saving order: {e}")
        
        # Clear the order after saving
        self.clear_order()
    
    def clear_order(self):
        """Clear all orders and reset the display"""
        # Clear seat orders
        for seat in self.seat_orders:
            self.seat_orders[seat] = {}
        
        # Clear order display
        for widget in self.order_frame.winfo_children():
            widget.destroy()
        
        # Reset total
        self.order_cost_total = 0
        
        print("Order cleared and ready for new order")

    def get_recipe(self):
        print('Get recipe')

    def get_quantity(self):
        print('Get quantity')

    def repeat(self):
        """Repeat highlighted items"""
        for label in self.highlighted_labels:
            duplicate_label = Label(self.order_frame, text=label.cget('text'), 
                                  fg="blue", cursor="hand2")
            duplicate_label.bind("<Button-1>", self.if_clicked)
            
            duplicate_label.grid(row=self.current_row, column=self.current_column, 
                               padx=10, pady=5)
            
            self.current_row += 1
            if self.current_row >= self.max_rows:
                self.current_row = 0
                self.current_column += 1

    def modify(self):
        pass

    def delete(self):
        """Delete highlighted items"""
        for label in self.highlighted_labels.copy():
            label.destroy()
        self.highlighted_labels.clear()

    def rapid_fire(self):
        print('Rapid fire')

    def close(self):
        print('close')

    def next_seat(self):
        """Move to next seat"""
        if self.current_seat == 'table':
            self.current_seat = 'seat1'
        elif self.current_seat == 'seat20':
            pass
        else:
            self.current_seat = 'seat' + str(int(self.current_seat[-1]) + 1)

    def run(self):
        """Start the application"""
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    pos_system = POSSystem()
    pos_system.run()
    pos_system.run()