from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('journaux/<int:pk>', UpdateJournalView.as_view()),
    path('journaux', JournalView.as_view()),
    path('journaux/search/', Journalsearch.as_view()),
    path('journaux/test/', JournalViewTest.as_view()),


    path('editions/search', EditionSearch.as_view()),
    path('editions/', EditionView.as_view()),
    path('editions/<int:pk>/', UpdateEditioneView.as_view()),
    path('editions/count/', Editioncount.as_view()),

    path('articles', ArticleView.as_view()),
    path('articles/confirmed/', ArticleConfirmed.as_view()),
    path('articles/confirmed/count/', ArticleConfirmedCount.as_view()),
    path('articles/<int:pk>/', UpdateArticleView.as_view()),
    path('articles/filter', SearchFilter.as_view()),
    path('articles/search/', Articlesearch.as_view()),
    path('articles/info/', getProduitMarqueAnnonceur.as_view()),
    path('articles/client/', getProduitMarqueAnnonceur.as_view()),
    path('articles/link/', ArticleLinkClient.as_view()),

    path('afficheur/', getAfficheurInfo.as_view()),
    path('afficheur/post/', AfficheurView.as_view()),
    path('afficheur/post/<int:pk>/', AfficheurDetail.as_view()),
    path('afficheur/search/', Afficheursearch.as_view()),


    path('panneau/', PanneauView.as_view()),
    path('panneau/<int:pk>/', PanneauDetail.as_view()),
    path('panneau/filter/', PanneauFilter.as_view()),

    path('pub/', PubView.as_view()),
    path('pub/count/', PubCount.as_view()),
    path('pub/<int:pk>/', PubDetail.as_view()),
    path('pub/filter/', PubFilter.as_view()),
    path('pub/confirmed/', PubConfirmation.as_view()),
    path('pub/confirmed/count/', PubConfirmedCount.as_view()),
    path('pub/link/', PubLinkClient.as_view()),

    path('annonceur/', AnnonceurView.as_view()),
    path('annonceur/exists/', AnnonceurExiste.as_view()),
    path('getannonceurs/', GetAnnonceurs.as_view()),
    path('annonceur/<int:pk>/', AnnonceurDetail.as_view()),
    path('annonceur/search/', Annonceursearch.as_view()),

    path('marque/', MarqueView.as_view()),
    path('marque/exists/', MarqueExiste.as_view()),
    path('marque/contract', MarqueSearchContract.as_view()),
    path('marque/<int:pk>/', MarqueDetail.as_view()),
    path('marque/filter', MarqueFilter.as_view()),
    path('marque/search/', MarqueSearch.as_view()),
    path('marque/filterforcontract', MarqueFilterForContract.as_view()),


    path('produit/', ProduitView.as_view()),
    path('produit/exists/', ProduitExiste.as_view()),
    path('produit/<int:pk>/', ProduitDetail.as_view()),
    path('produit/filter', ProduitFilter.as_view()),
    path('produit/search/', ProduitSearch.as_view()),
    path('produit/filterforcontract', ProduitFilterForContract.as_view()),


    path('abonnement/', AbonnementView.as_view()),
    path('abonnement/<int:pk>', AbonnementDetail.as_view()),
    path('abonnement/search/', Abonnementsearch.as_view()),

    path('contract/', ContractView.as_view()),
    path('contract/post/', ContractPost.as_view()),
    path('contract/<int:pk>', ContractDetail.as_view()),
    path('contract/search/', Contractsearch.as_view()),

    path('wilaya/', WilayaView.as_view()),

    path('apc/', ApcView.as_view()),
    path('apc/search/', Apcsearch.as_view()),

    path('commune/', CommuneView.as_view()),
    path('commune/search/', Communesearch.as_view()),
    path('articleclient/', ArticleClientView.as_view()),
    path('pubclient/', PubClientView.as_view()),

    path('sendemail/', send_email.as_view()),
    path('clientabonnement/', ClientAbonnement.as_view()),
    path('clientcontart/', ContractViewClient.as_view()),

    path('chaine/', ChaineView.as_view()),
    path('chaine/getall/', ChaineAllView.as_view()),
    path('chaine/<int:pk>/', ChaineDetail.as_view()),
    path('chaine/search/', Chainesearch.as_view()),

    path('video/', VideoView.as_view()),
    path('video/search/', VideoView.as_view()),
    path('video/<int:pk>/', VideoDetail.as_view()),
    path('video/confirmed/', VideoConfirmation.as_view()),
    path('video/confirmed/count/', VideoConfirmedCount.as_view()),
    path('videoclient/', ChaneiClientView.as_view()),

    path('articles/link/', ArticleLinkClient.as_view()),
    path('pub/link/', PubLinkClient.as_view()),
]
