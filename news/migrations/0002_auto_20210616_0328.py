# Generated by Django 3.2.4 on 2021-06-15 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='New',
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
    ]
