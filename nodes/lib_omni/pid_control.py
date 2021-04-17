#!/usr/bin/env python3
class PID_omni():
    def __init__(self, kp, ki, kd, delta_t, max_pwm): 
        self.kp=kp
        self.ki = ki
        self.kd=kd
        self.delta_t_=delta_t
        self.max_pwm=max_pwm
        self.integral=[0,0,0,0]
        self.derivativa=[0,0,0,0]
        self.prev_error=[0,0,0,0]

    def compute_pid(self,setpoint,rpm_medida_):
        error=[0,0,0,0]
        pid=[0,0,0,0]

        error[0] = setpoint[0] - rpm_medida_[0]
        error[1] = setpoint[1] - rpm_medida_[1]
        error[2] = setpoint[2] - rpm_medida_[2]
        error[3] = setpoint[3] - rpm_medida_[3]

        self.integral[0]+= error[0]*self.delta_t_/1000
        self.integral[1]+= error[1]*self.delta_t_/1000
        self.integral[2]+= error[2]*self.delta_t_/1000
        self.integral[3]+= error[3]*self.delta_t_/1000

        if (self.integral[0]>self.max_pwm):
            self.integral[0]=self.max_pwm
        elif (self.integral[0]< -self.max_pwm):
            self.integral[0]=-self.max_pwm
        if (self.integral[1]>self.max_pwm):
            self.integral[1]=self.max_pwm
        elif (self.integral[1]< -self.max_pwm):
            self.integral[1]=-self.max_pwm
        if (self.integral[2]>self.max_pwm):
            self.integral[2]=self.max_pwm
        elif (self.integral[2]< -self.max_pwm):
            self.integral[2]=-self.max_pwm
        if (self.integral[3]>self.max_pwm):
            self.integral[3]=self.max_pwm
        elif (self.integral[3]< -self.max_pwm):
            self.integral[3]=-self.max_pwm

        self.derivativa[0] = (error[0] - self.prev_error[0])*1000/self.delta_t_
        self.derivativa[1] = (error[1] - self.prev_error[1])*1000/self.delta_t_
        self.derivativa[2] = (error[2] - self.prev_error[2])*1000/self.delta_t_
        self.derivativa[3] = (error[3] - self.prev_error[3])*1000/self.delta_t_

        pid[0] = (self.kp[0] * error[0]) + (self.ki[0] * self.integral[0]) + (self.kd[0]*self.derivativa[0])
        pid[1] = (self.kp[1] * error[1]) + (self.ki[1] * self.integral[1]) + (self.kd[1]*self.derivativa[1])
        pid[2] = (self.kp[2] * error[2]) + (self.ki[2] * self.integral[2]) + (self.kd[2]*self.derivativa[2])
        pid[3] = (self.kp[3] * error[3]) + (self.ki[3] * self.integral[3]) + (self.kd[3]*self.derivativa[3])

        if pid[0]>self.max_pwm:
            pid[0]=self.max_pwm
        elif (pid[0]<0):
            pid[0]=0
        if pid[1]>self.max_pwm:
            pid[1]=self.max_pwm
        elif (pid[1]<0):
            pid[1]=0
        if pid[2]>self.max_pwm:
            pid[2]=self.max_pwm
        elif (pid[2]<0):
            pid[2]=0
        if pid[3]>self.max_pwm:
            pid[3]=self.max_pwm
        elif (pid[3]<0):
            pid[3]=0


        self.prev_error[0]= error[0]
        self.prev_error[1]= error[1]
        self.prev_error[2]= error[2]
        self.prev_error[3]= error[3]

        return pid


    def update_pid(self,kp,ki,kd,dt_board_):
        self.delta_t = dt_board_ #delay system board in ms
        self.kp=kp
        self.ki=ki
        self.kd=kd

