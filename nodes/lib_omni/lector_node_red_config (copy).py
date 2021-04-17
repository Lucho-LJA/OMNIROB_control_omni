import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Char
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8
_mov_omni_1=Char()
_mov_omni_1.data=75


_mov_omni_2=Int16()
_mov_omni_2.data=75
_mov_omni_3=Int16()
_mov_omni_3.data=75
_mov_omni_4=Int16()
_mov_omni_4.data=75
_mov_omni_5=Int16()
_mov_omni_5.data=75




_rpm_omni_1=Float32MultiArray()
_rpm_omni_1.data=[0,0,0,0]

_rpm_omni_2=Int16()
_rpm_omni_2.data=0
_rpm_omni_3=Int16()
_rpm_omni_3.data=0
_rpm_omni_4=Int16()
_rpm_omni_4.data=0
_rpm_omni_5=Int16()
_rpm_omni_5.data=0

_opc_omni_1=Int8()
_opc_omni_1.data=0

def Movimiento_omni1(data):
    _mov_omni_1.data=data.data

def SetPoint1(data):
    _rpm_omni_1.data=[data.data,data.data,data.data,data.data]



rospy.Subscriber('node_red/rasp2/movimiento', Int16, Movimiento_omni1)
rospy.Subscriber('node_red/rasp2/rpm', Int16, SetPoint1)




pub_mov_omni_1 = rospy.Publisher('rasp_control/rasp2/movimiento', Char, queue_size=2)
pub_rpm_1 = rospy.Publisher('rasp_control/rasp2/setpoint', Float32MultiArray, queue_size=2)
pub_Opc_1 = rospy.Publisher('rasp_control/rasp2/opc', Int8, queue_size=2)


rospy.init_node('comunication_node_red', anonymous=True)
rospy.loginfo('node_control')
rate = rospy.Rate(10) # 10hz

def publicar_omni1():
    pub_mov_omni_1.publish(_mov_omni_1)
    pub_rpm_1.publish(_rpm_omni_1)
    pub_Opc_1.publish(_opc_omni_1)
    rate.sleep()
