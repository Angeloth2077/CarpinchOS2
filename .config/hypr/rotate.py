#!/usr/bin/env python
from hyprpapperRotation import variate
import argparse

activated = False

parser = argparse.ArgumentParser(description = "Activates or deactivates the program loop")
parser.add_argument('status',metavar = 'status', type = str, help = "Enter a status")
args = parser.parse_args()

status = args.status

if status == 'activate':
    activated = True
elif status == 'deactivate':
    activated = False

def run():
    variate(activated)

if __name__ == '__main__':
    run()