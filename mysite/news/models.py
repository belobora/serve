from django.db import models
from datetime import date

# Create your models here.

class Art(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anon = models.CharField('Анонс', max_length=250, default='')
    full = models.TextField('', null=True, blank=True)
    table = models.IntegerField('стол', default='1')
    guests = models.IntegerField('количество', default='1')
    vdate = models.DateField('vДата', default='2021-05-31')
    vtime = models.TimeField('vВремя', default='12:00')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'