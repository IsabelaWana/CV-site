from django.db import models
from django.utils import timezone


class CV(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    personal_info = models.TextField()
    education = models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
