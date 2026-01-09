# Edited via GitHub!
from django.db import models

# Зміна в гілці fix01 для практикуму №6

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
