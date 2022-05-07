from django.db import models

class Classe(models.Model):
    titre = models.CharField(max_length=100)
    resume = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.titre} "
        return chaine

    def dico(self):
        return{"titre": self.titre,"resume":self.resume}

class Arme(models.Model):

    classe= models.ForeignKey(Classe, on_delete=models.CASCADE, default=None, null=True)
    nom_d_arme = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)
    date_creation = models.DateField(blank=True, null=True)
    nombre_d_exemplaire = models.IntegerField(blank=False)
    porte = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.nom_d_arme} {self.createur} {self. date_creation}{self.nombre_d_exemplaire}"
        return chaine