#!/usr/bin/env python
import time as t
import os
import subprocess

wallpapwer_list = os.listdir('./Wallpapers')
wait_time = 60
preload_str = 'preload = /home/angel/.config/hypr/Wallpapers/'
wallpapwer_str = '\nwallpaper = HDMI-A-1, /home/angel/.config/hypr/Wallpapers/'


def variate():
    for img in wallpapwer_list:
        with open('./hyprpaper.conf', 'w') as w:
            w.write(preload_str + str(img) + wallpapwer_str + str(img))
        os.system('hyprpaper & disown')
        t.sleep(wait_time)


if  __name__ == '__main__':
    variate()