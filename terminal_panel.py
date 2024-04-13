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
        
