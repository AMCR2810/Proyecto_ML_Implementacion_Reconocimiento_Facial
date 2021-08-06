import cv2
import os
import numpy
import pymysql
import time
from datetime import datetime


dataPath = 'C:/Users/esteb/Desktop/Reconocimiento_facial/Data' #Ruta de los datos
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)
contador=0
id_encontrada=0



face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo

face_recognizer.read('modeloLBPHFace.xml')

#Webcam o video
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('alvaro.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
	ret,frame = cap.read()
	if ret == False: break
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	auxFrame = gray.copy()

	faces = faceClassif.detectMultiScale(gray,1.3,5)

	for (x,y,w,h) in faces:
		rostro = auxFrame[y:y+h,x:x+w]
		rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
		result = face_recognizer.predict(rostro)

		cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
		
		# LBPHFace
		if result[1] < 70:
			## AQUI ENVIAMOS EL NUMERO DE LA PERSONA IDENTIFICADA
			cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
			
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
			contador+=1
			if contador==15:
				db = pymysql.connect(host = 'localhost',
                 					user ='root',
                  					password = '', 
                       				db= 'ml_info_personas',
                     	     		charset='utf8mb4')
				cursor = db.cursor()
				
				# Esta query busca la id de la imagen
				sql = "SELECT id FROM personas \
				WHERE imagen = {}".format(imagePaths[result[0]])
					
				cursor.execute(sql)

				# Fetch all the rows in a list of lists.
				results = cursor.fetchall()
				for row in results:
				   id = row[0]
				
				sql = "SELECT id FROM personas_identificadas \
				WHERE id = {}".format(id)
				cursor.execute(sql)
				results = cursor.fetchall()
				print(len(results))
				
				now = datetime.now()
				hora = datetime.now()
				hora = hora.strftime('%H:%M:%S')
				
				
				
				if len(results)==0:
					now = datetime.now() 
					sql = "INSERT INTO  personas_identificadas (id, fecha, hora, lugar) VALUES ('{}', '{}', '{}', '{}')".format(id, now, hora, "local")
					cursor.execute(sql)
					db.commit()
					print('se insertaron datos')
				else:
					sql = "UPDATE personas_identificadas SET fecha='{}', hora='{}', lugar='{}' WHERE id='{}'".format(now, hora, "local 22", id)
					cursor.execute(sql)
					db.commit()
				# desconecta del servidor
				db.close()	
					
				#print(imagePaths[result[0]])
				
		else:
			cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
			cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
			contador=0
		
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()

#CON ESTO RESETEAMOS EL AUTO INCREMENTO DE LA TABLA
#ALTER TABLE personas_identificadas AUTO_INCREMENT = 1
