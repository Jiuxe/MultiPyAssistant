from logging import exception
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from PIL import Image
import cv2
import numpy as np
import encriptador

#Para ver el progreso de encriptacion
from tqdm import tqdm

root = Tk()
root.title("Encrypt Image")

def write_matrix(matrix):
    matrix_array = '['
    for i in range(len(matrix)):
        matrix_array += '['
        for j in range(len(matrix[0])):
            matrix_array += str(matrix[i][j]) + " "
        matrix_array += ']'
    matrix_array += ']'

    return matrix_array

def read_file(name):
    with open(name, 'r') as f:
        epocs = int(f.readline())
        tam_x = int(f.readline())
        tam_y = int(f.readline())
        key, init = read_matrix(f.readline())
        key = key[0]
        imagen, init = read_matrix(f.readline())
        imagen = imagen[0]

    return imagen, key

def read_matrix(matrix_string, init=0):
    matrix = []
    index = init
    while index < len(matrix_string):
        if matrix_string[index] == '[':
            array, index = read_matrix(matrix_string, index+1)
            matrix.append(array)
        elif matrix_string[index] == ']':
            init = index
            break
        elif matrix_string[index] != ' ' and matrix_string[index] != '.' and matrix_string[index] != '\n':
            number = ""
            while matrix_string[index] != ' ' and matrix_string[index] != '.' and matrix_string[index] != '\n' and matrix_string[index] != ']':
                number += matrix_string[index]
                index += 1
            matrix.append(int(number))
            if matrix_string[index+1] == '.':
                index += 2
            if matrix_string[index] == ']':
                index -= 1
        index += 1
    return matrix, init

def encrypt_img():

    try:
        import_filename = fd.askopenfile()
        imagen = cv2.imread(import_filename.name)

        img_save = open("imagen_LGR.lgr", 'w')

        tam_x = 10
        tam_y = 10

        grillEncrypt, inital_key = encriptador.getGrillEncryptor(tam_x, tam_y)
        apply_encrypt(imagen, grillEncrypt)

        img_save.write(str(inital_key.get('epocs')) + '\n')
        img_save.write(str(inital_key.get('tam_x')) + '\n')
        img_save.write(str(inital_key.get('tam_y')) + '\n')

        img_save.write(write_matrix(inital_key.get('key')) + '\n')

        img_save.write(write_matrix(imagen) + '\n')

        # imagen_des = np.copy(imagen)

        # grillDecrypt = encriptador.getGrillDecryptor(inital_key)
        # apply_decrypt(imagen_des, grillDecrypt)

        #result_image = np.concatenate((imagen, imagen_des), axis=1)

        # cv2.imshow('', result_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


    except exception as e:
        mb.showerror("Error", "Problema al realizar encriptacion" + e)
        return

def decrypt_img():

    try:
        import_filename = fd.askopenfile()
        imagen, key = read_file(import_filename.name)
        imagen = np.array(imagen).astype(np.uint8)

        cv2.imshow('', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # print(key)
        # print(imagen)

    except exception as e:
        mb.showerror("Error", "Problema al realizar desencriptacion" + e)
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
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=encrypt_img)

button1.place(x=155, y=60)

button2 = Button(root, text="Desencriptar imagen", width=20,
                  height=2, bg="lightblue", fg="black",
                  font=("Helvetica", 12, "bold"),
                  command=decrypt_img)

button2.place(x=155, y=200)

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

