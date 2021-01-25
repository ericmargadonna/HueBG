#Configuration for lightController.py
#Written by Eric Margadonna
#January 22, 2021

SUGARMATE_API_CODE = 'zuv49t'
HUE_BRIDGE_IP = '192.168.0.100'

class Hues:
    red = 0
    green = 25500
    blue = 43690
    magenta = 54615

#Hues to be used by the application for mapping
OUT_HUE = Hues.blue
TARGET_HUE = Hues.magenta

#Refresh rate in seconds for the application
REFRESH_RATE = 20

#Minimum and maximum BG values for mapping the hues
MAX_BG = 250
MIN_BG = 70

#Target BG
TARGET_BG = 130
RNBW_ON_TARGET = True




