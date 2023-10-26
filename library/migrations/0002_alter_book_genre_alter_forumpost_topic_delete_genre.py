# Generated by Django 4.2.2 on 2023-09-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='topic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]