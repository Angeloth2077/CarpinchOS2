#!/usr/bin/env python
import os
import re
import subprocess

p1 = subprocess.Popen(['hyprctl', 'activewindow'], stdout = subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'workspace: '], stdin = p1.stdout, stdout = subprocess.PIPE)
p1.stdout.close()
output = subprocess.check_output(['cut', '-d', '', '-f2'], stdin = p2.stdout, text=True)
p2.stdout.close()

ws = [i for i in output if i.isdigit()]
ws.pop(1)
workspace = ''.join(ws)

os.system('hyprctl dispatch movetoworkspace \"' + workspace + ',title:Picture in picture\"')


