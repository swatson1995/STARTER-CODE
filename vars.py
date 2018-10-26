# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 03:31:17 2018

@author: Lab1
"""

def Initalise_vars (FMCa = None):
    #FMCa = dict()
    
    if FMCa is None:
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
    FMCa['sample_freq'] = 25e6
    FMCa['gain'] = 200
    FMCa['voltage'] = 100    #DO not exceed 100V
    FMCa['width'] = 110e-9   
    FMCa['filter_no'] = 1
    FMCa['wave_mode'] = 1
    FMCa['avgs'] = 1
    FMCa['prf'] = 200
    FMCa['matrix'] = 'full'
    
    return FMCa


def IP():
    
    IP='10.1.1.2'
    port = 1067
    IP_address=(IP,port)
    return IP_address    

def algorithm(algorithm = None) :
    if algorithm is None:
        algorithm = dict()
        
    algorithm['LTA'] = 'LTA'
    algorithm['SPA'] = 'SPA'
    
    return algorithm 

def wedges(wedges = None):
    if wedges is None :
        wedges= dict()
    wedges['yes'] = 'yes'
    wedges['no'] = 'no'
    
    return wedges 
 
