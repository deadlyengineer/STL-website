# Generated by Django 3.1 on 2021-05-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stl_upload', '0003_auto_20210519_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstl',
            name='file',
            field=models.FileField(default='settings.STATIC_URL/uploads/user_uploaded_model.stl', upload_to='static/uploads'),
        ),
    ]