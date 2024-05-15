from django.db import models



class vid(models.Model):

    url = models.FileField(upload_to='videos/', null=True)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=120, null=True)
    cap_fil = models.FileField(upload_to='subtitles/', null=True)
    image = models.ImageField(upload_to='images/', null=True)


# Create your models here.
