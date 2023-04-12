#!/usr/bin/env python
import time as t
import os
import subprocess

wallpaper_list = os.listdir('/home/angel/.config/hypr/Wallpapers')
wait_time = 60
path = '/home/angel/.config/hypr/Wallpapers/'
preload_str = 'preload = ' + path
wallpaper_str = '\nwallpaper = HDMI-A-1, ' + path

def variate(activated):
    while True:
        if activated == True:
            for img in wallpaper_list:
                with open('/home/angel/.config/hypr/hyprpaper.conf', 'w') as w:
                    w.write(preload_str + img + wallpaper_str + img)
                os.system('hyprpaper & disown')
                os.system('hyprctl hyprpaper unload '+ path + img)
                t.sleep(wait_time)
                os.system('killall hyprpaper')
        elif activated == False: break

if __name__ == '__main__':
    variate()