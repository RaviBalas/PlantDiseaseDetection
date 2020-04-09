from django.db import models

class Profile(models.Model):   
   picture = models.ImageField(upload_to = 'media/')
