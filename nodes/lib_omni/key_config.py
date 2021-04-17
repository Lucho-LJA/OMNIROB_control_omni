import rospy
from std_msgs.msg import Char
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int8
from pynput import keyboard as kb
import sys
#global num_omni.data
num_omni=Int8()
num_omni.data=0


_opc_omni=Int8()
_opc_omni.data=0


_mov_omni=Char()
_mov_omni.data=ord('K');
_setpoint_omni=Float32MultiArray()
_setpoint_omni.data=[0,0,0,0]

rpm_=80

def pulsa(tecla):
	global _opc_omni
	global num_omni

	if tecla == kb.KeyCode.from_char('w'):
		#print(tecla)
		_mov_omni.data=ord('A')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('s'):
		_mov_omni.data=ord('B')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('d'):
		_mov_omni.data=ord('C')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('a'):
		_mov_omni.data=ord('D')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('q'):
		_mov_omni.data=ord('E')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('e'):
		_mov_omni.data=ord('F')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('2'):
		_mov_omni.data=ord('G')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('4'):
		_mov_omni.data=ord('H')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('3'):
		_mov_omni.data=ord('I')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif tecla == kb.KeyCode.from_char('1'):
		_mov_omni.data=ord('J')
		_setpoint_omni.data=[rpm_,rpm_,rpm_,rpm_]
	elif str(tecla) == str('Key.space'):
		_mov_omni.data=ord('L')
		_setpoint_omni.data=[0,0,0,0]
	elif tecla == kb.KeyCode.from_char('+'):
		_mov_omni.data=ord('+')
		_setpoint_omni.data=[0,0,0,0]
	elif tecla == kb.KeyCode.from_char('-'):
		_mov_omni.data=ord('-')
		_setpoint_omni.data=[0,0,0,0]
	elif str(tecla) == str(','):
		_opc_omni.data=0
		if num_omni.data==1:
			pubOpc1.publish(_opc_omni)
		elif num_omni.data==2:
			pubOpc2.publish(_opc_omni)
		elif num_omni.data==3:
			pubOpc3.publish(_opc_omni)
	elif tecla == kb.KeyCode.from_char('0'):
		_opc_omni.data=100
		if num_omni.data==1:
			pubOpc1.publish(_opc_omni)
		elif num_omni.data==2:
			pubOpc2.publish(_opc_omni)
		elif num_omni.data==3:
			pubOpc3.publish(_opc_omni)
	elif str(tecla) == str('Key.esc'):
		_opc_omni.data=0
		print(num_omni.data)
		if num_omni.data==1:
			pubOpc1.publish(_opc_omni)
		elif num_omni.data==2:
			pubOpc2.publish(_opc_omni)
		elif num_omni.data==3:
			pubOpc3.publish(_opc_omni)
		num_omni.data=0
		#sys.exit()
	else:
		#print(str(tecla))
		_setpoint_omni.data=[0,0,0,0]
		_mov_omni.data=ord('K')

def suelta(tecla):
	print('suelta')
	_setpoint_omni.data=[0,0,0,0]
	_mov_omni.data=ord('K')

escuchador = kb.Listener(pulsa, suelta)






pubS1 = rospy.Publisher('rasp_control/rasp1/setpoint', Float32MultiArray, queue_size=10)
pubM1 = rospy.Publisher('rasp_control/rasp1/movimiento', Char, queue_size=10)
pubOpc1 = rospy.Publisher('rasp_control/rasp1/opc', Int8, queue_size=10)

pubS2 = rospy.Publisher('rasp_control/rasp2/setpoint', Float32MultiArray, queue_size=10)
pubM2 = rospy.Publisher('rasp_control/rasp2/movimiento', Char, queue_size=10)
pubOpc2 = rospy.Publisher('rasp_control/rasp2/opc', Int8, queue_size=10)

pubS3 = rospy.Publisher('rasp_control/rasp3/setpoint', Float32MultiArray, queue_size=10)
pubM3 = rospy.Publisher('rasp_control/rasp3/movimiento', Char, queue_size=10)
pubOpc3 = rospy.Publisher('rasp_control/rasp3/opc', Int8, queue_size=10)






rospy.init_node('control_omni_teclado_test', anonymous=True)
rospy.loginfo('control_test_keyboard')
rate = rospy.Rate(10) # 10hz
print('inicializado')




def publicar():
	global num_omni
	global _setpoint_omni
	global _mov_omni
	if num_omni.data==1:
		pubS1.publish(_setpoint_omni)
		pubM1.publish(_mov_omni)
	elif num_omni.data==2:
		pubS2.publish(_setpoint_omni)
		pubM2.publish(_mov_omni)
	elif num_omni.data==3:
		pubS3.publish(_setpoint_omni)
		pubM3.publish(_mov_omni)

	rate.sleep()

def publicar_opc():
	global num_omni
	global _opc_omni

	if num_omni.data==1:
		pubOpc1.publish(_opc_omni)

	elif num_omni.data==2:
		pubOpc2.publish(_opc_omni)

	elif num_omni.data==3:
		pubOpc3.publish(_opc_omni)

	rate.sleep()
