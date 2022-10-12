from .models import *
from rest_framework import serializers


class CoordSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Coord
        fields = [
            'latitude',
            'longitude',
            'height'
        ]

class UserSerialiser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'fam',
            'name',
            'otc',
            'phone',
        ]

class LevelSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Level
        fields = [
            'winter',
            'summer',
            'autumn',
            'spring'
        ]

class ImageSerialiser(serializers.ModelSerializer):

    class Meta:
        model = PerevalImages
        fields = [
            'date_added',
            'title',
            'img',
        ]


class PerevalSerializer(serializers.ModelSerializer):
    coord_id = CoordSerialiser(read_only=True)
    level_id = LevelSerialiser(read_only=True)
    user_id = UserSerialiser(read_only=True)
    image_id = ImageSerialiser(read_only=True)

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
            'image_id',
            'status'
        ]
class PerevalAddSerializer(serializers.ModelSerializer):
    coord_id = CoordSerialiser()
    level_id = LevelSerialiser()
    image_id = ImageSerialiser()

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
            'image_id',
            'status'
        ]
    def create(self, validated_data):
        coord_data = validated_data.pop('coord_id')
        coord = Coord.objects.create(**coord_data)
        level_data = validated_data.pop('level_id')
        level = Level.objects.create(**level_data)
        image_data = validated_data.pop('image_id')
        image = PerevalImages.objects.create(**image_data)
        return PerevalAdded.objects.create(coord_id=coord, level_id=level, image_id=image, **validated_data)

    def update(self, instance, validated_data):
        instance.coord_id = validated_data.get('coord_id', instance.coord_id)
        instance.level_id = validated_data.get('level_id', instance.level_id)
        instance.image_id = validated_data.get('image_id', instance.image_id)
        instance.save()
        return instance


