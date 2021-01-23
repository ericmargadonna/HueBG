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
HUE_DIFF = abs(HIGH_HUE-LOW_HUE)

#Calculating the size of the range of values to be used
BG_RANGE = MAX_BG-MIN_BG

#Calculating the factor at which we scale the hue to the BG reading
scaleFactor = HUE_DIFF/BG_RANGE

QUIT = False

def refreshBG():
        #Using the sugarmate API to fetch the most recent BG reading
        url = 'https://sugarmate.io/api/v1/{0}/latest.json'.format(SUGARMATE_API_CODE)
        return r.get(url).json().get('value')

def setup():
    QUIT=False
    for l in lights:
        l.on = True
        l.effect = 'none'
        l.bri = 254
        l.sat = 254

def mainLoop():
        while True:
            if QUIT:
                return
            #Grabbing the most recent sugar
            currentBG = refreshBG()

            #Sets the lights to rainbow mode if you hit your target BG
            if currentBG == TARGET_BG:
                for l in lights:
                    l.effect = 'colorloop'
        
            if currentBG < MAX_BG and currentBG > MIN_BG and currentBG != TARGET_BG:
                # Okay, so becuase the hue is a wrapping uint16 value, 
                # the starting or ending hue could have a larger value.
                # Therefore we check to see which one is higher 
                # (if statements), then find the hue to apply to the 
                # lights. This is done by subtracting the lowest 
                # possible value from the current BG reading to find 
                # where the current BG reading is in our range 
                # (currentBG-MIN_BG). Then that difference is
                # multiplied by the scale factor (*scaleFactor). 
                # This product is the final hue value (calc_hue).

                if HIGH_HUE > LOW_HUE:
                    calc_hue = HIGH_HUE - ((currentBG - MIN_BG)*scaleFactor)
                if HIGH_HUE < LOW_HUE:
                    calc_hue = LOW_HUE - ((currentBG - MIN_BG)*scaleFactor)
                
                for l in lights:
                    l.effect = 'none'
                    l.hue = calc_hue

            if currentBG >= MAX_BG:
                for l in lights:
                    l.effect = 'none'
                    l.hue = HIGH_HUE
            
            if currentBG <= MIN_BG:
                for l in lights:
                    l.effect = 'none'
                    l.hue = LOW_HUE

            t.sleep(REFRESH_RATE)

def run():
    setup()
    mainLoop()

run()