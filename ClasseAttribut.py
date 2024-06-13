#coding:utf-8

class Humain:
    """
    Classe des etres humains
    """
    def __init__(self, c_prenom, c_age): # creation de constructeur
        print("creation d'un Humain")
        self.Prenom=c_prenom
        self.Age=c_age
print("Lancement du programme...")

h1= Humain('Mbaye DIop',26)
print('Prenom de h1 -> {}'.format(h1.Prenom))
print('Age de h1 -> {}'.format(h1.Age))
# print("Prenom de h1 -> {} et il a {} ans ".format(h1.prenom,h1.age))
h2 = Humain('Demba Soke',21)
print('Prenom de h2 -> {}'.format(h2.Prenom))
print('Age de h2 -> {}'.format(h2.Age))

""" Nous avons aussi ici un code beaucoup plus avancer
#coding:utf-8

class Humain:
 
 Humaine_creer =0 #initialisation de l'attribut de classe

 def __init__(self,c_prenom,c_nom,c_age):
  self.prenom=c_prenom
  self.nom=c_nom
  self.age=c_age
  Humain.Humaine_creer +=1 # incrementation de l'attribut de classe

print("lancement du programme")
h1=Humain('Mbaye','Diop',26)
print('les attributs du premiers homme est :{} {} ayant {}ans'.format(h1.prenom,h1.nom,h1.age))
print("Humaine creer est {}".format(Humain.Humaine_creer)) #affichage de l'attribut de classe
print("----------------*************-------------")
h2=Humain('Abdou','Faye',25)
print('les attributs du Deuxieme homme est :{} {} ayant {}ans'.format(h2.prenom,h2.nom,h2.age))
print("Humaine creer est {}".format(Humain.Humaine_creer))
"""