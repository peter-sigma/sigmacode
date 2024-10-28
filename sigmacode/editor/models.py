from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class CodeSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    output = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
