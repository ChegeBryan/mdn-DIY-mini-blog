from django.db import models


class Blog(models.Model):
    """Model representing a blog """
    title = models.CharField(max_length=200)
    content = models.TextField(help_text='Enter the blog content')
    post_date = models.DateField(auto_now_add=True)
