from django.contrib import admin
from django.urls import path
from . import views

app_name = 'redis_queue'
urlpatterns = [
    path('', views.index, name='index'),
    path('execute/', views.execute, name='execute'),
    path('get_message/<user_uuid>/', views.get_message, name='get_message'),
    path('admin/', admin.site.urls),
]