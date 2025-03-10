from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    skillsets = models.CharField(max_length=100, default="No skill sets assigned")
    tools_known = models.CharField(max_length=150, default="No tools are assigned")
    computer_languages_known = models.CharField(max_length=100, default="Languages are not assigned")
    department = models.CharField(max_length=30, default='EEE' )
    working_at = models.CharField(max_length=30, default="Not updated yet")
    batch = models.PositiveIntegerField(default=2020)
    contact_email = models.EmailField(default='notset@gmail.com')

    def __str__(self):
        return '{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        try:
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        except:
            pass
