# Generated by Django 4.2.9 on 2024-01-26 13:33

import billUpload.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', validators=[billUpload.models.validate_excel_extension])),
            ],
        ),
    ]
