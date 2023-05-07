import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class Meal(models.Model):

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Rating(models.Model):

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    meal = models.ForeignKey(Meal, related_name="rating", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.meal) + str(self.stars)+ str(self.user)
    
    class Meta:
        unique_together = (('user', 'meal'), )
        index_together = (('user', 'meal'), )
        

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def _post_save_receiver(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    



