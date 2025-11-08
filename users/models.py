from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True)
    major = models.TextField(blank=True)
    yos = models.IntegerField(blank=True) # year of study (yos)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username