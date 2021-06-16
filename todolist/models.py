from django.db import models
from datetime import date
import datetime
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    startdate=models.DateTimeField(verbose_name="start date")
    enddate=models.DateTimeField(verbose_name="end date")
    def __str__(self):
        return self.title