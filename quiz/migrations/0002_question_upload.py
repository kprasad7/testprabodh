# Generated by Django 3.0 on 2021-07-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='upload',
            field=models.ImageField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
