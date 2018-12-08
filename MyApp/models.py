from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=50, blank=True)
    picture = models.CharField(max_length=255,blank=True)
    created = models.DateField(default=datetime.now, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class messaging(models.Model):

    idmsg = models.AutoField(primary_key=True)
    idRoom = models.IntegerField(blank=False)
    senderId = models.IntegerField(blank=False)
    message = models.CharField(max_length=255)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('message-view', args=[str(self.idmsg)])

    def __str__(self):
        return self.message

class rooms(models.Model):

    idRoom = models.AutoField(primary_key=True)
    idUser1 = models.IntegerField(blank=False)
    idUser2 = models.IntegerField(blank=False)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('room-view', args=[str(self.idRoom)])

    def __str__(self):
        return self.idRoom

class friends(models.Model):
    id = models.AutoField(primary_key=True)
    senderId = models.IntegerField(blank=False)
    receiverId = models.IntegerField(blank=False)
    statut = models.IntegerField(blank=False)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def get_absolute_url(self):
        return reverse('freind-view', args=[str(self.id)])

    def __str__(self):
        return self.id






