from django.db import models

class Noticia(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=50)
  imageLink = models.CharField(max_length=200, blank=True, null=True)
  published_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
