# Generated by Django 4.2.3 on 2023-07-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_item_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='time',
        ),
        migrations.AddField(
            model_name='item',
            name='link',
            field=models.CharField(default='food', max_length=500),
        ),
    ]
