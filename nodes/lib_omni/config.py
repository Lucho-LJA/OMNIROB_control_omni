#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Char
from lib_omni.pid_control import *

dt_board = 100 #delay system board in ms
Kp_motor=[21.4,20.7,20.8,20.5]
Ki_motor=[228,276,221,183]
Kd_motor=[0,0,0,0]
#PWM_motor=[0,0,0,0]
RPM_motor=[0,0,0,0]
MPU_motor=[0,0,0,0,0,0]
max_pwm_=1023
Setpoint_omni=[0,0,0,0]
Omni_sensor=[0,0,0,0]


_pwm_omni=Float32MultiArray()
_pwm_omni.data=[0,0,0,0]

motor_omni=PID_omni(Kp_motor, Ki_motor, Kd_motor, dt_board, max_pwm_)

def callback(data):
    global Setpoint_omni
    Setpoint_omni=data.data

def callback2(data):
    global Omni_sensor
    Omni_sensor=data.data


pub = rospy.Publisher('omni/pwm', Float32MultiArray, queue_size=2)
rospy.Subscriber("omni/rpm", Float32MultiArray, callback2)
rospy.Subscriber("omni/setpoint", Float32MultiArray, callback)
rospy.init_node('control_omni_raspberry', anonymous=True)
rospy.loginfo('control_raspberry')
rate = rospy.Rate(10) # 100hz
print('inicializado')







def publicar_pwm():
    global Setpoint_omni
    global Omni_sensor

    _pwm_omni.data=motor_omni.compute_pid(Setpoint_omni,Omni_sensor)
    print(_pwm_omni.data)
    
    pub.publish(_pwm_omni)
    

