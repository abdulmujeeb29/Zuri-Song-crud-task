from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from musicapp.serializer import Artisteserializer ,Songserializer,Lyricserializer
from musicapp.models import Artiste,Lyric,Song



# Create your views here.

@api_view(['GET'])
def song_list(request):
    songs =Song.objects.all()
    serializer =Songserializer(songs, many= True)
    return Response(serializer.data)


@api_view(['GET'])
def artiste_list(request):
    lists =Artiste.objects.all()
    serializer= Artisteserializer(lists,many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def song_particular(request, pk):
    song = Song.objects.get(pk=pk)

    if request.method == 'GET':
        
        serializer = Songserializer(song)
        return Response(serializer.data)


    elif request.method == 'PUT':
        
        serializer= Songserializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)



    elif request.method == 'DELETE':
        song.delete()
        return Response('deleted')