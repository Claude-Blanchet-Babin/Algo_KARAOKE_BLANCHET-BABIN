# contrôle prog et algo

# exercice A

# question 1

# voir l'image en pièce jointe

# question 2

# construction de la classe Player

class Player :
    def __init__(self,name,score1,score2,score3,score4,score5):
        self.__nom = name
        self.__point1 = score1
        self.__point2 = score2
        self.__point3 = score3
        self.__point4 = score4
        self.__point5 = score5

    def getNom(self):
        return self.__nom

    def getPoint1 (self):
        return self.__point1

    def getPoint2 (self):
        return self.__point2

    def getPoint3 (self):
        return self.__point3

    def getPoint4 (self):
        return self.__point4

    def getPoint5 (self):
        return self.__point5

    # question 3

    # ajout des méthodes de la classe Player

    def getMoyenne (self):
        moyenne = (self.__point1 + self.__point2 + self.__point3 + self.__point4 +self.__point5) / 5
        print ("La moyenne de " + self.__nom + " est de " + str(moyenne))

    def getTotal (self):
        total = self.__point1 + self.__point2 + self.__point3 + self.__point4 +self.__point5
        print ("Le total de " + self.__nom + " est de " + str(total))

    def getMeilleur (self):
        listescore = [self.__point1,self.__point2,self.__point3,self.__point4,self.__point5]
        meilleur = 0
        indicemeilleur = 0

        for i in range (0,len(listescore)):

            if (listescore[i] > meilleur):
                meilleur = listescore[i]
                indicemeilleur = i + 1

        print ("Le meilleur score de " + self.__nom + " est de " + str(meilleur) + "et il s'agit de la chanson numéro " + str(indicemeilleur))


    def getPire (self):
        listescore = [self.__point1,self.__point2,self.__point3,self.__point4,self.__point5]
        pire = 100
        indicepire = 0

        for i in range (0,len(listescore)):

            if (listescore[i] < pire):
                pire = listescore[i]
                indicepire = i + 1

        print ("Le pire score de " + self.__nom + " est de " + str(pire) + "et il s'agit de la chanson numéro " + str(indicepire))

    def getAfficher (self):
        print ("Voici la liste des scores")
        print ("Musique 1 : " + str(self.__point1))
        print ("Musique 2 : " + str(self.__point2))
        print ("Musique 3 : " + str(self.__point3))
        print ("Musique 4 : " + str(self.__point4))
        print ("Musique 5 : " + str(self.__point5))

    def getAjouter (self,numeroscore,newscore):

        # il faut d'abord vérifier quel est la position du score que l'on veut ajouter
        # il faut d'abord vérifier si le nouveau score est supérieur à l'ancien score enregistré

        if (numeroscore == 1):
            if (newscore > self.__point1):
                self.__point1 = newscore

        if (numeroscore == 2):
            if (newscore > self.__point2):
                self.__point2 = newscore

        if (numeroscore == 3):
            if (newscore > self.__point3):
                self.__point3 = newscore

        if (numeroscore == 4):
            if (newscore > self.__point4):
                self.__point4 = newscore

        if (numeroscore == 5):
            if (newscore > self.__point5):
                self.__point5 = newscore


# question 4

# début du programme principal
# création de deux objets joueurs à partir de la classe Player

Joueur1 = Player("Michel",60,70,80,90,100)
Joueur2 = Player("Paul",50,75,85,100,100)

# faire des tests en appelant les méthodes

Joueur1.getMoyenne()
Joueur2.getTotal()

Joueur1.getMeilleur()
Joueur2.getPire()

Joueur1.getAfficher()
Joueur2.getAjouter(1,80)
Joueur2.getAfficher()


# exercice B


# question 1

# voir l'image en pièce jointe

# question 2

class Karaoke:
    def __init__ (self, music1, music2, music3, player1, player2, player3):
        self.__musique1 = music1
        self.__musique2 = music2
        self.__musique3 = music3
        self.__joueur1 = player1
        self.__joueur2 = player2
        self.__joueur3 = player3

    def getMusique1 (self):
        return self.__musique1
    
    def getMusique2 (self):
        return self.__musique2

    def getMusique3 (self):
        return self.__musique3

    def getJoueur1 (self):
        return self.__joueur1

    def getJoueur2 (self):
        return self.__joueur2

    def getJoueur3 (self):
        return self.__joueur3

    def afficherMusique (self,numero):

        if (numero == 1):
            print (" La musique jouée est la " + self.__musique1)

        if (numero == 2):
            print (" La musique jouée est la " + self.__musique2)

        if (numero == 3):
            print (" La musique jouée est la " + self.__musique3)

    def ajouterJoueur (self):

    def supprimerJoueur (self):

        # dans un premier temps, il faut vérifier s'il reste plus de 1 joueur

    def bestScoreChanson (self):

        # étape 1 : déterminer il s'agit de quelle chanson
        # étape 2 : aller chercher le score de cette chanson pour tous les joueurs
        # étape 3 : mettre c'est score dans une liste
        # étape 4 : lancer une suite de comparaison entre tous les scores de la liste
        # étape 5 : mettre un message affichant le meilleur score et dire à qui il appartient

    def bestScoreTotal (self):

        # étape 1 : appeler la méthode de calcul du total pour la classe Player et le faire pour tous les joueurs
        # étape 2 : mettre le résultat de ces calculs dans une liste
        # étape 3 : lancer une suite de comparaison entre tous les scores de la liste
        # étape 4 : mettre un message affichant le meilleur score total et dire à qui il appartient

    def bestScore (self):

        # étape 1 : appeler la méthode de calcul du meilleur score la classe Player et le faire pour tous les joueurs
        # étape 2 : mettre le résultat de ces calculs dans une liste
        # étape 3 : lancer une suite de comparaison entre tous les scores de la liste
        # étape 4 : mettre un message affichant le meilleur score tout confondu, dire à qui il appartient et pour quelle chanson


    def bestMoyenne (self):

        # étape 1 : appeler la méthode de calcul de la moyenne pour la classe Player et le faire pour tous les joueurs
        # étape 2 : mettre le résultat de ces calculs dans une liste
        # étape 3 : lancer une suite de comparaison entre tous les scores de la liste
        # étape 4 : mettre un message affichant la meilleur moyenne et dire à qui il appartient


# question 3

# début du programme principal
# création d'un objet lecteur de chanson à partir de la classe Karaoke

lecteurMusique = Karaoke ("musique1","musique2","musique3",Joueur1, Joueur2, Joueur3)

# faire des tests en appelant les méthodes

lecteurMusique.afficherMusique(2)

lecteurMusique.bestScoreChanson()

lecteurMusique.bestMoyenne()

