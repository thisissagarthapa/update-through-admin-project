from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image')  # python library-pip install pillow for first time

    def __str__(self) -> str:
        return self.title
