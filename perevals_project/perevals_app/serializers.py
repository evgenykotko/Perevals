from .models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone']
class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']

class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']

class PerevalImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PerevalImages
        fields = ['date_added', 'title', 'img']

class PerevalAddedSerializer(serializers.ModelSerializer):
    coord_id = CoordSerializer()
    user_id = UserSerializer()
    level_id = LevelSerializer()
    images_id = PerevalImagesSerializer()
    class Meta:
        model = PerevalAdded
        fields = [
            'id',
            'date_added',
            'beauty_title',
            'title',
            'other_title',
            'connect',
            'add_time',
            'user_id',
            'coord_id',
            'level_id',
            'images_id',
            'status',
        ]

    def create(self, validated_data):
        coord_data = validated_data.pop('coord_id')
        user_data = validated_data.pop('user_id')
        level_data = validated_data.pop('level_id')
        images_data = validated_data.pop('images_id')
        coords = Coord.objects.create(**coord_data)
        user = User.objects.create(**user_data)
        level = Level.objects.create(**level_data)
        images = PerevalImages.objects.create(**images_data)
        pereval = PerevalAdded.objects.create(coord_id=coords, user_id=user, level_id=level, images_id=images, **validated_data)
        return pereval

#
# class PerevalAddedSerializer(serializers.ModelSerializer):
#     raw_data = PerevalSerializer
#     images = ImagesSerializer
#
#     class Meta:
#         model = PerevalAdded
#         fields = '__all__'

