# Generated by Django 4.2.3 on 2023-07-15 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_alter_item_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user_name',
            new_name='user',
        ),
    ]
