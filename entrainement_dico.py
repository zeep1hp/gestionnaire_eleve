import json

    

def save():
    with open("eleve.json", "w") as f:
        json.dump(eleves, f)

def load():
    with open("eleve.json", "r") as f:
        eleves = json.load(f)
        f.close()
        return eleves

eleves = load()

def demande():
    while True:
        x = input("==>")
        if x.isdigit():
            break
        print("entrez un choix valide") 
    x = int(x)
    return x

def retour_menu():

    solution = [1,2]
    entry = 0

    while entry not in solution:

        print("[1] MENU [2] FERMER")
        entry = demande()
        if entry == 1:
            save()
            break
        elif entry == 2:
            save()
            return False


def visionnez_liste_eleves():

    # a pofiné
    print(eleves)
    
    retour = retour_menu()
    if retour is False:
        return False
        

def ajoutez_eleve():
   
    prop=[1,2]
    
    a_nom = input("entrez le nom de l'élèves \n==>")
    eleves[a_nom] = {
        'note' : None,
        'appreciation' : None
    }
    a_note = 0
    while a_note not in prop:
        print("veut tu ajoutez une note ?\n[1] oui, [2] non")
        a_note = demande()
        if a_note ==1:
            print("entre une note")
            a_note = demande()
            
            eleves[a_nom]['note'] = a_note
            break
        elif a_note == 2:
            break

    a_appreciation = 0
    while a_appreciation not in prop:
        print("veut tu ajoutez une appreciation ? \n[1] oui, [2] non")
        a_appreciation = demande()
        if a_appreciation == 1:
            a_appreciation = input("entre une appreciation\n==>")
            eleves[a_nom]['appreciation']= a_appreciation
            break
        elif a_appreciation == 2:
            break
    
    retour = retour_menu()
    if retour is False:
        return False


def modifier_eleves():

    prop=[1,2]
    nom_eleves = input("entre le nom de l'eleves\n==>")
    if nom_eleves in eleves.keys():
        choix_modif = 0
        while choix_modif not in prop:
            print("[1] note, [2] appreciation")
            choix_modif = demande()
            
            if choix_modif == 1:
                print("entre la nouvel note")
                modif_note = demande()
                
                eleves[nom_eleves]['note'] = modif_note
            elif choix_modif == 2:
                modif_appre = input("entre un nouvel appreciation\n==>")
                eleves[nom_eleves]['appreciation'] = modif_appre
    
    retour = retour_menu()
    if retour is False:
        return False

def affichez_un_eleve():
    choix_eleve = input("choisie l'eleve que tu veut consulter\n==>")
    for eleve in eleves:
        if choix_eleve in eleves.keys():
            print(f"nom eleve : {choix_eleve}\nnote : {eleves[choix_eleve]['note']}\nappreciation : {eleves[choix_eleve]['appreciation']}")
        else:
            print(f"l'eleve : {choix_eleve} n'est pas référencé")
        
        retour = retour_menu()
        if retour is False:
            return False

def supprimez_un_eleve():
    x = input("quel eleves souhaite tu supprimez ?\n==>")
    if x in eleves.keys():
        del eleves[x]
        print(f"{x} a bien était supprimez")
    else:
        print(f"{x} n'est pas referencé impossible a supprimé")

    retour = retour_menu()
    if retour is False:
        return False

def moyenne_classe():
    somme_notes = 0
    nb_eleves = len(eleves)
    for eleve in eleves.values():
        somme_notes += eleve['note']
    x = somme_notes / nb_eleves
    print(f"la moyenne de la classe est de : {x}")

    retour = retour_menu()
    if retour is False:
        return False

def menu():
    g = True
    while g:
        
        print("********")
        print("*      *")
        print("* MENU *")
        print("*      *")
        print("********")
        prop=[1,2,3,4,5,6]
        x = 0

        while x not in prop:
            print("Que veut tu faire ?\n[1] liste tout les eleves\n[2] ajouté un eleves\n[3] modifier eleves\n[4] afficher un eleve\n[5] supprimez un eleve\n[6] afficher la moyenne de la classe\n[7] quittez")
            x = demande()
            
            if x == 1:
                y = visionnez_liste_eleves()
                if y is False:
                    g=False
                    save()
                    break

            elif x == 2:
                y = ajoutez_eleve()
                if y is False:
                    g=False
                    save()
                    break
            
            elif x ==3:
                y = modifier_eleves()
                if y is False:
                    g=False
                    save()
                    break

            elif x == 4:
                y = affichez_un_eleve()
                if y is False:
                    g=False
                    save()
                    break
            
            elif x == 5:
                y = supprimez_un_eleve()
                if y is False:
                    g=False
                    save()
                    break
            
            elif x == 6:
                y = moyenne_classe()
                if y is False:
                    g=False
                    save()
                    break

            elif x == 7:

                g=False
                break


menu()

