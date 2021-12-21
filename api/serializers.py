from rest_framework import serializers, fields
from .models import *
from django.db.models.aggregates import Count, Sum


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id', 'nomJournal', 'image']


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ['id', 'date', "numero", "journal", "image"]


class ArticleClientSerializer(serializers.ModelSerializer):
    nom_annonceur = serializers.SerializerMethodField()
    nom_marque = serializers.SerializerMethodField()
    nom_produit = serializers.SerializerMethodField()

    numEdition = serializers.SerializerMethodField()
    dateEdition = serializers.SerializerMethodField()
    nomJournal = serializers.SerializerMethodField()

    def get_numEdition(self, obj):
        return obj.edition.numero

    def get_dateEdition(self, obj):
        return obj.edition.date

    def get_nomJournal(self, obj):
        return obj.edition.journal.nomJournal

    def get_nom_annonceur(self, obj):
        return obj.annonceur.Nom

    def get_nom_marque(self, obj):
        if obj.marque:
            return obj.marque.Nom
        else:
            return "indefinie"

    def get_nom_produit(self, obj):
        if obj.produit:
            return obj.produit.Nom
        else:
            return "indefinie"

    class Meta:
        model = Article
        fields = ['id', 'date_creation', "language", "edition", "accroche",
                  "page_suivante", "page_precedente", 'annonceur', 'marque', "produit", "image",
                  "numEdition", "dateEdition", "nomJournal", "nom_annonceur",
                  "nom_marque", "nom_produit"]


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_creation', "language", "edition", "accroche",
                  "page_suivante", "page_precedente", 'annonceur', 'marque', "produit", "confirmed", "image"]


# ---------------------------------------------------------------------------------------------


class AfficheurSerializer(serializers.ModelSerializer):
    numPanneau = serializers.SerializerMethodField()
    numPub = serializers.SerializerMethodField()
    nomAff = serializers.SerializerMethodField()

    def get_numPanneau(self, obj):
        numPanneau = Panneau.objects.filter(afficheur=obj.id).count()
        return numPanneau

    def get_numPub(self, obj):
        numPub = Panneau.objects.filter(afficheur=obj.id).annotate(
            num_prod=Count('pub')).aggregate(Sum("num_prod"))
        return numPub['num_prod__sum'] if numPub['num_prod__sum'] != None else 0

    def get_nomAff(self, obj):
        return obj.nom_afficheur

    class Meta:
        model = Afficheur
        fields = ['id', 'nom_afficheur', 'numPanneau', 'numPub', 'nomAff']
# ---------------------------------------------------------------------------------------------


class PanneauSerializer(serializers.ModelSerializer):
    nomWilaya = serializers.SerializerMethodField()
    nomApc = serializers.SerializerMethodField()
    nomCommune = serializers.SerializerMethodField()

    def get_nomWilaya(self, obj):
        return obj.apc.commune.Wilaya.id

    def get_nomCommune(self, obj):
        return obj.apc.commune.id

    def get_nomApc(self, obj):
        return obj.apc.id

    class Meta:
        model = Panneau
        fields = ['id', 'afficheur', 'adresse', 'code', 'type', 'apc', 'itineraire',
                  'latitude', 'longitude', 'designation', 'nombre_facette', 'hauteur', 'largeur',
                  'elevation', 'mecanisme',  'image', 'nomApc', 'nomWilaya', 'nomCommune', 'nbpub']

# ----------------------------------------------------------------------------------------------


class PubSerializer(serializers.ModelSerializer):
    nom_annonceur = serializers.SerializerMethodField()
    nom_marque = serializers.SerializerMethodField()
    nom_produit = serializers.SerializerMethodField()
    code_panneau = serializers.SerializerMethodField()

    def get_nom_annonceur(self, obj):
        return obj.annonceur.Nom

    def get_nom_marque(self, obj):
        if obj.marque:
            return obj.marque.Nom
        else:
            return ""

    def get_nom_produit(self, obj):
        if obj.produit:
            return obj.produit.Nom
        else:
            return ""

    def get_code_panneau(self, obj):
        return obj.panneau.code

    class Meta:
        model = Pub
        fields = ['id', "panneau", 'code_panneau', 'langue', 'annonceur', 'marque', 'produit',  "confirmed",
                  'nom_produit', 'nom_annonceur', 'nom_marque', 'date_creation', 'image', 'video', 'circulation']


class PubClientSerializer(serializers.ModelSerializer):
    nom_annonceur = serializers.SerializerMethodField()
    nom_marque = serializers.SerializerMethodField()
    nom_produit = serializers.SerializerMethodField()
    code_panneau = serializers.SerializerMethodField()
    panneau_detail = serializers.SerializerMethodField()

    def get_panneau_detail(self, obj):
        serializer = PanneauSerializer(obj.panneau)
        return serializer.data

    def get_nom_annonceur(self, obj):
        return obj.annonceur.Nom

    def get_nom_marque(self, obj):
        if obj.marque:
            return obj.marque.Nom
        else:
            return "indefinie"

    def get_nom_produit(self, obj):
        if obj.produit:
            return obj.produit.Nom
        else:
            return "indefinie"

    def get_code_panneau(self, obj):
        return obj.panneau.code

    class Meta:
        model = Pub
        fields = ['id', "panneau", 'code_panneau', 'langue',  'annonceur', 'marque', 'produit',
                  'nom_produit', 'nom_annonceur', 'nom_marque', 'date_creation', 'image', 'panneau_detail', "circulation"]


