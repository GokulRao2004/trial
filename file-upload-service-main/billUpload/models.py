# YourAppName/models.py

from django.core.exceptions import ValidationError
from django.db import models

def validate_excel_extension(value):
    if not value.name.lower().endswith('.xlsx'):
        raise ValidationError('Only .xlsx files are allowed.')

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', validators=[validate_excel_extension])
