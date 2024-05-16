from django.db import models

class Comentario(models.Model):
  noticia = models.ForeignKey('noticias.Noticia', on_delete=models.CASCADE)
  content = models.TextField()
  author = models.CharField(max_length=50)
  published_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.content