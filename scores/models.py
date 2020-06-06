from django.db import models

# Create your models here.

class Situation(models.Model):
    innings_no = models.IntegerField()
    over_no = models.IntegerField()
    target = models.IntegerField()
    runs = models.IntegerField()
    wickets = models.IntegerField()
    avg_socre = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
