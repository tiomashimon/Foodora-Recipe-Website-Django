from django.contrib import admin
from django.urls import path
from django.urls import include

import users
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from food import views as food_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profile, name='profile'),
    path('edit/', users_views.edit, name='edit'),
    path('', food_views.home, name='home')

]

urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
