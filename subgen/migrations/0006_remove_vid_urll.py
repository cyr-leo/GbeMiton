# Generated by Django 5.0.6 on 2024-05-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subgen', '0005_vid_urll_alter_vid_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vid',
            name='urll',
        ),
    ]