from django.db import models
from django.utils import timezone

# Create your models here.


class Feedback(models.Model):
    author = models.CharField(max_length = 254)
    email = models.EmailField(max_length = 254)
    phone_number = models.IntegerField(max_length = 254)
    text = models.TextField(max_length = 2048)
    created_date = models.DateTimeField(default = timezone.now())

    def publish (self):
        self.save()

    def __str__(self):
        return self.text