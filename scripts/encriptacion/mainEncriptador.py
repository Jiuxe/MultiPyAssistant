from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import cv2
import encriptador

#Para ver el progreso de encriptacion
from tqdm import tqdm

root = Tk()
root.title("Encrypt Image")

array_img = []

def encrypt_img():

    try:
        import_filename = fd.askopenfile()
        imagen = cv2.imread(import_filename.name)

        tam_x = 10
        tam_y = 10

        grillEncrypt = encriptador.getGrillEncryptor(tam_x, tam_y)

        apply_encrypt(imagen, grillEncrypt)

        cv2.imshow('', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        mb.showerror("Error", "Problema al realizar encriptacion")
        return


def apply_encrypt(img, grill):

    center_grill_x = len(grill[0]) // 2
    center_grill_y = len(grill) // 2

    img_size_x = len(img[0])
    img_size_y = len(img)

    for i in tqdm(range(img_size_y)):
        for j in range(img_size_x):
            for i_grill in range(len(grill)):
                for j_grill in range(len(grill[0])):
                   img[i][j][0] += img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][0] * grill[i_grill][j_grill]
                   img[i][j][1] += img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][1] * grill[i_grill][j_grill]
                   img[i][j][2] += img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][2] * grill[i_grill][j_grill]



button1 = Button(root, text="Encriptar imagen", width=20,
                  height=5, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=encrypt_img)

button1.place(x=155, y=60)

root.geometry("500x300")
root.mainloop()