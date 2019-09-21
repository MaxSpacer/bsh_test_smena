

from django.urls import path
from . import views
from django.views.generic import ListView
from .views import HomePageView

# app_name = 'landing'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
#
# urlpatterns = [
#     path('', views.landing, name='landing'),
#     # path('create/', views.CallmeCreateView.as_view(), name='create_callme'),
# ]
