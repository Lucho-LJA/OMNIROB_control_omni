#!/usr/bin/env python3
import rospy
import math
import time
#import pigpio

from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int32MultiArray
from std_msgs.msg import Char
from std_msgs.msg import Int8
from lib_omni.config_general import *

#######Variables-Raspberry#######
#rpi=pigpio.pi() # Conectar a local pi

#rpi.set_mode(2,pigpio.OUTPUT) #modo de gpio
# start 1500 us servo pulses on gpio2

# set gpio modes
#rpi.set_mode(2, pigpio.OUTPUT)

#rpi.set_servo_pulsewidth(2, 1500)
#time.sleep(1)
#for _i in range(5): #loop between -90 and 90 degrees
#rpi.set_servo_pulsewidth(2,2500)
#time.sleep(1)
#rpi.set_servo_pulsewidth(2,600)
#time.sleep(1)
#rpi.set_servo_pulsewidth(2, 1500)
#time.sleep(1)
 
#rpi.set_servo_pulsewidth(2, 0) # stop servo pulses
 
#rpi.stop() # terminate connection and release resources




#######Variables-Modo automatico#######
distancia=0
angulo=0
rango_des=0
rango_prev=0
error_ang=1
opc_rang_ang =0
med_ang=0
prev_ticks=[0,0,0,0]


#######Subscripciones#######
#Opcion entre manual y automatico
opc=Int8()
opc.data=0
#Puntoa P0, P1, P3 para movimiento a P3
puntos=Float32MultiArray()
puntos.data=[0,0,0,0,0,0]
#Datos Imu
imu_d=Float32MultiArray()
imu_d.data=[0,0,0,0,0,0]
#Datos encoder
encoder_ticks=Int32MultiArray()
encoder_ticks.data=[0,0,0,0]




#######Publiciones con subscriptor#######
#Velocidad de carro
Setpoint_omni=Float32MultiArray()
Setpoint_omni.data=[0,0,0,0]
#Tipo de movimiento
movimiento=Char()
movimiento.data=ord('K')
#Estado de rasberry al moverse de punto A -> B
estado=Int8()
estado.data=0


#######FUNCIONES DE CALCULO#######
def Calculo_pts():
    global puntos
    
    
    x_0=puntos.data[2]-puntos.data[0]
    y_0=puntos.data[3]-puntos.data[1]
    x_p=puntos.data[4]-puntos.data[0]
    y_p=puntos.data[5]-puntos.data[1]


    global distancia
    distancia = math.sqrt(x_p*x_p + y_p*y_p)

    global factor_dis
    distancia=factor_dis*distancia

    m0=x_0*x_0+y_0*y_0
    mp=x_p*x_p+y_p*y_p
    if mp!=0:
        x_0=x_0/math.sqrt(m0)
        y_0=y_0/math.sqrt(m0)
        x_p=x_p/math.sqrt(mp)
        y_p=y_p/math.sqrt(mp)

        val_aux=(x_0*y_p-x_p*y_0)/(x_0*x_0+y_0*y_0)

        signo_ang=math.asin(val_aux)
        global angulo
        angulo=math.degrees(math.acos((y_0*y_p+x_0*x_p)/(x_0*x_0+y_0*y_0)))
        if signo_ang>0:
            angulo=-angulo
    else:
        angulo=0

    global med_ang
    angulo=angulo+med_ang
    if angulo<0:
        angulo=360+angulo

    if angulo>=360:
        angulo=-360+angulo


    global rango_des
    global rango_prev
    global opc_rang_ang


    if angulo+error_ang>360:
        rango_des=angulo+error_ang-360
        rango_prev=angulo-error_ang
        opc_rang_ang=1
    elif angulo-error_ang< 0:
        rango_des=angulo+error_ang
        rango_prev=360+angulo-error_ang
        opc_rang_ang=2
    else:
        rango_prev=angulo-error_ang
        rango_des=angulo+error_ang
        opc_rang_ang=0


def Abrir_gripper():
    #Definir habertura de griper


    time.sleep(0.1)

def Cerrar_gripper():
    #Definir Cerrar griper


    time.sleep(0.1)

def Regresar():
    #Definir Regresar



    time.sleep(0.1)







#######FUNCIONES DE SUBSCRIPCIONES#######
def Option_function(data):
    global opc
    opc.data=data.data


def Movimiento_omni(data):
    global movimiento
    movimiento.data=data.data

def SetPoint(data):
    global Setpoint_omni
    Setpoint_omni.data=data.data

def SetPts(data):
    global puntos
    puntos.data=data.data

def SetTicks(data):
    global encoder_ticks
    encoder_ticks.data=data.data

def SetMPU(data):
    global imu_d
    global med_ang
    imu_d.data=data.data
    med_ang=imu_d.data[3]

    if med_ang<0:
        med_ang=360+med_ang






rospy.Subscriber(topic_opc, Int8, Option_function)
rospy.Subscriber(topic_rasp_mov, Char, Movimiento_omni)
rospy.Subscriber(topic_rasp_set, Float32MultiArray, SetPoint)
rospy.Subscriber(topic_rasp_pts, Float32MultiArray, SetPts)
rospy.Subscriber(topic_ticks, Int32MultiArray, SetTicks)
rospy.Subscriber(topic_mpu, Float32MultiArray, SetMPU)


pub_set_point = rospy.Publisher(topic_set, Float32MultiArray, queue_size=2)
pub_movimiento=rospy.Publisher(topic_mov, Char, queue_size=2)
pub_estado=rospy.Publisher(topic_rasp_est, Int8, queue_size=2)


