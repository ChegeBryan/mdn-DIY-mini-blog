from django.db import models


class Blog(models.Model):
    """Model representing a blog """
    title = models.CharField(max_length=200)
    content = models.TextField(help_text='Enter the blog content')
    post_date = models.DateField(auto_now_add=True)

    class Meta:
        # sort blogs from latest to oldest
        ordering = ['-post_date']


class Comment(models.Model):
    """ Comment model """
    comment = models.TextField(help_text='Write your comment')
    post_date = models.DateField(auto_now_add=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        # sort blog comments from oldest to latest
        ordering = ['post_date']


# TODO: Add author fields to both models
