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
                indicemeilleur = i

        print ("Le meilleur score es de " + str(meilleur) + "et il s'agit de la chanson numéro " + str(indicemeilleur))


    def getPire (self):
        listescore = [self.__point1,self.__point2,self.__point3,self.__point4,self.__point5]
        pire = 100
        indicepire = 0

        for i in range (0,len(listescore)):

            if (listescore[i] < pire):
                pire = listescore[i]
                indicepire = i

        print ("Le meilleur score es de " + str(pire) + "et il s'agit de la chanson numéro " + str(indicepire))

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






# exercice B

# question 1





# question 2





# question 3
