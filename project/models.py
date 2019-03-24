"""
This script is used to create the models for the projects app.

Author: Benjamin Garrard
Date: 3/20/2019
"""
from django.db import models
from django.utils.timezone import now
from .validators import pdf_validator


# Create your models here.
class Project(models.Model):
    """
    Projects are a project that has been worked on in code and/or art.

    This class is a django model that represents one row inside the projects
    table within the database.  A project must have a name, can be whatever
    category, must have a date when it was worked on, there must be a
    description and an image to go along with it.

    Attributes
    ----------
    project_name : CharField
        The name of the project that was worked on.

    project_category : CharField
        The category of the project, e.g. Virtual Reality, Data Science.

    project_date : DateField
        This is the date when the project was started.  If left blank todays
        date will be used.

    project_description : TextField
        Describes what the project was.

    image : ImageField
        The image that will be displayed like a thumbnail for the project on
        the home page and on the detail page.

    technologies_used1 : CharField
        One of the technologies used in the project.

    technologies_used2 : CharField
        One of the technologies used in the project.

    technologies_used3 : CharField
        One of the technologies used in the project.

    technologies_used4 : CharField
        One of the technologies used in the project.

    pdf_presentation : FileField
        A pdf of a slideshow or documentation of a project.

    """

    project_name = models.CharField(max_length=120)
    project_category = models.CharField(max_length=120)
    project_date = models.DateField(default=now, editable=True)
    project_description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    technologies_used1 = models.CharField(max_length=120, default='N/A')
    technologies_used2 = models.CharField(max_length=120, default='N/A')
    technologies_used3 = models.CharField(max_length=120, default='N/A')
    technologies_used4 = models.CharField(max_length=120, default='N/A')

    pdf_presentation = models.FileField(upload_to='pdfs/',
                                        validators=[pdf_validator],
                                        blank=True, null=True)

    class Meta:
        """Rename the database table from Project to projects."""

        db_table = "projects"

    def __str__(self):
        """Return the project name when printed."""
        return self.project_name


class Skill(models.Model):
    """
    A Skill is something Benjamin Garrard is proficient in.

    Attributes
    ----------
    skill : CharField
        skill is the name of the skill.

    score : IntegerField
        score is the confident level that is associated with the skill.

    """

    skill = models.CharField(max_length=120)
    score = models.IntegerField()

    def __str__(self):
        """Return the skill name."""
        return self.skill
