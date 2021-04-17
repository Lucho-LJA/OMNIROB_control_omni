#!/usr/bin/env python3
from lib_omni.config_central import *




if __name__ == '__main__':
    try:
        global opc
        global estado
        
        while not rospy.is_shutdown():

            if opc.data==0:
                #print(opc.data)
                global movimiento
                if movimiento.data=='+':
                    Abrir_gripper()
                    movimiento.data='K'
                elif movimiento.data=='-':
                    Cerrar_gripper()
                    movimiento.data='K'
                else:
                    publicar_opc0()
            elif opc.data==1:
                global puntos
                
                Calculo_pts()
                    
                Orientar()
                #time.sleep(1)
                if opc.data==1:
                    Caminar()
                    
                    #print(estado)
                    #print('---')
                        
                    estado.data=0
                    #print(estado)

            elif opc.data==2:
                Calculo_pts()
                Orientar()

                if opc.data==2:
                    opc.data=200
                    global puntos
                    puntos.data=[0,0,0,0,0,0]

                    publicar_est(1)
                    #Abrir_gripper()
                    #Caminar()
                    #Cerrar_gripper()
                    #Regresar()
                    #global estado
                    estado.data=0
                

            elif opc.data==3:
                Calculo_pts()
                Orientar()
                Caminar()
                Abrir_gripper()
                Regresar()
                Cerrar_gripper()

            elif opc.data==200:
                movimiento.data=='K'
                opc.data=0
                publicar_opc0()
            else:
                publicar_paro()
                #rospy.spin()
                rate.sleep()

    except rospy.ROSInterruptException:
        pass

