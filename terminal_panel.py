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
        exitpanel()
    if choix2 == "m":
        startpanel()

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
        exitpanel()
    if choix3 == "m":
        startpanel()

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
        print("You want to kill a process ? Yes/No")
        choix5 = input()
        if choix5 == "Yes":
            print("Enter the name of the task")
            task = input()
            os.system(killprocess + task)
            exitpanel()
    if choix4 == "pk":
        print("Enter the name of the task")
        task = input()
        os.system(killprocess + task)
    if choix4 == "q":
            exitpanel()
    if choix4 == "m":
            startpanel()

#condition pour nettoyer le terminal au menu principal
if choix == "c":
    os.system(clear)
    startpanel()

#condition pour quitter le programme au menu principal
if choix == "q":
    exitpanel()
        
