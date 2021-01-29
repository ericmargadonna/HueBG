# HueBG: Visualize Glucose Readings with Philips Light Bulbs
 ### A python program to control Philips Hue lightbulbs based on   Continous Glucose Monitor (CGM) readings fetched from [sugarmate.io](https://sugarmate.io)

## Supplies:
- CGM linked to sugarmate
- Philips Hue bridge and bulbs
- A computer (duh)

## Usage:
First thing you must do in order to run hueBG is set your bridge's IP address and your sugarmate API code in `config.py`

To find your bridge IP, use either your router's administration portal or through the Philips Hue app.

_NOTE: When running hueBG for the first time, you will have to press the button on your Philips Hue bridge at most 30 seconds before_ 

For sugarmate, set up an account if you don't have one already. Then, on the settings page scroll to the bottom and enable "External JSON". The code is in the link given as follows:
`https://sugarmate.io/api/v1/ YOUR CODE /latest.json`

## Daemon:
The astute among you may have already noticed the `hueBGdaemon.py` file. This is can be run to have HueBG in the background, not attached to a particular terminal window. This is intended for raspberry pi's so that you can have, for example, a headless Pi Zero W running this as a service. This allows you to close your ssh sesion without killing the app. This is quite finnicky however and has caused me issues on macOS.