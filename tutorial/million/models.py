from django.db import models



class Singer(models.Model):
    singer_sex=models.CharField('kek', max_length=20,default='')
    singer_age = models.IntegerField('kek', default='')
    singer_style = models.CharField('kek', max_length=20, default='')
    singer_reputation = models.CharField('kek', max_length=20, default='')
    singer_prize = models.CharField('kek', max_length=20, default='')


# Create your models here.
class Groups(models.Model):
    groups_style=models.CharField(max_length=20,default='')
    groups_singers= models.ManyToManyField(Singer)
    groups_had= models.CharField(max_length=20, default='')
    groups_songs = models.CharField(max_length=20, default='')
    groups_diski= models.CharField(max_length=20, default='')




class Concert(models.Model):
    Concert_date=models.CharField('kek', max_length=20,default='')
    Concert_time = models.CharField('kek', max_length=20, default='')
    Concert_place = models.CharField('kek', max_length=20, default='')
    Concert_price = models.CharField('kek', max_length=20, default='')
    Concert_ft = models.CharField('kek', max_length=20, default='')
    Concert_name = models.CharField('kek', max_length=20, default='')
    Concert_groups=models.ForeignKey(Groups, on_delete=models.CASCADE)
        