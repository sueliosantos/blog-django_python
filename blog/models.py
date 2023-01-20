from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    author = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    conteudo = RichTextUploadingField()
    data_publicacao= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo