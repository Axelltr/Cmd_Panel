#fonction pour quitter le programme
def exitpanel():
    print(colorama.Fore.WHITE + "Bye Bye !")
    time.sleep(3)
    quit()

#fonction pour afficher le menu principal
def startpanel():
    print(colorama.Fore.RED + "*** Welcome to terminal panel !***")
    print(colorama.Fore.RED + "Select an option")
    print(colorama.Fore.GREEN + mainoption)
    global choix
    choix = input()
