from rest_framework import serializers 

class Artisteserializer(serializers.Serializer):
    first_name=serializers.CharField()
    last_name= serializers.CharField()
    age=serializers.IntegerField()


class Songserializer(serializers.Serializer):
    artiste_id = serializers.CharField()
    title=serializers.CharField()
    date_released =serializers.DateTimeField()
    likes =serializers.IntegerField()


    def update(self, instance , data):
        instance.title = data.get('title', instance.title )
        instance.date_released = data.get('date_released', instance.date_released )

        instance.save() 
        return instance 

class Lyricserializer(serializers.Serializer):
    song_id= serializers.CharField()
    content =serializers.CharField()