class AnnonceurSerializer(serializers.ModelSerializer):
    numMarque = serializers.SerializerMethodField()
    nbProduit = serializers.SerializerMethodField()

    def get_numMarque(self, obj):
        nbMarque = Marque.objects.filter(NomAnnonceur=obj.id).count()
        return nbMarque

    def get_nbProduit(self, obj):
        nbProduit = Marque.objects.filter(NomAnnonceur=obj.id).annotate(
            num_prod=Count('produit')).aggregate(Sum("num_prod"))
        return nbProduit['num_prod__sum'] if nbProduit['num_prod__sum'] != None else 0

    class Meta:
        model = Annonceur
        fields = ('id', 'Nom', "Logo", "numMarque", "nbProduit")


class MarqueSerializer(serializers.ModelSerializer):
    nbProduit = serializers.SerializerMethodField()

    def get_nbProduit(self, obj):
        return Produit.objects.filter(NomMarque=obj.id).count()

    class Meta:
        model = Marque
        fields = ('id', "NomAnnonceur", 'Nom', "Logo", "nbProduit")


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = ('id', "NomMarque", 'Nom', "Logo")


class WilayaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wilaya
        fields = ('id', 'nom_wilaya', "num_wilaya")


class ApcSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apc
        fields = ('id', 'nom_APC', "commune")


class CommuneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commune
        fields = ('id', 'nom_commune', "Wilaya")


class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = ('id', 'client', 'Nom', "service", 'date_debut', "date_fin")


class ContractSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()

    def get_detail(self, obj):
        ann = []
        for a in obj.annonceurs.all():
            ann.append({
                "idAnnonceur": a.Nom,
                "marques": [{"marque": MarqueSerializer(m).data,
                             "produits": [ProduitSerializer(p).data for p in obj.produits.filter(NomMarque=m)]
                             } for m in obj.marques.filter(NomAnnonceur=a)]
            })
        return ann

    class Meta:
        model = Contract
        fields = ('id', 'abonnement', "produits", "annonceurs",
                  "marques", 'date_debut', "date_fin", "detail")


class ContractSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('id', 'abonnement', "produits", "annonceurs",
                  "marques", 'date_debut', "date_fin")


class ClientArticleSerializer(serializers.ModelSerializer):
    numEdition = serializers.SerializerMethodField()
    dateEdition = serializers.SerializerMethodField()
    nomJournal = serializers.SerializerMethodField()

    def get_numEdition(self, obj):
        return obj.edition.numero

    def get_dateEdition(self, obj):
        return obj.edition.date

    def get_nomJournal(self, obj):
        return obj.edition.journal.nomJournal

    class Meta:
        model = Article
        fields = ['id', 'date_creation', "language", "edition", "accroche",
                  "page_suivante", "page_precedente", 'annonceur', 'marque', "produit", "image",
                  "numEdition", "dateEdition", "nomJournal"]


class ClientPubSerializer(serializers.ModelSerializer):
    codePanneau = serializers.SerializerMethodField()
    adresse = serializers.SerializerMethodField()
    itineraire = serializers.SerializerMethodField()
    apc = serializers.SerializerMethodField()
    commune = serializers.SerializerMethodField()
    wilaya = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    def get_codePanneau(self, obj):
        return obj.panneau.code

    def get_adresse(self, obj):
        return obj.panneau.adresse

    def get_itineraire(self, obj):
        return obj.panneau.itineraire

    def get_apc(self, obj):
        return obj.panneau.apc.nom_APC

    def get_commune(self, obj):
        return obj.panneau.apc.commune.nom_commune

    def get_wilaya(self, obj):
        return obj.panneau.apc.commune.Wilaya.nom_wilaya

    def get_latitude(self, obj):
        return obj.panneau.latitude

    def get_longitude(self, obj):
        return obj.panneau.longitude

    class Meta:
        model = Pub
        fields = ['id', 'codePanneau', 'langue', 'prod',
                  'date_creation', 'image',
                  'adresse', 'itineraire', 'apc', 'commune',
                  'wilaya', 'latitude', 'longitude']


class VideoSerializer(serializers.ModelSerializer):
    nom_produit = serializers.SerializerMethodField()
    nom_marque = serializers.SerializerMethodField()
    nom_annonceur = serializers.SerializerMethodField()
    nom_chaine = serializers.SerializerMethodField()

    def get_nom_annonceur(self, obj):
        return obj.annonceur.Nom

    def get_nom_chaine(self, obj):
        return obj.chaine.nom

    def get_nom_marque(self, obj):
        if obj.marque:
            return obj.marque.Nom
        else:
            return "indefine"

    def get_nom_produit(self, obj):
        if obj.produit:
            return obj.produit.Nom
        else:
            return "indefine"

    class Meta:
        model = VideoPub
        fields = ['id', 'date_creation', "language", "chaine", "accroche",
                  'annonceur', 'marque', "produit", "video", "confirmed",
                  "nom_annonceur", "nom_marque", "nom_produit", "nom_chaine"]


class ChaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chaine
        fields = "__all__"
