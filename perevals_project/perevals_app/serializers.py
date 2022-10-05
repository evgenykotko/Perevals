from .models import *
from rest_framework import serializers



class Add_userSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add_user
        fields = ['email', 'fam', 'name', 'otc', 'phone']
class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']

class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = ['data', 'title']

class PerevalSerializer(serializers.ModelSerializer):
    coords = CoordSerializer()
    user = Add_userSerializer()
    level = LevelSerializer()
    images = ImagesSerializer()
    class Meta:
        model = Pereval
        fields = ['beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coords', 'level', 'images']

    def create(self, validated_data):
        coords_data = validated_data.pop('coords')
        user_data = validated_data.pop('user')
        level_data = validated_data.pop('level')
        images_data = validated_data.pop('images')
        coords = Coord.objects.create(**coords_data)
        user = Add_user.objects.create(**user_data)
        level = Level.objects.create(**level_data)
        images = Images.objects.create(**images_data)
        pereval = Pereval.objects.create(coords=coords, user=user, level=level, images=images, **validated_data)
        return pereval


class PerevalAddedSerializer(serializers.ModelSerializer):
    raw_data = PerevalSerializer
    images = ImagesSerializer

    class Meta:
        model = PerevalAdded
        fields = '__all__'

