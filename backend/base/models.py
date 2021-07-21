from django.db import models

# Create your models here.
class Recipe(models.Model):
    image = models.ImageField(null=True, blank=False)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name