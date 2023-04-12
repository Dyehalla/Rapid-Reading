from django.db import models

from myauth.models import Profile


class Result(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=5)
    questions = models.PositiveIntegerField(blank=True, null=True)
    speed = models.FloatField()
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)


