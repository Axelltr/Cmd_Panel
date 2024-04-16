#importation des modules necessaires
import os
import time
import sys
import colorama

#message d'acceuil
print(colorama.Fore.RED + "*** Welcome to terminal panel !***")
print(colorama.Fore.RED + "Select an option")

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
    [pk] Kill Processus By Name
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
killprocess = "taskkill /IM "

#fonction pour quitter le programme
def exitpanel():
    print("Bye Bye !")
    time.sleep(3)
    quit()

#fonction pour afficher le menu principal
def startpanel():
    print(colorama.Fore.GREEN + mainoption)
    global choix
    choix = input()

#affichage du menu principal et choix du menu adapte
startpanel()

#conditions pour les commandes en fonction des choix pour le menu IP
if choix == "i":
    print(colorama.Fore.BLUE + ipoption)
    print("Select an option")
    choix2 = input()
    match choix2:
        case "ic":
            os.system(ic)
            time.sleep(10)
        case "ir":
            os.system(irl)
            time.sleep(10)
        case "in":
            os.system(irn)
            time.sleep(10)
        case "q":
            exitpanel()
        case "m":
            startpanel()

#conditions pour les commandes en fonction des choix pour le menu systeme
if choix == "s":
    print(colorama.Fore.CYAN + sysoption)
    print("Select an option")
    choix3 = input()
    match choix3:
        case "ov":
            os.system(osver)
            time.sleep(10)
        case "si":
            os.system(sysinfo)
            time.sleep(10)
        case "ev":
            os.system(varenv)
            time.sleep(10)
        case "q":
            exitpanel()
        case "m":
            startpanel

#conditions pour les commandes en fonction des choix pour le menu fixing
if choix == "f":
    print(colorama.Fore.YELLOW + fixoption)
    print("Select an option")
    choix4 = input()
    match choix4:
        case "cd":
            os.system(check)
            time.sleep(10)
        case "pl":
            os.system(processlist)
            print("You want to kill a process ? Yes/No")
            choix5 = input()
            if choix5 == "Yes":
                print("Enter the name of the task")
                task = input()
                os.system(killprocess + task)
                exitpanel()
        case "pk":
            print("Enter the name of the task")
            task = input()
            os.system(killprocess + task) 
        case "q":
            exitpanel()
        case "m":
            startpanel()

#condition pour nettoyer le terminal au menu principal
if choix == "c":
    os.system(clear)
    startpanel()

#condition pour quitter le programme au menu principal
if choix == "q":
    exitpanel()
        
