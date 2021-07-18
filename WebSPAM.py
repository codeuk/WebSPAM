#you may expand on this, but please give credit :P

import time
import sys
import os
import colorama
from colorama import Fore
import requests
import threading

#functions
def anim():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'{Fore.CYAN}[>] Loading Spammer {Fore.RESET}'+i)
        sys.stdout.flush()
        time.sleep(0.2)

def anim2():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'{Fore.RED}[x] No Webhook Specified, Exiting {Fore.RESET}'+i)
        sys.stdout.flush()
        time.sleep(0.2)

def anim3():
    l = ['|', '/', '-', '\\']
    for i in l+l+l:
        sys.stdout.write('\r' + f'{Fore.GREEN}[>] Starting Spam {Fore.RESET}'+i)
        sys.stdout.flush()
        time.sleep(0.2)

#setting up
os.system('cls')
anim()
os.system("title [SPAMMER!]")
os.system('cls')
defaulthookname = 'Webhook Spammer!'
defaultmessage = 'You have been spammed! :scream: '

print(f"""{Fore.RED}

    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ ██╗
    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗██║
    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝██║
    ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗╚═╝
    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║██╗
    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝

{Fore.RESET}""")

def send(webhook, message, username):
    data = {
        'content': message,
        'username': hookname
    }
    try:
        print(" ")
        while True:
            requests.post(webhook, data=data)
            print(f'{Fore.CYAN}[>]{Fore.RESET} Message Sent! {Fore.GREEN}[SUCCESS]{Fore.RESET}')
    except KeyboardInterrupt: 
        exit()


webhook = input(f'{Fore.GREEN}[>]{Fore.RESET} Please Enter Your Webhook Link: {Fore.RESET}')
if webhook == '': 
	print(" ")
	anim2()
	print(" ")
	os.system('cls')
	exit()
print(" ")

hookname = input(f'{Fore.GREEN}[>]{Fore.RESET} What would you like the username to be?: {Fore.RESET}')
if hookname == '': 
    hookname = defaulthookname
    print(" ")
    print(f'{Fore.RED}[x]{Fore.RESET} Set to Default Username.{Fore.RESET}')

print(" ")
message = input(f'{Fore.GREEN}[>]{Fore.RESET} Enter your message: {Fore.RESET}')
if message == '': 
    message = defaultmessage
    print(" ")
    print(f'{Fore.RED}[x]{Fore.RESET} Set to Default Message')

try:
    print(" ")
    threads = int(input(f'{Fore.GREEN}[>]{Fore.RESET} How many threads would you like to run?: {Fore.RESET}'))
    if threads < 1: 
        print(" ")
        print(f'{Fore.RED}[x]{Fore.RESET} Negative or No threads, Setting Threads to 1.{Fore.RESET}')
        threads = 1

except ValueError:
    threads = 1
    print(" ")
    print(f'{Fore.RED}[x] Invalid threads / Setting to 1.{Fore.RESET}')

print(" ")
print(f'{Fore.CYAN}[>] Starting Spam.{Fore.RESET}')

for x in range(threads):
    thread = threading.Thread(
        target=send(webhook, message, hookname), args=(1,))
    thread.start()
print(f'{Fore.RED}[]')

#created by doop#0001 / github.com/@7uk
