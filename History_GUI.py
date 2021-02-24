import ...




class Converter:
    def __init__(self):

        # Formatting Variables
        background_color = "lightblue"

        # Initalise list to hold calculations history
        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter heading (row 0)
        self.temp_heading_label = label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 19 bold", bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

