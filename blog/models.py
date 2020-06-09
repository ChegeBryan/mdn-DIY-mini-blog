from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    """Model representing a blog """
    title = models.CharField(max_length=200)
    content = models.TextField(help_text='Enter the blog content')
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        # String for representing the Model object.
        return self.title

    class Meta:
        # sort blogs from latest to oldest
        ordering = ['-post_date']


class Comment(models.Model):
    """ Comment model """
    comment = models.TextField(help_text='Write your comment')
    post_date = models.DateField(auto_now_add=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        # String for representing the Model object.
        # add elipsis if length of comment is longer than 75 characters
        if len(self.comment) > 75:
            return self.comment[:75] + '...'
        return self.comment

    class Meta:
        # sort blog comments from oldest to latest
        ordering = ['post_date']


# TODO: Add author fields to both models
