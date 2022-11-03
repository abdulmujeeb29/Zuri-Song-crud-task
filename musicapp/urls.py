from django.urls import path 
from . import views 

urlpatterns = [
    path('artists',views.artiste_list,name='artiste_list'),
    path('songs',views.song_list),
    path('songs/<int:pk>',views.song_particular),
    
]