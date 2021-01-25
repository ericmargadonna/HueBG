#Written by Eric Margadonna
#January 21, 2021

import phue
#Thank you to https://github.com/studioimaginaire for the philips hue control library
#DOCS: https://github.com/studioimaginaire/phue

import requests as r
import time as t
from config import *

#Connects to the Philips Hue Bridge and fetches the lights as a list
b = phue.Bridge(HUE_BRIDGE_IP)
lights = b.lights

#This is the difference between the hues for high and low sugars
#25500 is the default for a green to red hue shift
HUE_DIFF = abs(TARGET_HUE-OUT_HUE)

LOW_RANGE = TARGET_BG-MIN_BG
HIGH_RANGE = MAX_BG-TARGET_BG

LOW_SCALE = HUE_DIFF/LOW_RANGE
HIGH_SCALE = HUE_DIFF/HIGH_RANGE

def refreshBG():
        #Using the sugarmate API to fetch the most recent BG reading
        url = 'https://sugarmate.io/api/v1/{0}/latest.json'.format(SUGARMATE_API_CODE)
        return r.get(url).json().get('value')

def setup():
    #Ensures that lights are on, and clears any effects
    #Then sets the brightness and saturation as defined
    #in config.py
    for l in lights:
        l.on = True
        l.effect = 'none'
        l.bri = BRIGHTNESS
        l.sat = SATURATION

def mainLoop():
        while True:
            #Grabbing the most recent sugar
            currentBG = refreshBG()

            #Debug
            #CurrentBG =

            #Sets the lights to rainbow mode if you hit your target BG
            #This can be toggled with this variable \/ in config.py
            if currentBG == TARGET_BG and RNBW_ON_TARGET == True:
                for l in lights:
                    l.effect = 'colorloop'

            #If currentBG is out of the range defined in config.py,
            #we skip any calculation and just set the bulbs to 
            #the OUT_HUE
            if currentBG >= MAX_BG or currentBG <= MIN_BG:
                for l in lights:
                    l.effect = 'none'
                    l.hue = OUT_HUE
        
            #The lines below consist of the following steps:
            #Check if currentBG is above the target and below the maximum
            #Check to see which hue has a greater numeric value, then
            #calculate the hue to set the lights to
            #Clear effects to remove the rainbow if previous BG was on target
            #Set the bulbs to the calculated hue
            if currentBG > TARGET_BG and currentBG < MAX_BG: 
                if TARGET_HUE > OUT_HUE:
                    calc_hue = TARGET_HUE - ((currentBG-TARGET_BG)*HIGH_SCALE)
                if OUT_HUE > TARGET_HUE:
                    calc_hue = OUT_HUE + ((currentBG-TARGET_BG)*HIGH_SCALE)
                for l in lights:
                    l.effect = 'none'
                    l.hue = calc_hue           
            if currentBG < TARGET_BG and currentBG > MIN_BG:
                if TARGET_HUE > OUT_HUE:
                    calc_hue = TARGET_HUE - ((TARGET_BG-currentBG)*LOW_SCALE)
                if OUT_HUE > TARGET_HUE:
                    calc_hue = OUT_HUE + ((TARGET_BG-currentBG)*LOW_SCALE)
                for l in lights:
                    l.effect = 'none'
                    l.hue = calc_hue
            
            #Rest, you've worked hard
            t.sleep(REFRESH_RATE)

#Running the app
def run():
    setup()
    mainLoop()
run()