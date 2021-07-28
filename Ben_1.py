#!/usr/bin/python3.4


#for the OS command execution
import subprocess

print('=====Start to test=====')
day = input('enter the day: ')

print('=====Start to test in',day,'=====' )

subprocess.call('net show interface', shell=True)
