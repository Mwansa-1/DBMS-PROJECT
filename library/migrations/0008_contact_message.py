# Generated by Django 4.2.2 on 2023-10-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]