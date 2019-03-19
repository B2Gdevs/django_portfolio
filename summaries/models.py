from django.db import models
from django.core.exceptions import ValidationError


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

    def save(self, *args, **kwargs):
        """
        save() is an overridden method of the Model class

        Summary is only allowed to have one summary in the app.  save() is
        overridden to check if summary objects exist and if they do to 
        return a validation error since only one is allowed
        """
        if Summary.objects.exists() and not self.pk:
            # if you'll not check for self.pk 
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Summary instance')
        return super(Summary, self).save(*args, **kwargs)