from django.db import models
from django_resized import ResizedImageField
from embed_video.fields import EmbedVideoField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE,)

    introtext = models.CharField(max_length=300, default="ABCD")

    date = models.DateTimeField(auto_now_add=True)

    body = models.TextField()

    cover = ResizedImageField(upload_to="images/", blank=True)

    video = EmbedVideoField(blank=True)

    tags = [
        ("Travel", "Travel"),
        ("Languages", "Languages"),
        ("Teaching", "Teaching"),
        ("Miscellaneous", "Miscellaneous"),
    ]

    tag = models.TextField(choices=tags, default="Miscellaneous")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogpost", args[str(self.id)])

