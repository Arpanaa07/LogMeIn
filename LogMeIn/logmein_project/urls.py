from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout
    path('', account_views.home, name='home'),  # Home page
]
