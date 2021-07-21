# HueBG: Visualize Glucose Readings with Philips Light Bulbs
 ### A python program to control Philips Hue lightbulbs based on Continous Glucose Monitor (CGM) readings fetched from [sugarmate.io](https://sugarmate.io)

This is a fun project I created in order to more passively keep track of my blood glucose readings without having to pick up my phone or checking my insulin pump. It also looks pretty cool and has an optional rainbow mode for when your reading is perfectly on your set target.

## Libraries Used:
[Requests](https://docs.python-requests.org/en/master/)

[phue](https://github.com/studioimaginaire/phue)

## Supplies:
- CGM linked to sugarmate
- Philips Hue bridge and bulbs
- A computer with python 3.7+

## Usage:
First thing you must do in order to run hueBG is set your bridge's IP address and your _sugarmate API code_ in `config.py`

To find your bridge IP, use either your router's administration portal or through the Philips Hue app.

_NOTE: When running hueBG for the first time, you will have to press the button on your Philips Hue bridge _ 

For sugarmate, set up an account if you don't have one already. 
Then, on the settings page scroll to the bottom and enable "External JSON". 
The API key is in the link given as follows:
`https://sugarmate.io/api/v1/ --- YOUR API KEY --- /latest.json`

## Daemon:
This can be run to have HueBG in the background, not attached to a terminal window. This is intended for raspberry pi's so that you can have, in my case, a headless Pi Zero W running this as a service. This allows you to close your ssh sesion without killing the app.
