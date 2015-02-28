#!/usr/bin/python
# This python script allows you to operate the LCD over the CLI
#
# Installation:
# Change the path to point to where you put the Adafruit_Python_CharLCD library on your system
# echo "alias lcd='sudo python /home/pi/dev/python/Adafruit_Python_CharLCD/examples/lcd_cli.py'" >> ~/.bashrc
#
# Note that when using this script from within a program, this alias probably won't work and you'll need to specify the full
# path of the python script (eg `sudo python path/to/examples/lcd_cli.py --on`)
#
# cmds:
# python lcd_cli.py --install-alias  # installs alias `lcd`
# . ~/.bashrc                        # run if needed to activates alias in shell
# lcd --on                           # turns the lcd backlight on
# lcd --off                          # turns the lcd backlight off
# lcd hello world                    # prints hello to the lcd screen
# lcd "hello world"                  # prints hello to the lcd screen

import sys
import Adafruit_CharLCD as LCD

lcd_dimensions = [16,2]  # for 16x2 LCD displays

my_arg = ""
if len(sys.argv) > 1:
  my_arg = ' '.join(sys.argv[1:])

if my_arg == "--install-alias":
  import inspect, os
  script_path = os.path.abspath( inspect.getfile(inspect.currentframe()) )
  bashrc_path = os.path.expanduser("/home/pi/.bashrc")
  alias_cmd = "alias lcd='sudo python " + script_path + "'"
  cmd = 'echo "' + alias_cmd + '" >> ' + bashrc_path
  os.system(cmd)
  print("An alias has been dropped into ~/.bashrc, run `. ~/.bashrc` or reload terminal")
  exit()

# Fit the words onto the display if possible...
# This is primitive and won't have any way of showing
# strings longer than the dimensions available on the LCD.
# A proper daemon should be designed to handle 
# input rather than a simple script like this.
if len(my_arg) > 16:
  my_arg = my_arg[0:lcd_dimensions[0]-1] + "\n" + my_arg[lcd_dimensions[0]-1:]

# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()
if my_arg == "--on":
  lcd.set_color(1.0,1.0,1.0)
elif my_arg == "--off":
  lcd.set_color(0.0,0.0,0.0)
else:
  lcd.set_color(1.0, 1.0, 1.0)
  lcd.message(my_arg)

