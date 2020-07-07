from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='names')
    name = models.CharField(max_length=500)
    slug_name = models.SlugField(blank=True,null=True)
    img = models.ImageField(blank=True,null=True,upload_to='images/')
    link = models.URLField()
    description = models.TextField(default='')
    img_link = models.URLField(blank=True,null=True)

    def save(self,*args,**kwargs):
        self.slug_name = slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('site_links:detail',kwargs={'pk':self.pk,'name':self.slug_name})

    def __str__(self):
        return self.name


