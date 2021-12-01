# Creating GUIs with Tkinter

import tkinter as tk


# creates the tkinter window
window = tk.Tk()
window.title("This is a gui")
# sets the minimum size for the window unless the user resizes it OR there's more content
window.minsize(width=600, height=500)
# Add padding around the edges of the screen
window.config(padx=20, pady=20)

# Creating a Label, text is used for the name, font etc
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
# pack is needed to place the label
# my_label.pack()
# You can also reassign the label after creation
my_label["text"] = "This is a new line"
# or
my_label.config(text="This is a new line")

# Quick function to alter text to use with the button
# def button_clicked():
#     my_label["text"] = "The button was clicked!"
#     button["text"] = "The button was clicked!"

# Challenge have the text input update the label when the button is clicked
def button_clicked():
    my_label.config(text=input.get())


# Creating a button to click on, command will run a function

button = tk.Button(text="Woof", command=button_clicked)
# button.pack()

# Pack is still needed to place the button, TK places them in order so it'll be the Label, then the button

# Entry box or Input box and setting the width
# You cannot assign an input like with pythons own input("Whatever") instead you have to use a GET method.
input = tk.Entry(width=25)
# input.pack()

# TKinter has three different ways of laying out widgets using layout managers
# *Pack* will place them from the top then any else below the previous one. You can add a side from top,left,right,bottom.
# As Doesn't have a precise way of laying them out

# *Place* will place them at x,y such as below

my_placed_label = tk.Label(text="Place label")
my_placed_label.place(x=100, y=200)

# *Grid* allows you to divide the screen space into rows and columns relative to another widget, however you cannot mix it with pack

my_grid_label = tk.Label(text="Grid label with MANY spaces to space grids")
my_grid_label.grid(column=0, row=0)
#pads around the widget
my_grid_label.config(padx=50, pady=50)

my_grid_button = tk.Button(text="Grid Button")
my_grid_button.grid(column=1, row=1)


# keeps the window running and needs to be at the end
window.mainloop()
