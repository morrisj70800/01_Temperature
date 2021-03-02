import  ...

from tkinter import *
from functools import partial   # To prevent unwanted windows


class Converter:
    def __init__(self):

        # Formatting Variables
        background_color = "light blue"

        # In actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F',
                              '24 degrees C is 75.2 degrees F',
                              '100 degrees C is 37.8 degrees F']

        #  Converter Main Screen GUI...
        self.all_calculations = []
        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 19 bold", bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)
        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                  font=("arial", "14"),
                                  padx=10, pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1, pady=10)

    def history(self):
        get_history = History(self)



class History:
    def __init__(self, partner):

        background ="light blue"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel ()

        # if user press cross at top, closes history and 'releases' history button
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))
        # Set up Gui Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set Up history heading (row 0)
        self.how_heading = Label(self.history_frame, text=" history / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are you most recent "
                                       "calculations. Please use the "
                                       "export button to create a text "
                                       " file of all your calculations for "
                                       " this session", wrap=250,
                                  font="arial 10 italic",
                                  justify=LEFT, width=40, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        # History Output goes here.. (row 2)

        # Generate string from list of calculations...
        history_string = ""

        if len(calc_history) >= 7:
            for item in range(0, 7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        # label to display calculation history to user

        # Export / Dismiss Buttons Frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Buttons
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_history))
        self.dismiss_button.grid(row=0, column=1)


    def close_history(self, partner) :
        # Put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()

