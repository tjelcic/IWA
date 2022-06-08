from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class MyPersonManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email adress")
        if not username:
            raise ValueError("User must have a username")

        user = self.model(email=self.normalize_email(email),
                        username=username)
        
        user.set_password(password) 
        user.save(using=self.db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username 
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Person(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    username = models.CharField(max_length=60, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyPersonManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Projection(Model):
    movie_name = models.CharField(max_length=30)
    movie_time = models.TimeField()
    capacity = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.movie_name, self.movie_time, self.capacity)

class Ticket(Model):
    seat_number = models.IntegerField()
    projection = models.ForeignKey(Projection, blank = True, null = True, on_delete = models.CASCADE)
    user = models.ForeignKey(Person, blank = True, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.seat_number, self.projection, self.user)
