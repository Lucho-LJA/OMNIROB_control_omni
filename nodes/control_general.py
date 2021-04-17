#!/usr/bin/env python3
from lib_omni.config import *




if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            publicar_pwm()
            #rospy.spin()
            rate.sleep()
    except rospy.ROSInterruptException:
        pass

