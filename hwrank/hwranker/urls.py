from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rhony/', views.rhony, name='rhony'),
    path('rhonj/', views.rhonj, name='rhonj'),
    path('rhobh/', views.rhobh, name='rhobh'),
    path('rhoa/', views.rhoa, name='rhoa'),
    path('rhop/', views.rhop, name='rhop'),
    path('rhoc/', views.rhoc, name='rhoc'),
    path('rhosl/', views.rhosl, name='rhosl'),
    path('rhod/', views.rhod, name='rhod'),
]
