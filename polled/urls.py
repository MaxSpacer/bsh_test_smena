"""bsh_test_smena URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'polled'

urlpatterns = [
    # path('polled/', include('polled.urls')),
	# path('create_polled_item/<pk>/', views.create_polled_item, name='create_polled_item_n'),
    # path('quest_formset/<pk>/', views.quest_formset, name='quest_formset_n'),
    # path('receive_formset_data/<pk>/', views.receive_formset_data, name='receive_formset_data_n'),
    path('polled_itog/<pk>/', views.polled_itog, name='polled_itog_n'),
    path('quest_formset_render/<pk>/', views.quest_formset_render, name='quest_formset_render_n'),
	path('generate_test_order/<pk>/', views.create_polled_order, name='create_polled_order_n'),

]
