import socket 
import sys 

#These are the inital variables for the Micropulse 5 Phased Array, my plan is 
#later develop a gui to let the user change these and have a desired effect
#This is a 1 sender 1 reciever mode 
FMCa = dict()
FMCa['TXelements'] = 1   #Transmitter elements
FMCa['RXelements'] = 1   #Reciever Elements   
FMCa['freq'] = 5e6       
FMCa['pitch'] = 1       #Spacing of inspection elements 
FMCa['Mp_default_vel'] = 5.9e6
FMCa['L_vel'] = 5.9e6    #Linear Velocity 
FMCa['start_gate'] = 1   
FMCa['end_gate'] = 200 
FMCa['DOF'] = 1 
#FMC['sample_freq'] = 25e6
FMCa['gain'] = 200
FMCa['voltage'] = 100    #DO not exceed 100V
FMCa['width'] = 110e-9   
FMCa['filter_no'] = 1
FMCa['wave_mode'] = 1
FMCa['avgs'] = 1
FMCa['prf'] = 200
FMCa['matrix'] = 'full'


Algorithim = dict()
Algorithim['SPA'] = 'SPA' 

Wedges = dict()
Wedges['Yes'] = 'yes'
Wedges['No'] = 'No'

IP = '10.1.1.2'

#Initalising the socket 

TCP_IP = '10.1.1.2'
TCP_PORT = 1067
BUFFER_SIZE = 2018880

t = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
t.connect((TCP_IP,TCP_PORT))
#
#t.send('RST ',FMC.sample_freq/1e6)
