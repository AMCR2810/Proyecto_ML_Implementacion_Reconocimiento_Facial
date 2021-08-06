import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
from PIL import Image
from functools import partial
import imutils
import numpy as np
import pymysql
import cv2
import os
import imutils



pag=2

raiz=tk.Tk()
raiz.title("PERSONAS IDENTIFICADAS")
raiz.resizable(True, True)

#raiz.geometry("1920x1080")
raiz.config(bg="black")


def con():
    db = pymysql.connect(host = 'localhost',
                         user ='root',
                          password = '', 
                           db= 'ml_info_personas',
                          charset='utf8mb4')
    
    return db





# 
db = con()
cursor= db.cursor()
sql = "SELECT max(numero) FROM personas_identificadas"
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
    total=row[0]
db.close()
    

miFrame=Frame()
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="gray")
miFrame.config(width="1024", height="768")


def mostrar(lugar,id,fecha,hora,numero,nombre,apellidos,run,causa,imagen,total,resultado):
    
    nombre= Label(miFrame, text="Nombre: {}".format(nombre))
    nombre.config(bg="orange")
    nombre.place(x=512,y=100, width=450, height=50)
    
    apellidos= Label(miFrame, text="Apellidos: {}".format(apellidos))
    apellidos.config(bg="orange")
    apellidos.place(x=512,y=170, width=450, height=50)
    
    run= Label(miFrame, text="RUN: {}".format(run))
    run.config(bg="orange")
    run.place(x=512,y=240, width=450, height=50)
    
    causa= Label(miFrame, text="Causa: {}".format(causa))
    causa.config(bg="orange")
    causa.place(x=512,y=310, width=450, height=50)
    
    fecha= Label(miFrame, text="Fecha y hora: {}, {}".format(fecha, hora))
    fecha.config(bg="orange")
    fecha.place(x=512,y=380, width=450, height=50)
    
    lugar= Label(miFrame, text="Lugar: {}".format(lugar))
    lugar.config(bg="orange")
    lugar.place(x=512,y=450, width=450, height=50)

    
    numpersonas= Label(miFrame, text="PERSONAS {}/{}".format(resultado,total))
    numpersonas.config(bg="orange")
    numpersonas.place(x=420,y=650, width=130, height=50)
  
  
    lblimagen = Label(miFrame)
    lblimagen.place(x=100,y=100, width=400, height=400)
    
    imagenCom ="C:/Users/esteb/Desktop/Reconocimiento_facial/Data/{}/rostro_0.jpg".format(imagen)
    #C:\Users\esteb\Desktop\Reconocimiento_facial\Data\000001

    image = cv2.imread(imagenCom)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY,1)
    image = imutils.resize(image, height=150)
    
    imageToShow = imutils.resize(image, width=150)
    im = Image.fromarray(imageToShow)
    img = ImageTk.PhotoImage(image=im)
    
    lblimagen.configure(image=img)
    lblimagen.image = img


def consulta(x):
    
    global pag
    global total
    resultado=pag
    if x>0:
        resultado=resultado+1
    else:
        resultado=resultado-1
    if resultado<=total and resultado>0:
        pag=resultado
        con()
        db = con()
        cursor= db.cursor()
        sql = "SELECT pi.lugar, pi.id, pi.fecha, pi.hora, pi.numero, p.id, p.nombre, p.apellidos, p.run, p.causa, p.imagen FROM personas_identificadas pi, personas p WHERE pi.numero={} AND pi.id=p.id".format(resultado)
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        for row in results:
            lugar = row[0]
            id = row[1]
            fecha = row[2]
            hora = row[3]
            numero = row[4]
            nombre = row[6]
            apellidos = row[7]
            run = row[8]
            causa = row[9]
            imagen = row[10]
        db.close()
        return mostrar(lugar,id,fecha,hora,numero,nombre,apellidos,run,causa,imagen,total,resultado)
    else:
        resultado=pag
        
        
def suma():
    a=1
    return consulta(a)
    
def resta():
    a=-1
    return consulta(a)
# desconecta del servidor

consulta(0)




boton1= Button(miFrame, text="Anterior",command=resta)
boton1.config(bg="white")
boton1.place(x=310,y=660, width=100, height=30)

boton2= Button(miFrame, text="Siguiente",command=suma)
boton2.config(bg="white")
boton2.place(x=560,y=660, width=100, height=30)

 
raiz.mainloop()

