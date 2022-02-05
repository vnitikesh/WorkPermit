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
    SUBACTIVITY_CHOICE = (
        ('X','X'),
        ('Y','Y')
    )
    WORKPERMIT_CHOICE = (
        ('Hot', 'Hot'),
        ('Height', 'Height')
    )
    Location_Choice = (
        ('TowerA', 'TowerA'),
        ('TowerB', 'TowerB')
    )
    Manager_Choice = (
        ('Bob','Bob'),
        ('John', 'John')
    )
    Assignee_Choice = (
        ('Ritu','Ritu'),
        ('Riya','Riya')
    )
    activity = models.CharField(max_length= 255, choices= ACTIVITY_CHOICE)
    sub_activity = models.CharField(max_length = 255, choices= SUBACTIVITY_CHOICE)
    work_permit = models.CharField(max_length = 255, choices= WORKPERMIT_CHOICE)
    location = models.CharField(max_length = 400, null = True, blank = True, choices= Location_Choice)
    manager = models.CharField(max_length = 255, choices= Manager_Choice)
    assignee = models.CharField(max_length = 255, choices= Assignee_Choice)

    def __str__(self):
        return self.activity
