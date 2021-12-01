# Project - Create a miles to KM converter using TKinter to write the UI
import tkinter as tk


# creates the tkinter window
window = tk.Tk()
window.title("KM <> Miles converter")
# sets the minimum size for the window unless the user resizes it OR there's more content
window.minsize(width=250, height=150)
# Add padding around the edges of the screen
window.config(padx=50, pady=50)


text_box = tk.Entry(justify="center")
text_box.insert(-1, string="0")
text_box.config(width=10)
text_box.grid(row=1, column=1)


def what_now():
    if radio_state.get() == 0:
        mile_or_km.config(text="Km")
    elif radio_state.get() == 1:
        mile_or_km.config(text="miles")


# Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Km", value=1, variable=radio_state, command=what_now)
radiobutton2 = tk.Radiobutton(text="Miles", value=0, variable=radio_state, command=what_now)
radiobutton1.grid(row=0, column=0)
radiobutton2.grid(row=1, column=0)


def convert_to():
    print(radio_state)
    value = 0
    if radio_state.get() == 0:
        value = float(text_box.get()) * 1.609
        result_label.config(text=round(value, 2))
    elif radio_state.get() == 1:
        value = float(text_box.get()) / 1.609
        result_label.config(text=round(value, 2))


is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=2, column=0)
result_label = tk.Label(text="0")
result_label.grid(row=2, column=1)
mile_or_km = tk.Label(text="km")
mile_or_km.grid(row=2, column=2)


calculate_button = tk.Button(text="Calculate", command=convert_to)
calculate_button.grid(
    row=3,
    column=1,
)


# TK mainloop will exit if not at the bottom
window.mainloop()
