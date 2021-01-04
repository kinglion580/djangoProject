from django.urls import path
from .views import IndexView

app_name = 'progress_bar'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]