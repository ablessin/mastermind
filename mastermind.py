import random ##bibliotheque pour choisir chiffre aléatoire

ordi = [] # couleur choisi par l'ordi
Tabjoueur =  [] # code rentré par l'utilisateur
CouleurJoueur = ""  #texte rentré par le joueur
CouleurOrdi = 0 # couleur présente dans le code
BonEndroit = 0 # bonne couleur à la bonne place

essais = 12 #nombre d'essais disponibles
essai = 1 #essai actuel
    

while len(ordi) <4:
    ordi.append(random.choice(['J','B','R','V','O','N'])) # l'ordi choisi 4 couleurs au hasard 1 par 1(attention au maj)
    #print(ordi)


partieTerminer = False # On initialise a false pour pouvoir arreter le jeu quand il est égal a true quand la partie est terminé


#### BLOC DE JEU ####


while partieTerminer == False:
    print("essai", essai, "sur 12")
    CouleurJoueur = str(input("Entrez une combinaison de couleurs(un espace entre chaque) \n")) ##demande a l'utilisateur de saisir ses valeurs 
    Tabjoueur = CouleurJoueur.split(' ') ## transcrit la chaine de caractère du joueur en tableau dans le but de pouvoir la comparer a celui de l'ordi


    i = 0
    
    ## CHECK SI COULEUR IDENTIQUE ##
    while i < len(ordi):
        if Tabjoueur[i] == ordi[i]: ## Compare les deux cases (joueurs et ordi) dans le but de savoir si elles sont identique
            BonEndroit +=1
        i+=1
    i = 0
    
    ## CHECK COULEUR PRESENTE ##
    while i < len(CouleurJoueur):
        CouleurOrdi += ordi.count(CouleurJoueur[i])
        i+=1
    
    
    
    essai +=1 ##permet de compter le nb de tour
    
    
    
    ## INFORME LUTILISATEUR DE LA SITUATION ##
    print(BonEndroit, " pions de bonne couleur à la bonne place") 
    print(CouleurOrdi, " pions de bonne couleur")
    
    
    ## Verifie si la partie est terminé ou non ##
    if BonEndroit == 4 or essai == essais:
        partieTerminer = True
        print("Vous avez gagné !")
        print("code : ".join(ordi))
    CouleurOrdi = 0
    BonEndroit = 0
quit()

    