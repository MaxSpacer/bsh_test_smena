from .views import HomePageView
from django.urls import path


app_name = 'smena_tests'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
