from django.db import models

# Create your models here.
class Push_event(models.Model):
    author=models.CharField(max_length=250)
    branch=models.CharField(max_length=250)
    datetime=models.DateTimeField()

class Pull_request(models.Model):
    author=models.CharField(max_length=250)
    from_branch=models.CharField(max_length=250)
    to_branch=models.CharField(max_length=250)
    datetime=models.DateTimeField()

class Merge_event(models.Model):
    author=models.CharField(max_length=250)
    from_branch=models.CharField(max_length=250)
    to_branch=models.CharField(max_length=250)
    datetime=models.DateTimeField()