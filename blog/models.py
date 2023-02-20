from django.db import models

# Create your models here.

class SnsModel(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  author = models.CharField(max_length=50)
  snsimage = models.ImageField(upload_to='')
  good = models.IntegerField()
  read = models.IntegerField()
  readtext = models.TextField()

  def __str__(self) -> str:
    return self.title