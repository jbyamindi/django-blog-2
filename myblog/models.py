from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
'''
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
'''

# this is the test
class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    title = models.CharField(max_length=255, verbose_name="Title")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
    is_published = models.BooleanField(default=False, verbose_name="Is published?")
    published_at = models.DateTimeField(null=True, blank=True, editable=False, verbose_name="Published at")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Category")
    author = models.ForeignKey('auth.User',on_delete=models.SET_NULL, null=True,  verbose_name="Author")
    title = models.CharField(max_length=128, verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']

    def publish(self):
        self.is_published = True
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title