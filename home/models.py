from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class NewsModel(models.Model):
    image = models.ImageField(upload_to='news image')
    banner = models.ImageField(upload_to='news banner')
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    long_description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'


class ContactModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

