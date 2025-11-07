from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
