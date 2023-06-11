from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    text=models.CharField(max_length=200)
    #Get foreign key from auth table user field
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    #Body of blog that expand as needed to fit users need
    body = models.TextField()

    #display title field is home page post list
    def __str__(self) -> str:
        return self.text
    
    #Get seperate page for click blog post
    def get_absolute_url(self):
        return reverse("post_detail",kwargs=("pk",self.pk))


