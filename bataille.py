from random import randint,seed
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
        print(self.valeur+"(" + str(self.valeurnum) + ") de " + self.enseigne + " de couleur " + self.couleur ) 

    def __str__(self):
        return self.valeur+"(" + str(self.valeurnum) + ") de " + self.enseigne + " de couleur " + self.couleur

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
        for i in range(500):
            i1=randint(0,len(self.cartes)-1)
            i2=randint(0,len(self.cartes)-1)
            self.switch(i1,i2)
        
seed()
paquet=Paquet("PLEIN")
paquet.melange()
paquet.affiche()

