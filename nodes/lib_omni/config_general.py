#!/usr/bin/env python3
import math
#######VARIABLES OMNIROBOT#######
D_wheel=66 #Diametro rueda en milimetros
reduction_motor=86
ppr_motor=7 #ppr motor 1 , 2 , 3 , 4
count_per_rev=4*ppr_motor #conteo por vuelta motor
factor_dis=count_per_rev*reduction_motor/(math.pi*D_wheel)
setPoint_rpm_giro=[40,40,40,40]
setPoint_rpm_camino=[85,85,85,85]


#######VARIABLES#######
set_ticks=0
prev_ticks=0
actual_ticks=0

#######OMNI#######
Omni_n="omni3"
Rasp_n="rasp3"
#######Topicos rasp-esp#######
#SUBSCRIPTORES
topic_mpu=Omni_n+"/mpu"
topic_ticks=Omni_n+"/encoder"

#PUBLICADORES
topic_set=Omni_n+"/setpoint"
topic_mov=Omni_n+"/movimiento"



#######Topicos rasp-pc
#SUBSCRIPTORES
topic_opc=Rasp_n+"/opc"
topic_rasp_pts=Rasp_n+"/puntos"
topic_rasp_set=Rasp_n+"/setpoint"
topic_rasp_mov=Rasp_n+"/movimiento"

#PUBLICADORES
topic_rasp_est=Rasp_n+"/estado"




