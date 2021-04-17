#!/usr/bin/env python3


from lib_omni.key_config import *
import os











if __name__ == '__main__':
    
    try:
        option_input=1
        global num_omni
        while option_input==1:
            
            num_omni.data=int(input('Ingrese N. Omni: '))

            if num_omni.data !=1 and num_omni.data !=2 and num_omni.data !=3:
                if num_omni==0:
                    sys.exit()
                else:
                    print('Ingrese valor entre 1-3 o 0 para salir')
                    option_input=1
            else:
                option_input=0

            
                    
        global escuchador
        escuchador.start()
        publicar_opc()
        while not rospy.is_shutdown():
            if num_omni.data>0 and num_omni.data<4:
                publicar()
            else:
                break
        os.system('clear')
        sys.exit()

            

    except Exception as e:#rospy.ROSInterruptException:
        print(e)
        pass

