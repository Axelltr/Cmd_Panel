if choix == "n":
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
        case "cn": 
            print("enter the name of website")
            name = input()
            os.system(checksite + name)
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
