# OMNIROB_control_omni
#####Installed programs
##ROS-MELODIC--->Tutorial config_ros
##pigpiod
sudo apt-get update
sudo apt-get install pigpio python-pigpio python3-pigpio

##Configure the pigpiod command
sudo visudo
#Add the code:
<user(omni4)> ALL=NOPASSWD:/usr/bin/pigpiod


#Connect HDMI, MOUSE and config Login Router.
#Obtain with ifconfig the MAC address
#Config in router or raspberry a IPstatic
#RASP1-->192.168.1.111
#RASP2-->192.168.1.112
#RASP3-->192.168.1.113
#If the router have a diferent subred 
	#configure with omni's directions with<Router's Subred(192.168.1)>.<last Direcction>
	#In ~/.bashrc config ROSMASTER with ip of Broker(pc)

#Install package control_omni in ~/catkin_ws/src/
git clone <url git github>

#Install package rosserial_python (modificate) in ~/catkin_ws/src/
git clone <url git hub>



#Modifiy ~/catkin_ws/src/control_omni/nodes/lib_omni/config_general.py lin 20 Omni_n

	#omni1--->"omni1"
	#omni2--->"omni2"
	#omni3--->"omni3"
#Modifiy ~/catkin_ws/src/control_omni/nodes/lib_omni/config_general.py lin 21 Rasp_n

	#omni1--->"rasp1"
	#omni2--->"rasp2"
	#omni3--->"rasp3"

#Modifiy ~/catkin_ws/src/rosserial_python/nodes/server_rasp.py : variable tcp_portnum

	#omni1--->11421
	#omni2--->11422
	#omni3--->11423

#Add in ~/.basrc

export ROS_MASTER_URI=http://<IP BROKER (PC)>:11311
export ROS_HOSTNAME=<IP_RASPBERRY>
#USE OF RASPBERRY'S I/O
#check if pigpiod is running 
if pgrep "pigpiod" >/dev/null
  then
     echo "pigpiod initialilized in other session"
  else
     if  sudo pigpiod
       then
          echo "pigpiod running"
     fi
fi


if [[ -n $SSH_CONNECTION ]] ; then

  if pgrep "roslaunch" >/dev/null
    then
      echo "Ejecutandose roslaunch"
    else
     . ~/script_ros.sh
  fi
fi
