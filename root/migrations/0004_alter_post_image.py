# Generated by Django 3.2.5 on 2021-07-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
