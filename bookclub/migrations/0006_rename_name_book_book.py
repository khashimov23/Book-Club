# Generated by Django 3.2.4 on 2021-06-06 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0005_alter_discussion_opinion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='book',
        ),
    ]