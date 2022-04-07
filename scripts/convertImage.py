from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
from PIL import Image


root = Tk()
root.title("Convert Image")

def jpg_to_gif():
    global img

    try:
        img = []

        # Hacer bucle para añadir mas imagenes
        import_filename = fd.askopenfile()
        img.append(Image.open(import_filename.name))

        export_filename = fd.asksaveasfilename(defaultextension=".gif")
        img[0].save(export_filename, save_all=True, append_images=img[1:], loop=0, duration=100, transparency=0)
        mb.showinfo("Convert Image", "Image converted to gif")
    except:
        mb.showerror("Convert Image", "Please select a png or jpg file")

def gif_to_jpg():
    return "jpg"

button1 = Button(root, text="JPG to GIF", width=20,
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=jpg_to_gif)

button1.place(x=155, y=60)

button2 = Button(root, text="Add more image", width=20,
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=jpg_to_gif, state=DISABLED)

button2.place(x=155, y=160)

root.geometry("500x300")
root.mainloop()