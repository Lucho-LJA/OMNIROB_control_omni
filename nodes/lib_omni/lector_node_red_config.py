import rospy
import time
from std_msgs.msg import Int16
from std_msgs.msg import Float32
from std_msgs.msg import Char
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8
from std_msgs.msg import String
from sensor_msgs.msg import Image
import base64
#Librery numpy
import numpy as np
#Library OpenCVvideo_msg=String()

import cv2
from cv_bridge import CvBridge, CvBridgeError

##SUBSCRIPTOR VARIABLES
#OMNI NUMBER - NODERED-TRADUCTOR
omni_n=Int8()
omni_n.data=1

#OMNI MOVE - NODERED-OMNI
movimiento_net=Char()
movimiento_net.data=75

#OMNI VELOCITY - NODERED-OMNI
vel_net=Float32MultiArray()
vel_net.data=[0,0,0,0]










###PUBLISH FUNCTIONS
##ENVIROMENT CAMERA BROKER-NODERED
cam1=String()
cam1.data=" "

#OMNI POSITION - BROKER-NODERED 
pos_net=Float32MultiArray()
pos_net.data=[0,0,0,0,0,0]


#ACTION WEB MESSAGE BROKER-NODERED /  CONDITIONAL BROKER-LECTOR
active_net=Int8()
active_net.data=1

#VELOCITY OF OMNIS LECTOR-NODERED
rpm_net=Float32MultiArray()
rpm_net.data=[0,0,0]


##OPTION MOVE OMNI LECTOR-OMNI
_opc_omni_=Int8()
_opc_omni_.data=0

##OPTION MOVE OMNI AUX LECTOR-OMNI
movimiento_net_aux=Char()
movimiento_net_aux.data=75



##SUBSCRIBER FUNCTION
#OF NODERED
def Omni_opc(data):
	global omni_n
	omni_n.data=data.data

def Movimiento_omni(data):
	global movimiento_net
	movimiento_net.data=data.data

def Omni_rpm(data):
	global vel_net
	vel_net.data=[data.data,data.data,data.data,data.data]

def Gripper_net(data):
	global movimiento_net
	movimiento_net.data=data.data

#OF OMNI
def RpmOmni1(data):
	global rpm_net
	rpm_net.data[0]=sum(data.data)/len(data.data)

def RpmOmni2(data):
	global rpm_net
	rpm_net.data[1]=sum(data.data)/len(data.data)

def RpmOmni3(data):
	global rpm_net
	rpm_net.data[2]=sum(data.data)/len(data.data)
def Active_iot(data):
	global active_net
	active_net.data=data.data









rospy.Subscriber('node_red/rasp/omni_opc', Int8, Omni_opc)
rospy.Subscriber('node_red/rasp/movimiento', Char, Movimiento_omni)
rospy.Subscriber('node_red/rasp/rpm', Int8, Omni_rpm)
rospy.Subscriber('node_red/rasp/gripper', Char, Gripper_net)


rospy.Subscriber('rasp_control/omni1/rpm', Float32MultiArray, RpmOmni1)
rospy.Subscriber('rasp_control/omni2/rpm', Float32MultiArray, RpmOmni2)
rospy.Subscriber('rasp_control/omni3/rpm', Float32MultiArray, RpmOmni3)

rospy.Subscriber('broker/rasp/active', Int8, Active_iot)






pub_img = rospy.Publisher('node_red/cam', String, queue_size=1)
pub_rpm = rospy.Publisher('node_red/rpm', Float32MultiArray, queue_size=1)
pub_pos = rospy.Publisher('node_red/pos', Float32MultiArray, queue_size=1)
#pub_active = rospy.Publisher('node_red/active', Int8, queue_size=1)


pub_mov_omni_1 = rospy.Publisher('rasp_control/rasp1/movimiento', Char, queue_size=2)
pub_rpm_1 = rospy.Publisher('rasp_control/rasp1/setpoint', Float32MultiArray, queue_size=2)
pub_Opc_1 = rospy.Publisher('rasp_control/rasp1/opc', Int8, queue_size=2)
pub_mov_omni_2 = rospy.Publisher('rasp_control/rasp2/movimiento', Char, queue_size=2)
pub_rpm_2 = rospy.Publisher('rasp_control/rasp2/setpoint', Float32MultiArray, queue_size=2)
pub_Opc_2 = rospy.Publisher('rasp_control/rasp2/opc', Int8, queue_size=2)
pub_mov_omni_3 = rospy.Publisher('rasp_control/rasp3/movimiento', Char, queue_size=2)
pub_rpm_3 = rospy.Publisher('rasp_control/rasp3/setpoint', Float32MultiArray, queue_size=2)
pub_Opc_3 = rospy.Publisher('rasp_control/rasp3/opc', Int8, queue_size=2)



rospy.init_node('comunication_node_red', anonymous=True)
rospy.loginfo('node_control')
rate = rospy.Rate(30) # 10hz

def publicar_omni():
	global omni_n
	global movimiento_net
	global vel_net
	global _opc_omni_
	global rpm_net
	global active_net
	global movimiento_net_aux

	if active_net.data==1:
		if omni_n.data==1 or omni_n.data==100:
			pub_Opc_1.publish(_opc_omni_)
			pub_rpm_1.publish(vel_net)
			pub_mov_omni_1.publish(movimiento_net)
			
			if omni_n.data!=100:
				pub_mov_omni_2.publish(movimiento_net_aux)
				pub_mov_omni_3.publish(movimiento_net_aux)
			
		elif omni_n.data==2 or omni_n.data==100:
			#print(_opc_omni_.data)
			pub_Opc_2.publish(_opc_omni_)

			pub_rpm_2.publish(vel_net)
			pub_mov_omni_2.publish(movimiento_net)
			
			if omni_n.data!=100:
				pub_mov_omni_1.publish(movimiento_net_aux)
				pub_mov_omni_3.publish(movimiento_net_aux)
			
		elif omni_n.data==3 or omni_n.data==100:
			pub_Opc_3.publish(_opc_omni_)
			pub_rpm_3.publish(vel_net)
			pub_mov_omni_2.publish(movimiento_net)

			if omni_n.data!=100:
				pub_mov_omni_1.publish(movimiento_net_aux)
				pub_mov_omni_2.publish(movimiento_net_aux)
			
		if movimiento_net.data==43 or movimiento_net.data==45:
			movimiento_net.data=75
			time.sleep(0.1)
			

	


def publicar_nodered(video_msg):
	global active_net
	global rpm_net
	global pos_net
	#print(video_msg)
	pub_img.publish(video_msg)
	pub_pos.publish(pos_net)
	pub_rpm.publish(rpm_net)
