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
    for l in lights:
        l.on = True
        l.effect = 'none'
        l.bri = 254
        l.sat = 254

def mainLoop():
        while True:
            #Grabbing the most recent sugar
            currentBG = refreshBG()

            #Debug
            #CurrentBG =

            #Sets the lights to rainbow mode if you hit your target BG
            if currentBG == TARGET_BG and RNBW_ON_TARGET == True:
                for l in lights:
                    l.effect = 'colorloop'
        
            #if currentBG < MAX_BG and currentBG > MIN_BG and currentBG != TARGET_BG:
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

                #if HIGH_HUE > LOW_HUE:
                #    calc_hue = HIGH_HUE - ((currentBG - MIN_BG)*scaleFactor)
                #if HIGH_HUE < LOW_HUE:
                #    calc_hue = LOW_HUE - ((currentBG - MIN_BG)*scaleFactor)
                
                #for l in lights:
                #    l.effect = 'none'
                #    l.hue = calc_hue

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
            

            if currentBG >= MAX_BG or currentBG <= MIN_BG:
                for l in lights:
                    l.effect = 'none'
                    l.hue = OUT_HUE
            
            t.sleep(REFRESH_RATE)

def run():
    setup()
    mainLoop()

run()