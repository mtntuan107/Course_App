from django.db import models

from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# from
# Create your models here.


# class User(AbstractUser):
#     pass

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    subject = models.CharField(max_length=50)
    content = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True