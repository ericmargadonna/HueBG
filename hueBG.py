#Written by Eric Margadonna
#January 21, 2021

import phue
#Thank you to https://github.com/studioimaginaire for the philips hue control library
#DOCS: https://github.com/studioimaginaire/phue

import requests as r
import time as t
from config import *


class hueBG:
    def __init__(self,key,ip_addr,target_bg,min_bg,max_bg,target_hue,out_hue,rainbow_on_target,refresh_rate):
        self.key = key

        self.min_bg = min_bg
        self.max_bg = max_bg
        self.target_bg = target_bg

        self.target_hue = target_hue
        self.out_hue = out_hue

        self.rainbow_on_target=rainbow_on_target
        self.refresh_rate = refresh_rate

        self.low_range = self.target_bg-self.min_bg
        self.high_range = self.max_bg-self.target_bg

        #This is the difference between the hues for high and low sugars
        #25500 is the default for a green to red hue shift
        self.hue_diff = abs(self.target_hue-self.out_hue)

        self.low_scale = self.hue_diff/self.low_range
        self.high_scale = self.hue_diff/self.high_range

        #Connects to the Philips Hue Bridge and fetches the 
        #lights as a list and ensures that lights are on, 
        #clears any effects, then sets the brightness and 
        #saturation as defined in config.py
        
        self.bridge = phue.Bridge(ip_addr)
        self.lights = self.bridge.lights
        for l in self.lights:
            l.on = True
            l.effect = 'none'
            l.bri = BRIGHTNESS
            l.sat = SATURATION

    def getBG(self, key):
            #Using the sugarmate API to fetch the most recent BG reading
            try:
                url = 'https://sugarmate.io/api/v1/{0}/latest.json'.format(key)
                return r.get(url).json().get('value')
            #If for some reason there's an issue, just tell the user and
            #try again.
            except Exception:
                print(Exception)
                print('Retrying')
                return getBG()
        
    def updateLights(self, BG):
        #Sets the lights to rainbow mode if you hit your target BG
        #and the effect is enabled in config.py
        if BG == self.target_bg:
            if self.rainbow_on_target == True:
                for l in self.lights:
                    l.effect = 'colorloop'
            else:
                for l in self.lights:
                    l.hue = self.target_hue

        #If BG is out of the range defined in config.py,
        #we skip any calculation and just set the bulbs to 
        #the OUT_HUE
        if BG >= self.max_bg or BG <= self.min_bg:
            for l in self.lights:
                l.effect = 'none'
                l.hue = self.out_hue

        #The lines below consist of the following steps:
        #Check if BG is above the target or below the maximum and
        #Check to see which hue has a greater numeric value, then
        #calculate the hue to set the lights to and set them
        if BG > self.target_bg and BG < self.max_bg: 

            if self.target_hue > self.out_hue:
                calc_hue = self.target_hue - ((BG-self.target_bg)*self.high_scale)
            if self.out_hue > self.target_hue:
                calc_hue = self.target_hue + ((BG-self.target_bg)*self.high_scale)

            for l in self.lights:
                l.effect = 'none'
                l.hue = calc_hue           

        if BG < self.target_bg and BG > self.min_bg:

            if self.target_hue > self.out_hue:
                calc_hue = self.target_hue - ((self.target_bg-BG)*self.low_scale)
            if self.out_hue > self.target_hue:
                calc_hue = self.target_hue + ((self.target_bg-BG)*self.low_scale)

            for l in self.lights:
                l.effect = 'none'
                l.hue = calc_hue
        
        #Rest, you've worked hard
        t.sleep(self.refresh_rate)

    def run(self):
        while True:
            self.updateLights(self.getBG(self.key))

def main():
    app = hueBG(SUGARMATE_API_CODE,HUE_BRIDGE_IP,TARGET_BG,MIN_BG,MAX_BG,TARGET_HUE,OUT_HUE,RNBW_ON_TARGET,REFRESH_RATE)
    app.run()

if __name__ == '__main__':
    main()