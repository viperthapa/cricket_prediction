from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    company = models.CharField(max_length=199)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employer')


    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length=200)
    # category = models.ForeignKey(Category,on_delete = models.CASCADE)
    image = models.ImageField(upload_to="news")
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
