from django.db import models

# Create your models here.

class Trainee(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name