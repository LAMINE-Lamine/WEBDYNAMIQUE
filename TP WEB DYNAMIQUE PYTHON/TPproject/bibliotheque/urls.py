from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
    path('traitementupdate/<int:id>/',views.traitementupdate),
    path('ajout2/', views.ajout2),
    path('traitementupdate2/', views.traitementupdate2),
    path('delete2/', views.delete2),
    path('traitement2/', views.traitement2),
    path('update2/', views.update2),

]