from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    # post  has the author, the title, the body and the created and published dates
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # note that this uses the django user model,
    # which you'd have to import to use in the shell
    title = models.CharField(max_length=200) # the title has a max char length of 200 chars
    text = models.TextField() # unlimited content of post
    created_date = models.DateTimeField(default=timezone.now) # current time
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # get the current time
        self.published_date = timezone.now()
        # save
        self.save()

    def __str__(self):
        # print the title of the post when called
        return self.title


class Comment(models.Model):
    # related_name is how the comments are found in the template
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
