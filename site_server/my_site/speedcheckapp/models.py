from django.db import models


class Result(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=5)
    questions = models.PositiveIntegerField(blank=True, null=True)
    speed = models.FloatField()
    user_id = models.IntegerField()


