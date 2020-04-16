#evol1
from random import randint,seed,shuffle
lcouleurs = ["ROUGE","NOIR"] 
lvaleurs =[ (0,"2"),
            (1,"3"),
            (2,"4"),
            (3,"5"),
            (4,"6"),
            (5,"7"),
            (6,"8"),
            (7,"9"),
            (8,"10"),
            (9,"VALET"),
            (10,"DAME"),
            (11,"ROI"),
            (12,"AS")] 
lenseignes=["COEUR","CARREAU","PIQUE","TREFLE"] 
lenseignescouleur=[("COEUR","ROUGE"),("CARREAU","ROUGE"),("PIQUE","NOIR"),("TREFLE","NOIR")]

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

    def switch(self,index1,index2):
        carte = self.cartes[index1]
        self.cartes[index1]=self.cartes[index2]
        self.cartes[index2]=carte

    def melange(self):
        shuffle(self.cartes)

    def prend_carte(self):
        return 
    
    def distribue(self,p1,p2):
        # tour=1
        # for carte in self.cartes:
        #     if tour==1 :
        #         p1.ajoute_carte(self.cartes.pop())
        #         tour=2
        #     else :
        #         p2.ajoute_carte(self.cartes.pop())
        #         tour=1
        # print()
        p1.cartes = self.cartes[1::2] 
        p2.cartes = self.cartes[0::2]
        print()
#
# def copie_paquet(self,paquet_source,paquet_cible):
#      paquet_cible.cartes =+ paquet_source.cartes

seed()
paquet=Paquet("PLEIN")
paquetj1=Paquet(None)
paquetj2=Paquet(None)
paquetjeu=Paquet(None)
paquet.melange()
paquet.distribue(paquetj1,paquetj2)

while True:
    cartej1 = paquetj1.cartes.pop()
    if cartej1 == None :
        print("Joueur 1 a perdu")
        break
    cartej2 = paquetj2.cartes.pop()
        print("Joueur 2 a perdu")
        break

    paquetjeu.ajoute_carte(cartej1)
    paquetjeu.ajoute_carte(cartej2)
    if cartej1.valeurnum > cartej2.valeurnum:
        print("---------------------")
        print("Joueur 1 gagne")
        print("Joueur 1")
        cartej1.affiche()
        print("Joueur 2")
        cartej2.affiche()
        print("---------------------")
        paquetj1.cartes+=paquetjeu.cartes
        paquetjeu=None
    if cartej1.valeurnum < cartej2.valeurnum:
        print("---------------------")
        print("Joueur 2 gagne")
        print("Joueur 1")
        cartej1.affiche()
        print("Joueur 2")
        cartej2.affiche()
        print("---------------------")
        paquetj2.cartes+=paquetjeu.cartes    
        paquetjeu=None
    if cartej1.valeurnum == cartej2.valeurnum:
        print("---------------------")
        print("Bataille")
        print("Joueur 1")
        cartej1.affiche()
        print("Joueur 2")
        cartej2.affiche()
        print("---------------------")

        
        

