from logging import exception
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import cv2
import numpy as np
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

        grillEncrypt, inital_key = encriptador.getGrillEncryptor(tam_x, tam_y)

        apply_encrypt(imagen, grillEncrypt)

        imagen_des = np.copy(imagen)

        grillDecrypt = encriptador.getGrillDecryptor(inital_key)
        apply_decrypt(imagen_des, grillDecrypt)

        result_image = np.concatenate((imagen, imagen_des), axis=1)

        cv2.imshow('', result_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except exception as e:
        mb.showerror("Error", "Problema al realizar encriptacion" + e)
        return


def apply_encrypt(img, grill):

    img_size_x = len(img[0])
    img_size_y = len(img)

    for i in tqdm(range(img_size_y)):
        for j in range(img_size_x):
            for i_grill in range(len(grill)):
                for j_grill in range(len(grill[0])):
                   if (i != (i + i_grill) % img_size_y and j != (j + j_grill) % img_size_x):
                    img[i][j][0] = img[i][j][0] + img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][0] * grill[i_grill][j_grill]
                    img[i][j][1] = img[i][j][1] + img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][1] * grill[i_grill][j_grill]
                    img[i][j][2] = img[i][j][2] + img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][2] * grill[i_grill][j_grill]
                    # img[i][j] = img[i][j] + img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x] * grill[i_grill][j_grill]

            img[i][j][0] = img[i][j][0] % 256
            img[i][j][1] = img[i][j][1] % 256
            img[i][j][2] = img[i][j][2] % 256

def apply_decrypt(img, grill):

    img_size_x = len(img[0])
    img_size_y = len(img)

    for i in tqdm(range(img_size_y-1, -1, -1)):
        for j in range(img_size_x-1, -1, -1):
            for i_grill in range(len(grill)-1, -1, -1):
                for j_grill in range(len(grill[0])-1, -1, -1):
                   if(i != (i+i_grill)%img_size_y and j != (j+j_grill)%img_size_x):
                    img[i][j][0] = img[i][j][0] - img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][0] * grill[i_grill][j_grill]
                    img[i][j][1] = img[i][j][1] - img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][1] * grill[i_grill][j_grill]
                    img[i][j][2] = img[i][j][2] - img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x][2] * grill[i_grill][j_grill]
                    #img[i][j] =  img[i][j] - img[(i+i_grill)%img_size_y][(j+j_grill)%img_size_x] * grill[i_grill][j_grill]
            img[i][j][0] = img[i][j][0] % 256
            img[i][j][1] = img[i][j][1] % 256
            img[i][j][2] = img[i][j][2] % 256


button1 = Button(root, text="Encriptar imagen", width=20,
                  height=5, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=encrypt_img)

button1.place(x=155, y=60)

root.geometry("500x300")
root.mainloop()

"""""
matriz_basica = [[[1,255,1],[2,225,2],[3,3,3]]
                ,[[4,4,4],[5,25,5],[6,6,255]]
                ,[[7,7,7],[8,25,28],[39,9,49]]]

grill_basic = [[1,5,1],
               [2,6,2],
               [1,3,1]]
print("Antes de encriptar: " , matriz_basica)
apply_encrypt(matriz_basica, grill_basic)
print("Despues de encriptar:", matriz_basica)

apply_desencrypt(matriz_basica, grill_basic)
print("Despues de desencriptar:", matriz_basica)
"""""

