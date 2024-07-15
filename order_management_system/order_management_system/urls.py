from django.contrib import admin
from django.urls import path
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_customer, name='register'),
    path('success/', views.success, name='success'),
]
