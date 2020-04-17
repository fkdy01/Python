#evol1
from random import randint,seed,shuffle
lcouleurs = ["R","N"] 
lvaleurs =[ (0,"2"),
            (1,"3"),
            (2,"4"),
            (3,"5"),
            (4,"6"),
            (5,"7"),
            (6,"8"),
            (7,"9"),
            (8,"10"),
            (9,"V"),
            (10,"D"),
            (11,"R"),
            (12,"A")] 
lenseignes=["C","K","P","T"] 
lenseignescouleur=[("C","R"),("K","R"),("P","N"),("T","N")]
debug=False

class Carte:
    def __init__(self, couleur, enseigne, valeurnum, valeur):
        self.couleur=couleur
        self.valeurnum=valeurnum
        self.valeur=valeur
        self.enseigne=enseigne


    
    def affiche(self):
        print(self.valeur+"(" + str(self.valeurnum) + ") de " + self.enseigne ) 

    def __str__(self):
        return self.valeur+"(" + str(self.valeurnum) + ") de " + self.enseigne

class Paquet:
    def __init__(self,type):
        self.cartes=[]
        if type=="PLEIN":
            for vn,v in lvaleurs:
                for enseigne,couleur in lenseignescouleur:
                    self.ajoute_carte(Carte(couleur,enseigne,vn,v))
    
    def ajoute_carte(self,carte):
        self.cartes.append(carte)

    def affiche(self):
        for carte in self.cartes:
           # carte.affiche()
           print(carte)

    def melange(self):
        shuffle(self.cartes)

    def vide(self):
        self.cartes=[]
        self.cartes.__sizeof__
    
    def distribue(self,p1,p2):
        p1.cartes = self.cartes[1::2] 
        p2.cartes = self.cartes[0::2]
        print()
    
    def __str__(self):
        r=""
        for carte in self.cartes:
            r=r+carte.valeur+" "+carte.enseigne+"|"
        return r


seed()
paquet=Paquet("PLEIN")
paquetj1=Paquet(None)
paquetj2=Paquet(None)
paquetjeu=Paquet(None)
paquet.melange()
paquet.distribue(paquetj1,paquetj2)
tour=1
while True:
  
    print("Joueur1:"+str(paquetj1))
    print("Joueur2:"+str(paquetj2))

    print("Joueur1:"+ str(paquetj1.cartes.__len__()) + " Joueur2:"+str(paquetj2.cartes.__len__()))
    if paquetj1.cartes.__len__()==0:
        print("Joueur 1 a perdu")
        break
    if paquetj2.cartes.__len__()==0:
        print("Joueur 2 a perdu")
        break

    cartej1 = paquetj1.cartes.pop(0)
    cartej2 = paquetj2.cartes.pop(0)

    paquetjeu.ajoute_carte(cartej1)
    paquetjeu.ajoute_carte(cartej2)
    print("tour:"+str(tour)+" Joueur1:"+ str(cartej1.valeur) + "|" + cartej1.enseigne + " Joueur2:" + str(cartej2.valeur) + "|" + cartej2.enseigne)
    if cartej1.valeurnum > cartej2.valeurnum:
        if debug:
            print("---------------------")
            print("Joueur 1 gagne")
            print("Joueur 1")
            cartej1.affiche()
            print("Joueur 2")
            cartej2.affiche()
            print("---------------------")
        paquetj1.cartes.extend(paquetjeu.cartes)
        paquetjeu.vide()
    if cartej1.valeurnum < cartej2.valeurnum:
        if debug:
            print("---------------------")
            print("Joueur 2 gagne")
            print("Joueur 1")
            cartej1.affiche()
            print("Joueur 2")
            cartej2.affiche()
            print("---------------------")
        paquetj2.cartes.extend(paquetjeu.cartes)
        paquetjeu.vide()
    if cartej1.valeurnum == cartej2.valeurnum:
        if debug:
            print("---------------------")
            print("Bataille")
            print("Joueur 1")
            cartej1.affiche()
            print("Joueur 2")
            cartej2.affiche()
            print("---------------------")
        if paquetj1.cartes.__len__() > 0 : paquetjeu.ajoute_carte(paquetj1.cartes.pop(0))
        if paquetj2.cartes.__len__() > 0 : paquetjeu.ajoute_carte(paquetj2.cartes.pop(0))
 
    tour=tour+1

        
        

