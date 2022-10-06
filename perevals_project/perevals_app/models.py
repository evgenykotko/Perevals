from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class Coord(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()


class Level(models.Model):
    winter = models.CharField(max_length=10, default='')
    summer = models.CharField(max_length=10, default='')
    autumn = models.CharField(max_length=10, default='')
    spring = models.CharField(max_length=10, default='')


class PerevalImages(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=20)
    img = models.BinaryField()

    class Meta:
        db_table = 'pereval_images'


class PerevalAdded(models.Model):
    new = 'new'
    pending = 'pen'
    accepted = 'acc'
    rejected = 'rej'
    STATUS_MODERATE = [
        (new, 'Новая заявка на модерацию'),
        (pending, 'Модерируется'),
        (accepted, 'Модерация прошла успешно'),
        (rejected, 'Модерация прошла, информация не принята'),
    ]
    date_added = models.DateField(auto_now_add=True)
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    other_title = models.CharField(max_length=255)
    connect = models.TextField(default='')
    add_time = models.TimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    coord_id = models.ForeignKey(Coord, related_name='coords_id', on_delete=models.CASCADE)
    level_id = models.ForeignKey(Level, related_name='level_id', on_delete=models.CASCADE)
    images_id = models.ForeignKey(PerevalImages, related_name='images_id', on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_MODERATE, default=new)

    class Meta:
        db_table = 'pereval_added'


class PerevalAreas(models.Model):
    id_parent = models.IntegerField(null=True)
    title = models.TextField(null=True)

    class Meta:
        db_table = 'pereval_areas'


class SprActivitiesTypes(models.Model):
    title = models.TextField(null=True)

    class Meta:
        db_table = 'spr_activities_types'
