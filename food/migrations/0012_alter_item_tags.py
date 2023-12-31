# Generated by Django 4.2.3 on 2023-07-18 16:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_item_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Breakfast', 'Breakfast'), ('Dinner', 'Dinner'), ('Easy', 'Easy'), ('Medium', 'Medium'), ('Difficult', 'Difficult'), ('Meaty', 'Meaty'), ('Healthy', 'Healthy')], max_length=50),
        ),
    ]
