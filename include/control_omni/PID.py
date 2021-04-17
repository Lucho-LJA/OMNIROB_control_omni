#!/usr/bin/env python3
class PID():
    def __init__(self, kp, ki, kd, delta_t, max_pwm): 
        self.kp=kp
        self.ki = ki
        self.kd=kd
        self.delta_t=delta_t
        self.max_pwm=max_pwm
        self.integral=0
        self.derivativa=0
        self.prev_error=0

    def compute(self,setpoint,rpm_medida):
        error = setpoint - rpm_medida
        pid=0
        self.integral+= error*self.delta_t_/1000;
        if (self.integral>self.max_pwm):
            self.integral=self.max_pwm
        elif (self.integral< -self.max_pwm):
            self.integral=-self.max_pwm

        self.derivativa = (error - self.prev_error)*1000/self.delta_t
        pid = (self.kp * error) + (self.ki * self.integral) + (self.kd_*self.derivativa)
        if pid>self.max_pwm:
            pid=self.max_pwm
        elif (pid<0):
            pid=0
        self.prev_error= error;

        return pid;
