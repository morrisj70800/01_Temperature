from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=600, height=300,
                                     bg=background_color,
                                     pady=10)

        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # Export Button (row 1)
        self.export_button = Button(self.converter_frame, text="Export",
                                    font=("arial", "14"),
                                    padx=10, pady=10, command=self.export)
        self.export_button.grid(row=1, pady=10)

    def export(self):
        get_export = Export(self)


class Export:
    def __init__(self, partner):

        background ="light blue"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel ()

        # if user press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))
        # Set up Gui Frame
        self.export_frame = Frame(self.export_box, bg=background)
        self.export_frame.grid()

        # Set Up export heading (row 0)
        self.how_heading = Label(self.export_frame, text=" Export / Instructions",
                                 font="arial 10 bold", bg=background)
        self.how_heading.grid(row=0)

        # export instructions (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a file name "
                                                         "in the box below "
                                                         "and press the save "
                                                         " button to save your "
                                                         " calculation history"
                                                         "to a text file.",

                             justify=LEFT, width=40,
                                 bg=background, wrap=250)

        self.export_text.grid(row=2, pady=10)

        # Warning text(row 2)
        self.export_text = Label(self.export_frame, text="if the filename "
                                                         "you enter below "
                                                         "already exists "
                                                         "its contents will "
                                                         "be replaced with "
                                                         "your calculation "
                                                         "history",
                                 justify=LEFT, width=40, bg="#ffafaf", fg="maroon",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)

        # Generate string from list of calculations...
        export_string = ""

        if len(calc_export) >= 7:
            for item in range(0, 7):
                export_string += calc_export[len(calc_export)
                                               - item - 1]+"\n"

        else:
            for item in calc_export:
                export_string += calc_export[len(calc_export) -
                                               calc_export.index(item) - 1] + "\n"
                self.export_text.config(text="Here is your calculation "
                                             "export. You can use the "
                                             "export button to save this "
                                             "data to a text file if "
                                             "desired.")

        # Filename Entry Box (row 3)
        self.filename_entry = Label(self.export_frame, text=export_string,
                                bg=background,font="arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row= 2)

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Self",
                                  font="arial 12 bold")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                     font="Arial 12 bold", command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)


    def close_export(self, partner) :
        # Put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()