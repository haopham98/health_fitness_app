from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This can be used to add additional fields or methods specific to the health and fitness application.
    """
    avatar_url = models.TextField(null=True, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


class Nutrition(models.Model):
    """
    Model to store nutrition information
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.TextField(null=True, blank=True)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.name

class MealPlan(models.Model):
    """
    Model to store meal plans
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    meals = models.ManyToManyField(Nutrition, related_name='meal_plans')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.title

class Workout(models.Model):
    """
    Model to store workout information
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.title

class WorkoutPlan(models.Model):
    """
    Model to store workout plans
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    workouts = models.ManyToManyField(Workout, related_name='workout_plans')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, default='en')

    def __str__(self):
        return self.title

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=10, default='en')
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model to store comments on blogs
    """
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.SET_NULL)

    class Meta:
        ordering = ['created_at']