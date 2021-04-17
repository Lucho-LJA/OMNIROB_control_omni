#!/usr/bin/env python3

from lib_omni.lector_node_red_config import *






if __name__ == '__main__':
    
    try:
        
        while not rospy.is_shutdown():
            publicar_omni1()

            #rate.sleep();

            

    except Exception as e:#rospy.ROSInterruptException:
        print(e)
        pass
