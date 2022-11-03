from turtle import title
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name=models.CharField(max_length= 100)
    last_name= models.CharField(max_length= 100)
    age=models.IntegerField()
    
    def __str__(self) :
        return str(self.first_name) + str(self.last_name)

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title=models.CharField(max_length= 100)
    date_released =models.DateTimeField()
    likes =models.IntegerField()
    #artiste_id=
    
    def __str__(self) -> str:
        return str(self.title)


class Lyric(models.Model):
    song_id= models.ForeignKey(Song,on_delete=models.CASCADE)
    content =models.CharField(max_length= 100)
    #song_id =

    def __str__(self) -> str:
        return str(self.content)