#!/usr/bin/env python3

import sys
import os
from os.path import expanduser
home = os.path.expanduser("~")
if os.path.isdir(home + "/.local/lib/python3.10/site-packages/je_auto_control") == False:
	os.system("sudo apt install python3-pip -y && pip install je_auto_control")

from time import sleep
from pprint import pprint
from je_auto_control import keyboard_keys_table
from je_auto_control import type_keyboard


# Check KB table
# pprint(keyboard_keys_table)


# Press Super key & type hp.com
n = 0
cycles = input("Test cycles: ")
os.system("touch ~/Desktop/KB_Test.txt && open ~/Desktop/KB_Test.txt")
while True: 
    if n < int(cycles):
        sleep(1)
        type_keyboard("win")
        sleep(1.5)
        type_keyboard("win")
        sleep(1.5)
        type_keyboard("h")
        sleep(0.5)
        type_keyboard("p")
        sleep(0.5)
        type_keyboard("decimal")
        sleep(0.5)
        type_keyboard("c")
        sleep(0.5)
        type_keyboard("o")
        sleep(0.5)
        type_keyboard("m")
        sleep(0.5)
        type_keyboard("return")
        sleep(1)
        n += 1
    else:
        break
print("\n***Test finished***\n")


