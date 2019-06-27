#!/usr/bin/python

import subprocess

subprocess.call(["sudo","ifconfig","wlp3s0","down"])
subprocess.call(["sudo","ifconfig","wlp3s0","hw","ether","00:11:22:33:44:55"])
subprocess.call(["sudo","ifconfig","wlp3s0","up"])
