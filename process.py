#### designed to set up the scanning profile of the scan 

def processing(process = None):
    if process == None :
        process = dict()
    
    process['xmin'] = 10
    process['xmax'] = 80
    process['zmin'] = -20
    process['zmax'] = 20
    process['xresl'] = 0.5
    process['zresl'] = 0.5
    process['threshold'] = 30 
    process['plot_type'] = 'linear'
    process['directivity'] = 'no'
    process['inverse'] = 'no'
    
    
    
