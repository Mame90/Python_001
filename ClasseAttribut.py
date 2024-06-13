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