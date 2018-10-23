import socket 

#These are the inital variables for the Micropulse 5 Phased Array, my plan is 
#later develop a gui to let the user change these and have a desired effect
#This is a 1 sender 1 reciever mode 
FMC = dict()
FMC['TXelements'] = 1   #Transmitter elements
FMC['RXelements'] = 1   #Reciever Elements   
FMC['freq'] = 5e6       
FMC['pitch'] = 1        #Spacing of inspection elements 
FMC['Mp_default_vel'] = 5.9e6
FMC['L_vel'] = 5.9e6    #Linear Velocity 
FMC['start_gate'] = 1   
FMC['end_gate'] = 200 
FMC['DOF'] = 1 
FMC['sample_freq'] = 25e6
FMC['gain'] = 200
FMC['voltage'] = 100    #DO not exceed 100V
FMC['width'] = 110e-9   
FMC['filter_no'] = 1
FMC['wave_mode'] = 1
FMC['avgs'] = 1
FMC['prf'] = 200
FMC['matrix'] = 'full'


Algorithim = dict()
Algorithim['SPA'] = 'SPA' 

Wedges = dict()
Wedges['Yes'] = 'yes'
Wedges['No'] = 'no'

IP = '10.1.1.2'

#Initalising the socket 

TCP_IP = '10.1.1.2'
TCP_PORT = 1067
BUFFER_SIZE = 2018880

t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
t.connect((TCP_IP,TCP_PORT))

t.send('RST ',FMC.sample_freq/1e6)
