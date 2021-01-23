#Configuration for lightController.py
#Written by Eric Margadonna
#January 22, 2021

SUGARMATE_API_CODE = 'zuv49t'
HUE_BRIDGE_IP = '192.168.0.100'

#Hue Values for red, green, and blue
hues = {'red':0, 'green':25500, 'blue':43690}
#Hues to be used by the application for mapping
HIGH_HUE = hues.get('red')
LOW_HUE = hues.get('green')

#Refresh rate in seconds for the application
REFRESH_RATE = 20

#Minimum and maximum BG values for mapping the hues
MAX_BG = 250
MIN_BG = 70

#Target BG for rainbow mode, 
#setting this to null will disable the effect
TARGET_BG = 130




