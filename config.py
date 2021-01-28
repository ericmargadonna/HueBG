#Configuration for lightController.py
#Written by Eric Margadonna
#January 22, 2021

#----------------------------------#
#--BE SURE TO SET THESE VARIABLES--#
#----------------------------------#
SUGARMATE_API_CODE = 'zuv49t'
HUE_BRIDGE_IP = '192.168.0.100'

#Refresh rate in seconds for the application
REFRESH_RATE = 20

#######################
### - BG Settings - ###
#######################
#Minimum and maximum BG values for mapping the hues to
MAX_BG = 250
MIN_BG = 70
#Your target BG
TARGET_BG = 130

##########################
### - LIGHT SETTINGS - ###
##########################
#Class to group together hue values for easy use
#You can ignore this if you want
class Hues:
    red = 0
    orange = 6375
    yellow = 12750
    green = 25500
    blue = 43690
    magenta = 54615

# OUT_HUE = Color for out of range readings.
# TARGET_HUE = Color for on target readings.
#
#                  Setting to make lights go 
# RNBW_ON_TARGET = rainbow mode when you're 
#                  BG is exacly on target.
OUT_HUE = Hues.red
TARGET_HUE = Hues.orange
RNBW_ON_TARGET = True

#Brightness can be from 1-254, pretty self
#explanitory... 
BRIGHTNESS = 254

#Saturation can be from 1-254, this controls
#how 'washed out' the color is. 1 is white
#and 254 is full color
SATURATION = 254