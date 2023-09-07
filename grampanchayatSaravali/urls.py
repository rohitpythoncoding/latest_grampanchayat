from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome),
    path('home/', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('workers/', views.workers, name='workers'),
    path('electedMember/', views.electedMember, name='electedMember'),
    path('certificates/', views.certificates, name='certificates'),
    path('photoGallery/', views.photoGallery, name='photoGallery'),
    path('faq/', views.faq, name='faq'),
    path('developmentPlan/', views.developmentPlan, name='developmentPlan'),
    path('committees/', views.committees, name='committees'),
    path('scm1/', views.scm1, name='scm1'),
    path('scm2/', views.scm2, name='scm2'),
    path('scm3/', views.scm3, name='scm3'),
    path('scm4/', views.scm4, name='scm4'),
    path('scm5/', views.scm5, name='scm5'),
    path('scm6/', views.scm6, name='scm6'),
    path('other1/', views.other1, name='other1'),
    path('other2/', views.other2, name='other2'),
    path('other3/', views.other3, name='other3'),
    path('other4/', views.other4, name='other4'),
    path('other5/', views.other5, name='other5'),
    path('other6/', views.other6, name='other6'),
    path('other7/', views.other7, name='other7'),
    path('about/', views.about, name='about'),


]
