#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8



############VARIABLES DE PUBLICADORES############
#Opcion para iniciar modo automatico
opc1=Int8()
opc1.data=1
opc2=Int8()
opc2.data=1
opc3=Int8()
opc3.data=1
opc4=Int8()
opc4.data=1
opc5=Int8()
opc5.data=1

#Puntos para direccionar
pts1=Float32MultiArray()
pts1.data=[0,0,0,0,0,0]
pts2=Float32MultiArray()
pts2.data=[0,0,0,0,0,0]
pts3=Float32MultiArray()
pts3.data=[0,0,0,0,0,0]
pts4=Float32MultiArray()
pts4.data=[0,0,0,0,0,0]
pts5=Float32MultiArray()
pts5.data=[0,0,0,0,0,0]


############VARIABLES DE SUBSCRIPTORES
#Variable de estado de raspberry
estado1=Int8()
estado1.data=0
estado2=Int8()
estado2.data=0
estado3=Int8()
estado3.data=0
estado4=Int8()
estado4.data=0
estado5=Int8()
estado5.data=0






############FUNCIONES DE SUBSCRIPTORES############
#VESTADO DE RASPBERRY
def SetState1(data):
    global estado1
    estado1.data=data.data


def SetState2(data):
    global estado2
    estado2.data=data.data

def SetState3(data):
    global estado3
    estado3.data=data.data

def SetState4(data):
    global estado4
    estado4.data=data.data

def SetState5(data):
    global estado5
    estado5.data=data.data




############PUBLICADORES############
#OPcion para iniciar modo auto
pub1_opc = rospy.Publisher('/rasp_control/rasp1/opc', Int8, queue_size=2)
pub2_opc = rospy.Publisher('/rasp_control/rasp2/opc', Int8, queue_size=2)
pub3_opc = rospy.Publisher('/rasp_control/rasp3/opc', Int8, queue_size=2)
pub4_opc = rospy.Publisher('/rasp_control/rasp4/opc', Int8, queue_size=2)
pub5_opc = rospy.Publisher('/rasp_control/rasp5/opc', Int8, queue_size=2)

"""pub1_opc = rospy.Publisher('/rasp1/opc', Int8, queue_size=2)
pub2_opc = rospy.Publisher('/rasp2/opc', Int8, queue_size=2)
pub3_opc = rospy.Publisher('/rasp3/opc', Int8, queue_size=2)
pub4_opc = rospy.Publisher('/rasp4/opc', Int8, queue_size=2)
pub5_opc = rospy.Publisher('/rasp5/opc', Int8, queue_size=2)"""

#Puntos para movilizarse
pub1_pts = rospy.Publisher('/rasp_control/rasp1/puntos', Float32MultiArray, queue_size=2)
pub2_pts = rospy.Publisher('/rasp_control/rasp2/puntos', Float32MultiArray, queue_size=2)
pub3_pts = rospy.Publisher('/rasp_control/rasp3/puntos', Float32MultiArray, queue_size=2)
pub4_pts = rospy.Publisher('/rasp_control/rasp4/puntos', Float32MultiArray, queue_size=2)
pub5_pts = rospy.Publisher('/rasp_control/rasp5/puntos', Float32MultiArray, queue_size=2)

"""pub1_pts = rospy.Publisher('/rasp1/puntos', Float32MultiArray, queue_size=2)
pub2_pts = rospy.Publisher('/rasp2/puntos', Float32MultiArray, queue_size=2)
pub3_pts = rospy.Publisher('/rasp3/puntos', Float32MultiArray, queue_size=2)
pub4_pts = rospy.Publisher('/rasp4/puntos', Float32MultiArray, queue_size=2)
pub5_pts = rospy.Publisher('/rasp5/puntos', Float32MultiArray, queue_size=2)"""



############SUBSCRIPTORES############
#Subscriptor estado
rospy.Subscriber("/rasp_control/rasp1/estado", Int8, SetState1)
rospy.Subscriber("/rasp_control/rasp2/estado", Int8, SetState2)
rospy.Subscriber("/rasp_control/rasp3/estado", Int8, SetState3)
rospy.Subscriber("/rasp_control/rasp4/estado", Int8, SetState4)
rospy.Subscriber("/rasp_control/rasp5/estado", Int8, SetState5)

"""rospy.Subscriber("/rasp1/estado", Int8, SetState1)
rospy.Subscriber("/rasp2/estado", Int8, SetState2)
rospy.Subscriber("/rasp3/estado", Int8, SetState3)
rospy.Subscriber("/rasp4/estado", Int8, SetState4)
rospy.Subscriber("/rasp5/estado", Int8, SetState5)"""




############START NODE############
rospy.init_node('control_omni_auto_test', anonymous=True)
#rospy.loginfo('control_test_keyboard')
rate = rospy.Rate(10) # 10hz
#print('inicializado')

############PUBLICADOR FUNCIONES############

def publicar(ras_op):
    if ras_op==1:
        pub1_pts.publish(pts1)
        pub1_opc.publish(opc1)
    elif ras_op==2:
        pub2_pts.publish(pts2)
        pub2_opc.publish(opc2)
    elif ras_op==3:
        pub3_pts.publish(pts3)
        pub3_opc.publish(opc3)

    #rate.sleep()
