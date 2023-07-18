from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.food, name='food'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('add/', login_required(views.create_item), name='create_item'),
    path('edit/<int:id>/', login_required(views.edit_item), name='edit_item'),
    path('delete/<int:id>/', login_required(views.delete_item), name='delete_item'),
    path('rating/', login_required(views.rating), name='rating'),
]
