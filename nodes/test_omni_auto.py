#!/usr/bin/env python3
import time
import sys
from lib_omni.auto_config import *




if __name__ == '__main__':
    try:
        global estado1
        global estado2
        global estado3
        global estado4
        global estado5
        global opc1
        global opc2
        global opc3
        global opc4
        global opc5
        #pts1.data=[0,0,0,1,0,0]
        pts1.data=[2293,1032,784,635,0,0]
        global pts2
        pts2.data=[0,0,0,1,0,0]

        global pts3
        pts3.data=[0,0,0,1,0,0]
        #pts3.data=[1100,762,1223,758,0,0]
        #pts3.data=[0,0,141,-19,0,0]
        global pts4
        pts4.data=[0,0,0,1,0,0]
        global pts5
        pts5.data=[0,0,0,1,0,0]

        omni_option=int(input('Ingrese N. Omni: '))

        if omni_option !=1 and omni_option !=2 and omni_option !=3 and omni_option !=4 and omni_option !=5 and omni_option !=10:

            sys.exit()

        else:
            
            while not rospy.is_shutdown():
                punto_omni=[]

                punto_omni=[float(item) for item in input("Ingrese  xp yp: ").split()]
                if len(punto_omni)==1 and punto_omni[0]==0:
                    omni_option=100

                else:
                    while len(punto_omni)!=2:
                        punto_omni=[]
                        print('Ingrese solo dos valores')
                        punto_omni=[float(item) for item in input("Ingrese  xp yp: ").split()]

                        if len(punto_omni)==1 and punto_omni[0]==0:
                            omni_option=100
                            break
                if omni_option!=100:
                    tarea_opc=int(input('Tarea 1:mov2pts 2:CogerObj 3:ColocarObj:  4:giro :'))
                    while tarea_opc!=1 and tarea_opc!=2 and tarea_opc!=3 and tarea_opc!=4:
                        tarea_opc=int(input('Tarea 1:mov2pts 2:CogerObj 3:ColocarObj 4:giro : '))

                    if tarea_opc==1:
                        opc1.data=1
                        opc2.data=1
                        opc3.data=1
                    elif tarea_opc==2:
                        opc1.data=2
                        opc2.data=2
                        opc3.data=2
                    elif tarea_opc==3:
                        opc1.data=3
                        opc2.data=3
                        opc3.data=3
                    elif tarea_opc==4:
                        opc1.data=4
                        opc2.data=4
                        opc3.data=4
                



                if omni_option==1:
                    pts1.data[4]=punto_omni[0]
                    pts1.data[5]=punto_omni[1]
                    publicar(omni_option)
                    while estado1.data!=1 and estado1.data!=2 and estado1.data!=3 and estado1.data!=4:
                        time.sleep(0.1)
                    print(estado1.data)
                    estado1.data=0
                    print(estado1.data)
                    print('FIN')

                elif omni_option==2:
                    pts2.data[4]=punto_omni[0]
                    pts2.data[5]=punto_omni[1]
                    publicar(omni_option)
                    while estado2.data!=1 and estado2.data!=2 and estado2.data!=3 and estado2.data!=4:
                        time.sleep(0.1)
                    print(estado2.data)
                    estado2.data=0
                    print(estado2.data)
                    print('FIN')

                elif omni_option==3:
                    pts3.data[4]=punto_omni[0]
                    pts3.data[5]=punto_omni[1]
                    publicar(omni_option)
                    while estado3.data!=1 and estado3.data!=2 and estado3.data!=3 and estado3.data!=4:
                        time.sleep(0.1)
                    print(estado3.data)
                    estado3.data=0
                    print(estado3.data)
                    print('FIN')


                else:
                    sys.exit()

                
                pts2.data=[0,0,0,1,0,0]
                pts3.data=[0,0,0,1,0,0]
                pts4.data=[0,0,0,1,0,0]
                pts5.data=[0,0,0,1,0,0]

            



            rate.sleep()
    except rospy.ROSInterruptException:
        pass
