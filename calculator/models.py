from django.db import models

# Create your models here.
class UserEntries(models.Model):
    text = models.TextField()
    words = models.IntegerField()
    chars = models.IntegerField()
    vowels = models.IntegerField()
    consonants = models.IntegerField()

    def __str__(self) -> str:
        return str(self.id) + " - " + self.text[:36]