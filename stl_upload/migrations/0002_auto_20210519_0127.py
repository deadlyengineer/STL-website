# Generated by Django 3.1 on 2021-05-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stl_upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstl',
            name='stl_file',
        ),
        migrations.AddField(
            model_name='userstl',
            name='file',
            field=models.FileField(default='settings.STATIC_URL/uploads/user_uploaded_model.stl', upload_to=''),
        ),
    ]