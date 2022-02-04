from django.db import models

# Create your models here.

class WorkPermit(models.Model):
    GENDER_CHOICE = (
        ('Male','Male'),
        ('Female','Female')
    )
    name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 6, choices= GENDER_CHOICE)
    age = models.IntegerField(null = True, blank = True)
    date_of_birth = models.DateField(null = True, blank = True)

    def __str__(self):
        return self.name



class WorkpermitExample(models.Model):
    ACTIVITY_CHOICE = (
        ('A','A'),
        ('B','B')
    )
    activity = models.CharField(max_length= 255)
    sub_activity = models.CharField(max_length = 255)
    work_permit = models.CharField(max_length = 255)
    location = models.CharField(max_length = 400, null = True, blank = True)
    manager = models.CharField(max_length = 255)
    assignee = models.CharField(max_length = 255)

    def __str__(self):
        return self.activity
