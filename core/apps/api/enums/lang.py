from django.db import models



class LangChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'
    RUSSIAN = 'ru', 'Russian'
    