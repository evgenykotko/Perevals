from django.db import models


class Add_user(models.Model):
    email = models.EmailField()
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
    img = models.BinaryField()

    class Meta:
        db_table = 'pereval_images'


class Images(models.Model):
    data = models.CharField(max_length=20)
    title = models.CharField(max_length=20)


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255, unique=True)
    other_title = models.CharField(max_length=255)
    connect = models.TextField(default='')
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.ForeignKey(Coord, related_name='coords', on_delete=models.CASCADE)
    user = models.ForeignKey(Add_user, related_name='user', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, related_name='level', on_delete=models.CASCADE)
    images = models.ForeignKey(Images, related_name='images', on_delete=models.CASCADE)


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
    date_added = models.DateTimeField(auto_now_add=True)
    raw_data = models.JSONField()
    images = models.JSONField(null=True)
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
