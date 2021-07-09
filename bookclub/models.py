from django.db import models
from django.db.models.fields import DateField
from ckeditor.fields import RichTextField

class Book(models.Model):
    book = models.CharField(max_length=100)
    description = RichTextField()
    read_by = DateField()

class Discussion(models.Model):
    book = models.ForeignKey('bookclub.Book', related_name='discussion', on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', related_name='records', on_delete=models.CASCADE)
    opinion = RichTextField()
    image = models.ImageField(upload_to='images', blank=True)