from django.db import models
from django.utils.timezone import now

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=120)
    project_category = models.CharField(max_length=120)
    project_date = models.DateField(default=now, editable=True)
    project_description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    technologies_used1 = models.CharField(max_length=120, default='nothing')
    technologies_used2 = models.CharField(max_length=120, default='nothing')
    technologies_used3 = models.CharField(max_length=120, default='nothing')
    technologies_used4 = models.CharField(max_length=120, default='nothing')

    def __str__(self):
       return self.project_name

class Skill(models.Model):
    skill = models.CharField(max_length=120)
    score = models.IntegerField()

    def __str__(self):
        return self.skill