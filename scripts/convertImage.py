from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
from PIL import Image


root = Tk()
root.title("Convert Image")

array_img = []

def jpg_to_gif():

    try:
        export_filename = fd.asksaveasfilename(defaultextension=".gif")
        array_img[0].save(export_filename, save_all=True, append_images=array_img[1:], loop=0, duration=100, transparency=0)
        mb.showinfo("Convert Image", "Image converted to gif")
    except:
        mb.showerror("Convert Image", "Please select a png or jpg file")
    array_img.clear()
    button1.config(state=DISABLED)
    count_img.config(text=str(len(array_img)))

def add_img():
    # Añadimos imagen al array para crear el gif
    import_filename = fd.askopenfile()
    array_img.append(Image.open(import_filename.name))
    button1.config(state=NORMAL)
    count_img.config(text=str(len(array_img)))


button1 = Button(root, text="JPG to GIF", width=20,
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=jpg_to_gif, state=DISABLED)

button1.place(x=155, y=60)

button2 = Button(root, text="Add more image", width=20,
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=add_img)

count_img = Label(root, text="0", width=10, height=1, bg="lightgreen", fg="black", font=("Helvetica", 12, "bold"))

button2.place(x=155, y=160)
count_img.place(x=200, y=215)

root.geometry("500x300")
root.mainloop()