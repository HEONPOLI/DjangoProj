from django.db import models
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    start_day=models.CharField(max_length=350)
    start_month=models.CharField(max_length=350)
    start_year=models.CharField(max_length=350)
    end_day=models.CharField(max_length=350)
    end_month=models.CharField(max_length=350)
    end_year=models.CharField(max_length=350)
    def __str__(self):
        return self.title