rospy.init_node('control_omni', anonymous=True)
#rospy.loginfo('control_test_keyboard')
rate = rospy.Rate(10) # 100hz


############FUNCIONES PUBLICADORAS############

def publicar_opc0():
    global Setpoint_omni
    global movimiento

    """print(str(chr(movimiento.data))+" - "+str(Setpoint_omni.data))
    print("---")"""
    
    pub_set_point.publish(Setpoint_omni)
    pub_movimiento.publish(movimiento)

def publicar_est(opc_st):
    global estado
    estado.data=opc_st

    pub_estado.publish(estado)

def publicar_opc1(mov):
    global Setpoint_omni
    global movimiento
    movimiento.data=ord(mov)

    pub_set_point.publish(Setpoint_omni)
    pub_movimiento.publish(movimiento)

def publicar_paro():
    global estado
    global puntos
    global angulo
    global distancia
    global Setpoint_omni
    global movimiento
    estado.data=0
    puntos.data=[0,0,0,0,0,0]
    angulo=0
    distancia=0
    Setpoint_omni.data=[0,0,0,0]
    movimiento.data=ord('L')
    pub_set_point.publish(Setpoint_omni)
    pub_movimiento.publish(movimiento)
    time.sleep(0.1)
    movimiento.data=ord('K')
    pub_movimiento.publish(movimiento)





############FUNCIONES PUBLICADORAS EN OPC2############

def Orientar():
    global opc_rang_ang
    global angulo
    global rango_des
    global rango_prev
    global med_ang
    global prev_med_ang
    global Setpoint_omni
    global setPoint_rpm_giro
    global opc

    Setpoint_omni.data=setPoint_rpm_giro

    """print(angulo)
    print(med_ang)
    print(opc_rang_ang)
    time.sleep(3)
    print(rango_prev)
    print(rango_des)"""
    if opc_rang_ang==0:
        while not (med_ang>rango_prev and med_ang<rango_des):
            if med_ang>angulo:
                if med_ang - angulo <180:
                    publicar_opc1('E')
                    if abs(med_ang - angulo) <30:
                        time.sleep(0.05)
                        publicar_opc1('L')
                else:
                    publicar_opc1('F')
                    if abs(med_ang - angulo) <30:
                        time.sleep(0.05)
                        publicar_opc1('L')
            else:
                if angulo - med_ang <180:
                    publicar_opc1('F')
                    if abs(med_ang - angulo) <30:
                        time.sleep(0.05)
                        publicar_opc1('L')
                else:
                    publicar_opc1('E')
                    if abs(med_ang - angulo) <30:
                        time.sleep(0.05)
                        publicar_opc1('L')
            """print(med_ang)
            print(rango_prev)
            print(rango_des)"""
            rate.sleep()
            if opc.data!=1 and opc.data!=2 and opc.data!=3:
                #print('paro0')
                break
        publicar_opc1('L')

    if opc_rang_ang==1 or opc_rang_ang==2:
        while med_ang>rango_des and med_ang<rango_prev:
            if med_ang>angulo:
                if med_ang - angulo <180:
                    publicar_opc1('E')
                    if abs(med_ang - angulo) <40:
                        time.sleep(0.05)
                        publicar_opc1('L')
                else:
                    publicar_opc1('F')
                    if abs(med_ang - angulo) <40:
                        time.sleep(0.05)
                        publicar_opc1('L')
            else:
                if angulo - med_ang <180:
                    publicar_opc1('F')
                    if abs(med_ang - angulo) <40:
                        time.sleep(0.05)
                        publicar_opc1('L')
                else:
                    publicar_opc1('E')
                    if abs(med_ang - angulo) <40:
                        time.sleep(0.05)
                        publicar_opc1('L')
            """print(med_ang)
            print(rango_prev)
            print(rango_des)"""
            rate.sleep()
            if opc.data!=1 and opc.data!=2 and opc.data!=3:
                #print('paro1')
                break
        publicar_opc1('L')



    global prev_ticks
    if opc.data!=1 and opc.data!=2 and opc.data!=3:
        publicar_opc1('K')
        prev_ticks=[0,0,0,0]
    else:
        publicar_opc1('L')
        prev_ticks=encoder_ticks.data
        #print(prev_ticks)





def Caminar():
    global distancia
    global prev_ticks
    actual_ticks=0
    global encoder_ticks
    global Setpoint_omni
    global setPoint_rpm_camino
    Setpoint_omni.data=setPoint_rpm_camino
    print(distancia)

    actual_ticks=abs(encoder_ticks.data[0] - prev_ticks[0])+abs(encoder_ticks.data[1] - prev_ticks[1])+abs(encoder_ticks.data[2] - prev_ticks[2])+abs(encoder_ticks.data[3] - prev_ticks[3])
    while (actual_ticks/4) < distancia:
        publicar_opc1('A')
        actual_ticks = abs(encoder_ticks.data[0] - prev_ticks[0])+abs(encoder_ticks.data[1] - prev_ticks[1])+abs(encoder_ticks.data[2] - prev_ticks[2])+abs(encoder_ticks.data[3] - prev_ticks[3])
        rate.sleep()
    publicar_opc1('L')
    global estado
    estado.data=1
    time.sleep(0.01)
    Setpoint_omni.data=[0,0,0,0]
    publicar_opc1('K')
    global opc
    opc.data=100
    prev_ticks=0
    actual_ticks=0
    distancia=0
    global puntos
    puntos.data=[0,0,0,0,0,0]
    publicar_est(1)








