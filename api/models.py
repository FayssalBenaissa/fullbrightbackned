
from django.db import models
import datetime

from django.db.models.deletion import CASCADE
from users.serializers import *


class Journal(models.Model):
    nomJournal = models.CharField(max_length=20, default="", unique=True)
    image = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return self.nomJournal


class Edition(models.Model):
    date = models.DateField()
    numero = models.IntegerField()
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return str(self.journal)+"  ===>  "+str(self.date)+"  ===>  "+str(self.id)


class Article(models.Model):
    languages = (
        ("AR", "arabe"),
        ("FR", "francais"),
    )

    pages = (
        ("s", "sport"),
        ("p", "politeque"),
        ("c", "culture"),
    )
    annonceur = models.ForeignKey(
        'Annonceur', on_delete=models.CASCADE)
    marque = models.ForeignKey(
        'Marque', on_delete=models.CASCADE, null=True, blank=True)
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="media",  default="")
    date_creation = models.DateField()
    language = models.CharField(max_length=2, default="", choices=languages)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    accroche = models.CharField(max_length=10000, default="")
    page_suivante = models.CharField(max_length=1, default="", choices=pages)
    page_precedente = models.CharField(max_length=1, default="", choices=pages)
    confirmed = models.BooleanField(default=False)


# -----------------------definition des table d'adresse : wilaya commune et Apc ---------------------------.
class Wilaya(models.Model):
    nom_wilaya = models.CharField(max_length=30)
    num_wilaya = models.IntegerField()

    def __str__(self):
        return self.nom_wilaya


class Commune (models.Model):
    nom_commune = models.CharField(max_length=50)
    Wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_commune


class Apc (models.Model):
    nom_APC = models.CharField(max_length=50)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_APC


# -------------------------- definition de la table Afficheur ------------------------------------------
class Afficheur(models.Model):
    nom_afficheur = models.CharField(max_length=30, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom_afficheur


# --------------------------- definition de la table Panneau --------------------------------------------
class Panneau(models.Model):
    choix_type = [
        ('Simple', 'Simple'),
        ('Unipol', 'Unipol'),
        ('Sucette', 'Sucette'),
        ('Abri-Bus', 'Abri-Bus'),
        ('Bus', 'Bus'),
        ('Sucette dynamique', 'Sucette dynamique'),
        ('Terasse', 'Terasse'),
        ('Fassade', 'Fassade'),
    ]
    choix_mecanisme = [
        ('Dérouleur', 'Dérouleur'),
        ('Trivision', 'Trivision'),
        ('Fix', 'Fix'),
    ]
    afficheur = models.ForeignKey(Afficheur, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=choix_type)
    apc = models.ForeignKey(Apc, on_delete=models.CASCADE)
    itineraire = models.CharField(max_length=20)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField()
    designation = models.CharField(max_length=40)
    nombre_facette = models.IntegerField()
    hauteur = models.FloatField()
    largeur = models.FloatField()
    elevation = models.FloatField()
    nbpub = models.IntegerField()
    mecanisme = models.CharField(max_length=20, choices=choix_mecanisme)
    date_creation = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return self.code
# --------------------------- definition de la table Pub --------------------------------------------


class Pub(models.Model):
    choix_langue = [
        ('fr', 'fr'),
        ('ar', 'ar'),
        ('fr + ar', 'fr + ar'),
    ]
    panneau = models.ForeignKey(Panneau, on_delete=models.CASCADE)
    langue = models.CharField(max_length=20, choices=choix_langue)
    date_creation = models.DateField(auto_now_add=True)
    image = models.ImageField(
        upload_to="media", null=True, blank=True, default="")
    video = models.FileField(
        upload_to="media", null=True, blank=True, default="")
    annonceur = models.ForeignKey(
        'Annonceur', on_delete=models.CASCADE)
    marque = models.ForeignKey(
        'Marque', on_delete=models.CASCADE, null=True, blank=True)
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    circulation = models.BooleanField(default=True)

    def __str__(self):
        return str(self.date_creation)+"  ===>  "+str(self.id)


class Annonceur(models.Model):

    Nom = models.CharField(max_length=100, unique=True)
    Logo = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return str(self.id)


class Marque(models.Model):
    NomAnnonceur = models.ForeignKey(Annonceur, on_delete=models.CASCADE)
    Nom = models.CharField(max_length=100, unique=True)
    Logo = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return str(self.id)


class Produit(models.Model):
    NomMarque = models.ForeignKey(Marque, on_delete=models.CASCADE)
    Nom = models.CharField(max_length=100, unique=True)
    Logo = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return str(self.id)


# ------------------------------------------------------------

class Abonnement(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, default=3)
    services = [
        ('J', 'Journal'),
        ('P', 'Panneau'),
        ('C', 'Chaine'),
    ]
    Nom = models.CharField(max_length=100, unique=True)
    service = models.CharField(max_length=1, default="", choices=services)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return self.Nom

# date d'expiration base sur l'abonnemnet


class Contract(models.Model):
    abonnement = models.ForeignKey(Abonnement, on_delete=models.CASCADE)
    annonceurs = models.ManyToManyField(Annonceur)
    marques = models.ManyToManyField(Marque, null=True, blank=True)
    produits = models.ManyToManyField(Produit, null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()


class VideoPub(models.Model):
    languages = (
        ("AR", "arabe"),
        ("FR", "francais"),
    )
    chaine = models.ForeignKey('Chaine', on_delete=models.CASCADE)
    annonceur = models.ForeignKey(
        'Annonceur', on_delete=models.CASCADE)
    marque = models.ForeignKey(
        'Marque', on_delete=models.CASCADE, null=True, blank=True)
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to="media",  default="")
    date_creation = models.DateTimeField()
    language = models.CharField(max_length=2, default="", choices=languages)
    accroche = models.CharField(max_length=10000, default="")
    confirmed = models.BooleanField(default=False)


class Chaine(models.Model):
    nom = models.CharField(max_length=20, default="", unique=True)
    image = models.ImageField(upload_to="media", default="")
