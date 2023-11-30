dico_histo = {"calcul": []} #Dico initialisé

def recommencer():
    restart = input("Voulez-vous faire un nouveau calcul (y/n) : ")
    if restart.lower() == 'y':
        main() #Recommence un nouveau calcul
    elif restart.lower() == 'n':
        return #Sort du programme
    else:
        print("Veuillez choisir entre 'y' ou 'n' pour continuer.")
        recommencer() #Relance le programme

def historique():
    review = input("Voulez vous observer vos précédents calculs (y/n) : ")

    if review.lower() == 'y':
        print("Votre historique :")
        #Chaque fois qu'il y a un élément dans le dico[calcul], print élément 1 puis élément 2,..
        for element in dico_histo["calcul"]:
            print(f"{element[0]} {element[1]} {element[2]} = {element[3]}")
        print() #Revient à la ligne
        eraser() #Lance la fonction effaceur historique

    elif review.lower() == 'n':
        pass #Ignore regarder l'historique
    else:
        print("Veuillez choisir entre 'y' ou 'n' pour continuer.")
        historique() #Relance le programme

def eraser():
    effacer=input("Voulez vous supprimer votre historique (y/n) :")
    if effacer.lower() == 'y':
        dico_histo["calcul"].clear() #On clear le dictionnaire
        print("Votre historique :\n") #On print un (fake) dictionnaire
        return 
    elif effacer.lower() == 'n':
        return #On sort de l'effaceur et on va vers la fonction 'recommencer'
    else:
        print("Veuillez choisir entre 'y' ou 'n' pour continuer.")
        eraser() #Relance le programme    

def calcul():
    # Mes Inputs
    try:
        chiffre1 = float(input('Entrez votre premier chiffre : '))
        operator = str(input("Entrez l'opérateur : "))
        chiffre2 = float(input("Entrez votre second chiffre : "))
    except ValueError:
        print("Veuillez entrer uniquement des chiffres.")
        main() #relance le programme
    #Mes Calcules
    if operator=='+': 
        resultat= chiffre1 + chiffre2
    elif operator=='-':
        resultat= chiffre1 - chiffre2
    elif operator=='*':
        resultat= chiffre1 * chiffre2
    elif operator=='/':
        #Divisions par 0
        if chiffre2 != 0: # ! = différent
            resultat= chiffre1 / chiffre2
        else:
            print("Désolé... Nous ne pouvons pas diviser par zéro")
            main() 
    elif operator == '%':
        resultat= chiffre1 % chiffre2
    else:
        print("Erreur : Opérateur non valide.")
        main()

    #Résultat
    print(f"Le résultat de votre calcul est {resultat}")

    #Ajoute le calcul à l'historique
    dico_histo["calcul"].append((chiffre1, operator, chiffre2, resultat))

def main():
    #Lance la calculatrice
    calcul()

    #Voir l'historique
    historique()

    #Recommencer un calcul
    recommencer()


main()