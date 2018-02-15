from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


REASON_CHOICE=(
    ('OD','OD'),
    ('FUNCTION','FUNCTION'),
    ('OTHER','OTHER')
)

class leavemodels(models.Model):
    reason=models.CharField(max_length=100,choices=REASON_CHOICE)
    date=models.DateTimeField(default=datetime.now())
    section=models.CharField(max_length=5)


class user(models.Model):
    rollno=models.CharField(max_length=8)

# Create your models here.
