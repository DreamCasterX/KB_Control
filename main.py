from je_auto_control import keyboard_keys_table, get_special_table
from time import sleep
from je_auto_control import press_keyboard_key, release_keyboard_key
from je_auto_control import type_keyboard
from je_auto_control import check_key_is_press
from je_auto_control import write
import sys
from je_auto_control import hotkey
from je_auto_control import screenshot
from je_auto_control import mouse_keys_table, special_mouse_keys_table
from je_auto_control import press_mouse, release_mouse
from je_auto_control import click_mouse
from je_auto_control import get_mouse_position, set_mouse_position
from je_auto_control import mouse_scroll

# Online document: https://autocontrol.readthedocs.io/en/latest/Zh/doc/keyboard/keyboard_doc.html
# pip install je_auto_control


# 查詢所有特殊按鍵對應的值
# print(keyboard_keys_table)
# print(get_special_table())  # 不是每個平台都有


# # 完成一次單點按鍵的動作
# type_keyboard("tab")


# # 連續hold住指定按鍵, 並給予時間放開
# press_keyboard_key("a")
# sleep(2)
# release_keyboard_key("a")


# # 輸入一長串連續的指定按鍵
# write("mikeyouaresogood")


# # 使用熱鍵，會按下傳入的按鍵並相反的放開
# if sys.platform in ["win32", "cygwin", "msys"]:
#     hotkey(["lcontrol", "a", "lcontrol", "c", "lcontrol", "v", "lcontrol", "v"])
#
# elif sys.platform in ["darwin"]:
#     hotkey(["command", "a", "command", "c", "command", "v", "command", "v"])
#
# elif sys.platform in ["linux", "linux2"]:
#     hotkey(["ctrl", "a", "ctrl", "c", "ctrl", "v", "ctrl", "v"])


# # 查詢所有滑鼠可以使用的按鍵
# print(mouse_keys_table)
# print(special_mouse_keys_table)


# # 按著滑鼠，一秒後釋放滑鼠
# press_mouse("mouse_right")
# sleep(1)
# release_mouse("mouse_right")


# # 完成一次單點滑鼠的動作
# click_mouse("mouse_right")


# # 檢查滑鼠位置並改變滑鼠位置
# print(get_mouse_position())
# set_mouse_position(100, 100)


# # 3秒後滑鼠會往上 scroll
# sleep(3)
# mouse_scroll(4)


# # 螢幕截圖
# screenshot()


input()