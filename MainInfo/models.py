from django.db import models
from django.utils import timezone

# Create your models here.


class Feedback(models.Model):
    author = models.CharField( verbose_name = "Введите Ваше имя", max_length = 254)
    email = models.EmailField(verbose_name = "E-mail", max_length = 254)
    phone_number = models.CharField(verbose_name = "Контактный телефон", max_length = 254)
    text = models.TextField(verbose_name = "Сообщение", max_length = 2048)
    created_date = models.DateTimeField(default = timezone.now())

    def publish (self):
        self.save()

    def __str__(self):
        return self.text