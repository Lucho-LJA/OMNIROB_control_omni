#!/usr/bin/env python3

from lib_omni.lector_node_red_config import *
import os

captura1 = cv2.VideoCapture(2)
display_window=False
def getImg():
	global display_window
	global captura1
	(_,img)=captura1.read()
	#img=cv2.resize(img,(size[0],size[1]))
	if display_window:
		cv2.imshow('IMG',img)
	return img



if __name__ == '__main__':
	try:
			
		bridge = CvBridge()
		global cam1
		while not rospy.is_shutdown():
			imagen1=getImg()
			ret, jpeg = cv2.imencode('.jpg', imagen1)
			jpg_as_text = base64.b64encode(jpeg)
			#cv2.imwrite(os.path.join('vomni.jpg'), imagen1)
			#print('oasa1')
			aux=str(jpg_as_text)
			aux="data:image/jpeg;base64,"+aux[2:len(aux)-1]
			cam1.data=aux
			
			#cv2.imshow('Taller OpenCV - Imagen',imagen1)
			#print('pasa')
			publicar_nodered(cam1)
			publicar_omni()
			#break

			rate.sleep()
			if display_window and (cv2.waitKey(1) & 0xFF==27):
				break
		
        #Terminate conextion
		captura1.release()
		#Close all open windows
		cv2.destroyAllWindows()

	except Exception as e:#rospy.ROSInterruptException:
		print(e)
		#Terminate conextion
		captura1.release()
		#Close all open windows
		cv2.destroyAllWindows()
		pass
