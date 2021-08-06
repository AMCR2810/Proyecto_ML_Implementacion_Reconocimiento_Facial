import os
import shutil





i=1
while i<30000:
   digitos=0
   i2 = i
  
   while i2>0:
        i2//=10
        digitos+=1
        
   if digitos == 1:
       input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
       files_name = os.listdir(input_images_path)
       
       nombre_carpeta = "00000"+str(i)
       comparacion=str(nombre_carpeta)+".jpg"
       destino="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2/"+nombre_carpeta
       os.makedirs(destino)
       
       for files_name in files_name:
        if files_name == comparacion:
            
            origen="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            shutil.move(origen + "/"+files_name, destino)
            ##input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            ##files_name = os.listdir(input_images_path)

   if digitos == 2:    
       input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
       files_name = os.listdir(input_images_path)
       nombre_carpeta = "0000"+str(i)
       comparacion=str(nombre_carpeta)+".jpg"
       destino="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2/"+nombre_carpeta
       os.makedirs(destino)
       
       for files_name in files_name:
        if files_name == comparacion:
            origen="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            shutil.move(origen + "/"+files_name, destino)
            input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            files_name = os.listdir(input_images_path)

   if digitos == 3:    
       input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
       files_name = os.listdir(input_images_path)
       nombre_carpeta = "000"+str(i)
       comparacion=str(nombre_carpeta)+".jpg"
       destino="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2/"+nombre_carpeta
       os.makedirs(destino)
       
       for files_name in files_name:
        if files_name == comparacion:
            origen="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            shutil.move(origen + "/"+files_name, destino)
            input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            files_name = os.listdir(input_images_path)

   if digitos == 4:     
       input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
       files_name = os.listdir(input_images_path)
       nombre_carpeta = "00"+str(i)
       comparacion=str(nombre_carpeta)+".jpg"
       destino="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2/"+nombre_carpeta
       os.makedirs(destino)
       
       for files_name in files_name:
        if files_name == comparacion:
            origen="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            shutil.move(origen + "/"+files_name, destino)
            input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            files_name = os.listdir(input_images_path)

   if digitos == 5:      
       input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
       files_name = os.listdir(input_images_path)
       nombre_carpeta = "0"+str(i)
       comparacion=str(nombre_carpeta)+".jpg"
       destino="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2/"+nombre_carpeta
       os.makedirs(destino)
       
       for files_name in files_name:
        if files_name == comparacion:
            origen="C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            shutil.move(origen + "/"+files_name, destino)
            input_images_path = "C:/Users/esteb/Desktop/Reconocimiento_facial/Data2"
            files_name = os.listdir(input_images_path)

   i+=1 
   



   
