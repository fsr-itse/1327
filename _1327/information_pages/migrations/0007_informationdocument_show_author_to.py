# Generated by Django 2.2.11 on 2020-03-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information_pages', '0006_rename_view_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationdocument',
            name='show_author_to',
            field=models.IntegerField(choices=[(0, 'No one'), (1, 'Logged in users'), (2, 'Everyone')], default=1, verbose_name='Show author to'),
        ),
    ]
