@@ -5,6 +5,7 @@ import random

class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "light blue"

@ -26,10 +27,12 @@ class Converter:
                                            text="Type in the amount to be "
                                                 "converted and then push "
                                                 "one of the buttons below...",
                                            font="Arial 10 italic", wrap=250,
                                            font="Arial 10 italic", wrap=290,
                                            justify=LEFT, bg=background_color,
                                            padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)
@ -72,20 +75,60 @@ class Converter:
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, to):
        print(to)
    def temp_convert(self, low):
        print(low)
        print("in function")

        error = "#ffafaf"  # pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()
        print(to_convert)

        try:
            to_convert = float(to_convert)
            print("yay")
            has_errors = "no"

            # Check and convert to Farhrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)
                print(answer)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees is C is {} degrees F".format(to_convert, celsius)

            else:
                # Input is invalid (too cold) !!
                answer = "too cold!"
                has_errors = "yes"

            # Display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg='blue')
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)
            # Add Answer to list for history

        except ValueError:
            print("oops")
            self.converted_label.configure(text="Enter a Number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded


# main routine