# Generated by Django 4.2.3 on 2023-07-15 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_rename_user_name_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='clicked',
            field=models.IntegerField(default=0),
        ),
    ]
