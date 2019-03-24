"""
Validators are used to validate fields associated with Project objects.

author: Benjamin Garrard
date: 3/20/2019
"""


def pdf_validator(value):
    """Validate that the given file is a pdf."""
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')