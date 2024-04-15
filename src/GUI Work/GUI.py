from tkinter import *
from PIL import ImageTk, Image
import customtkinter

# Create CTk window
root = customtkinter.CTk()
# Set window width / height
root.geometry("500x400")
root.minsize(300, 400)

# Load image
img = ImageTk.PhotoImage(Image.open("Resources/TestImage.jpeg"))
# Create canvas to display the image
canvas = customtkinter.CTkCanvas(root, width=300, height=300)
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.place(relx=0.5, rely=0.3, anchor=CENTER)

# Use CTk button instead of tkinter button
button = customtkinter.CTkButton(master=root, text="Hello World!")
# Showing at the center of the screen
button.place(relx=0.5, rely=0.7, anchor=CENTER)

# Running the app
root.mainloop()
