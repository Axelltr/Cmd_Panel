#importation des modules necessaires
import os
import time
import sys
import colorama

#message d'acceuil
print("*** Welcome to terminal panel !***")
print("Select an option")

#creation des menus
mainoption = """
    [i] Ip Tools
    [s] System Tools
    [f] Fixing Tools
    [c] Clear Terminal
    [q] Quit Terminal Panel
"""

ipoption = """
    [ic] Ip Config All
    [ir] Ip Realease For DHCP
    [in] Ip Renew For DHCP
    [q] Quit Terminal Panel
    [m] Return To Terminal Panel Menu
"""

sysoption = """
    [ov] Os Version
    [si] System Info
    [ev] Environnement variables
    [q] Quit Terminal Panel
    [m] Return To Terminal Panel Menu
"""
fixoption = """"
    [cd] Check State Of Disk
    [pl] List Of Processus
    [q] Quit Terminal Panel
    [m] Return To Terminal Panel Menu
"""

#declaration des variables pour les commandes
ic = "ipconfig/all"
irl = "ipconfig/release"
irn = "ipconfig/renew"
sysinfo = "systeminfo"
osver = "ver"
clear = "cls"
varenv = "set"
check = "chkdsk"
processlist = "tasklist"

#affichage du menu principal et choix du menu adapte
print(colorama.Fore.GREEN + mainoption)
choix = input()

#conditions pour les commandes en fonction des choix pour le menu IP
if choix == "i":
    print(colorama.Fore.BLUE + ipoption)
    print("Select an option")
    choix2 = input()
    if choix2 == "ic":
        os.system(ic)
        time.sleep(10)
    if choix2 == "ir":
        os.system(irl)
        time.sleep(10)
    if choix2 == "in":
        os.system(irn)
        time.sleep(10)
    if choix2 == "q":
        quit()
    if choix2 == "m":
        print(colorama.Fore.GREEN + mainoption)
        choix = input()

#conditions pour les commandes en fonction des choix pour le menu systeme
if choix == "s":
    print(colorama.Fore.CYAN + sysoption)
    print("Select an option")
    choix3 = input()
    if choix3 == "ov":
        os.system(osver)
        time.sleep(10)
    if choix3 == "si":
        os.system(sysinfo)
        time.sleep(10)
    if choix3 == "ev":
        os.system(varenv)
        time.sleep(10)
    if choix3 == "q":
        quit()
    if choix3 == "m":
        print(colorama.Fore.GREEN + mainoption)
        choix = input()

#conditions pour les commandes en fonction des choix pour le menu fixing
if choix == "f":
    print(colorama.Fore.YELLOW + fixoption)
    print("Select an option")
    choix4 = input()
    if choix4 == "cd":
        os.system(check)
        time.sleep(10)
    if choix4 == "pl": 
        os.system(processlist)
        time.sleep(30)
        if choix4 == "q":
            quit()
        if choix4 == "m":
            print(colorama.Fore.GREEN + mainoption)
            choix = input()

#condition pour nettoyer le terminal au menu principal
if choix == "c":
    os.system(clear)
    print(colorama.Fore.GREEN + mainoption)
    choix = input()

#condition pour quitter le programme au menu principal
if choix == "q":
    quit()
        
