from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# model for Notes
class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'notes'
        verbose_name_plural = "notes"


# model for Homework
class Homework(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()
    is_finished = models.BooleanField(default = False)


    def __str__(self):
        return self.title



# model for todo
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    # due = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title

# models for books/articals
class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    # due = models.DateTimeField()
    is_finished = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    
    