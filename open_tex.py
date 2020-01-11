#!/usr/bin/env python3
"""
A script to open a tex file in i3
- Opens the corresponding pdf
- Opens a terminal to watch the file
- Opens the tex file in vim
"""
import sys
import tempfile
import os
from subprocess import call
from i3ipc import Connection, Event
import argparse
import subprocess
import time

parser = argparse.ArgumentParser(description='Tex file opener')

parser.add_argument('file', metavar='NAME', help='Latex file name to open')


args = parser.parse_args()
i3 = Connection()
i3.command('workspace 1')
i3.command('split h')
time.sleep(0.2)
subprocess.Popen(["alacritty", "--working-directory="+os.getcwd(), "-e", "zsh", "-i", "-c","nvim "+ args.file+".tex"])
# subprocess.Popen(["alacritty", "--working-directory="+os.getcwd(), "-e", "/usr/bin/nvim", args.file+".tex"])
time.sleep(0.2)
subprocess.Popen(["zathura", args.file+".pdf"])
time.sleep(0.2)
i3.command('focus right, focus right, split v')
time.sleep(0.2)
subprocess.Popen(["alacritty", "--working-directory="+os.getcwd(), "-e", "zsh", "-i", "-c","ls *.tex | entr -s 'latexmk -pdf' "])
i3.command('focus down')
time.sleep(0.2)
i3.command('resize shrink height 40 px or 40 ppt')
i3.command('focus left')
