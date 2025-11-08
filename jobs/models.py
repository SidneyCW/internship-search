from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"

class Application(models.Model):
    from users.models import StudentProfile

    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("Applied", "Applied"),
            ("Rejected", "Rejected"),
            ("Accepted", "Accepted"),
        ],
        default="Pending"
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'job')

    def __str__(self):
        return f"{self.student.user.username} → {self.job.title}"

