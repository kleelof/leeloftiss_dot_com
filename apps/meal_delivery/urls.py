from django.urls import path
from rest_framework import routers
from apps.meal_delivery.views import ProfilePageView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='md_index'),
    path('profile/', ProfilePageView.as_view(), name='md_profile')
]