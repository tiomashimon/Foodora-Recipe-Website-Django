from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from multiselectfield import MultiSelectField


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    time = models.IntegerField()
    image = models.CharField(max_length=500,
                             default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')
    link = models.CharField(max_length=500, default='')
    clicked = models.IntegerField(default=0)

    OPTION_CHOICES = (
        ('Very easy', 'Very easy'),
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Difficult', 'Difficult'),
        ('Breakfast', 'Breakfast'),
        ('Dinner', 'Dinner'),
        ('Meaty', 'Meaty'),
        ('Healthy', 'Healthy'),
        ('Pizza', 'Pizza'),
        ('Vegetables', 'Vegetables'),
        ('Pie', 'Pie'),
        ('Dessert', 'Dessert'),
        ('Vegan', 'Vegan'),
    )

    tags = MultiSelectField(choices=OPTION_CHOICES, max_choices=3, max_length=50, blank=True)

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
