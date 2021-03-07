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
                                        font="Arial 16 bold", bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)
        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # export Button (row 1)
        self.export_button = Button(self.converter_frame, text="export",
                                    font=("arial", "14"),
                                    padx=10, pady=10,
                                    command=lambda: self.export(self.all_calc_list))
        self.export_button.grid(row=1, pady=10)

    def export(self, calc_export):
        export(self, calc_export)



class Export:
    def __init__(self, partner, calc_export):

        background ="light blue"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel ()

        # if user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        # Set up Gui Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set Up export heading (row 0)
        self.how_heading = Label(self.export_frame,
                                 text=" Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame,text="Enter a filename "
                                                        "in the box below "
                                                        "and press the save "
                                                        " button to save your "
                                                        " calculation history"
                                                        "to a text file.",

                              justify=LEFT, width=40,
                                bg=background, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label).. (row 2)
        self.export_text= Label(self.export_frame, text="If the filename "
                                                        "you enter below "
                                                        "already exists "
                                                        "its contents will "
                                                        "be replaced with "
                                                        "your calculation"
                                                        "history",
                                justify=LEFT, bg="#ffafaf", fg="maroon",
                                  font="Arial 10 italic", wrap=225, padx=10,
                                  pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename entry box (row 3)
        self.filename_entry = Label(self.export_frame, width=20,
                                 font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Save / Cancel frame (row 4)
        self.export_cancel_frame = Frame(self.export_frame)
        self.export_cancel_frame.grid(row=3, pady=10)

        # Save and Cancel Buttons (row 0 of the save_cancel_Frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold", command=partial(self.close_export))
        self.dismiss_button.grid(row=0, column=1)


    def close_export(self, partner) :
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter()
    root.mainloop()

