from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from django.contrib.postgres.fields import ArrayField

STATUS = ((0, 'Draft'), (1, 'Published'))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    profile_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes_posted'
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    # ingredients = ArrayField(models.TextField())
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name='recipes_liked', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.title}'
