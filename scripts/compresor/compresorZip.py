import os
import tkinter as tk
from tkinter import *
import zipfile
from tkinter import filedialog, messagebox


def createWidgets():
    # Descompresion
    unzipArchLabel = Label(window, text="Archivo a descomprimir: ", bg="steelblue", font=('',10, 'bold'))
    unzipArchLabel.grid(row=0, column=0, padx=5, pady=5)

    window.unzipEntry = Text(window, height=4, width=45, font=('Arial', 10))
    window.unzipEntry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

    unzipButton = Button(window, command=unzipNavigate, text="Navegar", width=20, height=2)
    unzipButton.grid(row=0, column=3, padx=5, pady=5)

    unzipArchNameLabel = Label(window, text="Nombre del archivo: ", bg="steelblue", font=('', 10, 'bold'))
    unzipArchNameLabel.grid(row=1, column=0, padx=5, pady=5)

    window.unzipNameEntry = Entry(window, width=45, font=('Arial', 10))
    window.unzipNameEntry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

    unzipButton = Button(window, command=unzipArch, text="Descomprimir", width=20)
    unzipButton.grid(row=1, column=3, padx=5, pady=5)

    # Compresion

    zipArchLabel = Label(window, text="Archivo a comprimir: ", bg="steelblue", font=('', 10, 'bold'))
    zipArchLabel.grid(row=2, column=0, padx=5, pady=5)

    window.zipEntry = Text(window, height=4, width=45, font=('Arial', 10))
    window.zipEntry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

    zipButton = Button(window, command=zipNavigate, text="Navegar", width=20, height=2)
    zipButton.grid(row=2, column=3, padx=5, pady=5)

    zipArchNameLabel = Label(window, text="Nombre del archivo: ", bg="steelblue", font=('', 10, 'bold'))
    zipArchNameLabel.grid(row=3, column=0, padx=5, pady=5)

    window.zipNameEntry = Entry(window, width=45, font=('Arial', 10))
    window.zipNameEntry.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    zipButton = Button(window, command=zipArch, text="Comprimir", width=20)
    zipButton.grid(row=3, column=3, padx=5, pady=5)


def unzipNavigate():

    window.fileList = filedialog.askopenfilename(initialdir = "C:\\Users\\Jiuxe\\Pictures\\Avatares")
    window.unzipEntry.insert("1.0", "Archivos a descomprimir:\n")

    window.files = os.path.basename(window.fileList)
    window.unzipEntry.insert("2.0", window.files + "\n")

    window.unzipEntry.config(state=DISABLED)

def unzipArch():

    #try:

    dirName = filedialog.askdirectory()
    os.makedirs(dirName+"\\"+window.unzipNameEntry.get())

    # Abrimos y extraemos el archivo
    with zipfile.ZipFile(window.fileList, 'r') as zip:
        zipFile = zipfile.ZipFile(window.fileList)
        zipFile.extractall(dirName+"\\"+window.unzipNameEntry.get())

    messagebox.showinfo("Descomprimir", "Archivo descomprimido con éxito")

    #except:
    #    messagebox.showerror("Descomprimir", "Error al descomprimir")


def zipNavigate():
    window.fileList = filedialog.askopenfilename(initialdir="C:\\Users\\Jiuxe\\Pictures\\Avatares")
    window.zipEntry.insert("1.0", "Archivos a comprimir:\n")

    window.files = os.path.basename(window.fileList)
    window.zipEntry.insert("2.0", window.files + "\n")

    window.zipEntry.config(state=DISABLED)

def zipArch():
    try:

        fileZip = zipfile.ZipFile(window.fileList + ".zip", 'w')

        fileZip.write(window.fileList, window.zipNameEntry.get(), compress_type=zipfile.ZIP_DEFLATED)
        fileZip.close()
        messagebox.showinfo("Comprimir", "Archivo comprimido con éxito")

    except:
        messagebox.showerror("Comprimir", "Error al comprimir")


window = tk.Tk()
window.title("ZipCompresor")
window.config(bg="steelblue")

createWidgets()

window.mainloop()