from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

# Create your models here.

class Projekcija(Model):
    movie_name = models.CharField(max_length=30)
    movie_time = models.TimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.movie_name, self.movie_time, self.capacity)

class Karta(Model):
    seat_number = models.IntegerField()
    movie = models.ForeignKey(Projekcija, blank = True, null = True, on_delete = models.CASCADE)
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.seat_number, self.movie, self.user)