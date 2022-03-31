from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def calculate_score():
    miles = float(text_input.get())
    km_converted = round(miles * 1.609, 2)
    km_value_label.config(text=f"{km_converted}")


# Entry

text_input = Entry(width=10)
text_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles").grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to").grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km").grid(column=2, row=1)

# Button
Button(text="Calculate", command=calculate_score).grid(column=1, row=2)


window.mainloop()