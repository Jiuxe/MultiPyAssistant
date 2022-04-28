from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import cv2
import encriptador

root = Tk()
root.title("Encrypt Image")

array_img = []

def encrypt_img():

    try:
        import_filename = fd.askopenfile()
        imagen = cv2.imread(import_filename.name, 0)

        tam_x = 10
        tam_y = 10

        grillEncrypt = encriptador.getGrillEncryptor(tam_x, tam_y)

        print(grillEncrypt)

        apply_encrypt(imagen, grillEncrypt)

        cv2.imshow('', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        mb.showerror("Error", "Problema al realizar encriptacion")
        return


def apply_encrypt(img, grill):
    pass


button1 = Button(root, text="Encriptar imagen", width=20,
                  height=5, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=encrypt_img)

button1.place(x=155, y=60)

root.geometry("500x300")
root.mainloop()