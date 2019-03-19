from django.db import models


# Create your models here.
class Summary(models.Model):
    """
    The summary model is used to describe me and my education in the base.html.

    Attributes
    ----------
    about_me: TextField
        This section describes me as a person like age, weight lifting, 
        interests and so on.

    education:  TextField
        This section describes my education, like how I study in my free time
        or what I have achieved academically.
    """

    about_me = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)