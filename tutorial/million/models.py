from django.db import models


# Create your models here.
class Singer(models.Model):
    singer_sex = models.CharField('Sex of singer', max_length=20, default='')
    singer_age = models.IntegerField('Age of singer', default='')
    singer_style = models.CharField('Style of singer', max_length=20, default='')
    singer_reputation = models.CharField('Reputation of singer', max_length=20, default='')
    singer_price = models.CharField('Price of singer', max_length=20, default='')
    owner = models.ForeignKey('auth.user', related_name='singer_owner', on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.singer_price


class Groups(models.Model):
    groups_style = models.CharField(max_length=20, default='')
    groups_singers = models.ManyToManyField(Singer)
    groups_had = models.CharField(max_length=20, default='')
    groups_songs = models.CharField(max_length=20, default='')
    groups_diski = models.CharField(max_length=20, default='')


class Concert(models.Model):
    Concert_date = models.CharField('Concert date', max_length=20, default='')
    Concert_time = models.CharField('Concert time', max_length=20, default='')
    Concert_place = models.CharField('Concert place', max_length=20, default='')
    Concert_price = models.CharField('Concert price', max_length=20, default='')
    Concert_name = models.CharField('Concert name', max_length=20, default='')
    Concert_groups = models.ForeignKey(Groups, on_delete=models.CASCADE)
