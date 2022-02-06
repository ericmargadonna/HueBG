# THIS PROJECT IS NO LONGER SUPPORTED
# SEE [HERE](https://help.sugarmate.io/en/articles/5793778-updated-faqs-sugarmate-and-dexcom-data-connection) FOR MORE INFORMATION
## HueBG: Visualize Glucose Readings with Philips Light Bulbs
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
First thing to do is to `git clone https://github.com/ericmargadonna/HueBG` in a repository of your choosing on a computer with python 3.7 or higher installed. You will also need to `python3 -m pip install phue` and `python3 -m pip install requests` if you haven't used either of these libraries before. 

After this you must set your *bridge's IP address* and your *sugarmate API code* in *`config.py`*.

To find your bridge IP, use either your router's administration portal or by using the Philips Hue app.

**NOTE: When running hueBG on a client for the first time, you will have to press the access button on your Philips Hue bridge**

For sugarmate, set up an account if you don't have one already. 
Log into your account and on the settings page scroll to the bottom and enable the switch for "External JSON". 
The API key is in the link given as follows:

`https://sugarmate.io/api/v1/ --- THIS IS YOUR API KEY --- /latest.json`

Once you have set the API key and IP address in `config.py` you can mess around with the colors, timings and bulb settings to your heart's content. 
Then, run `HueBG.py` or `hueBGdaemon.py` (see below) and enjoy!


## Daemon:
This can be run to have `HueBG.py` in the background, not attached to a terminal window. This is intended for raspberry pi's so that you can have, in my case, a headless Pi Zero W running this as a service. This allows you to close your ssh sesion without killing the app. This seems to work on all platforms but I've had some weird issues with the daemon library on MacOS. My raspberry pi runs the daemon perfectly on Raspberry Pi OS, and that was good enough for me. 
