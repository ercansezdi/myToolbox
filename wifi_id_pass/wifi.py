from tkinter import *
import pyperclip
import subprocess

class wifi_passwd:
    def see_wifi_pass():
        id_pass = [[],[]]
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode(
                'utf-8').split(
                '\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                id_pass[0].append(i)
                id_pass[1].append(results[0])
            except IndexError:
                id_pass[0].append(i)
        return id_pass
