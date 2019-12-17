from django.urls import path
from rest_framework import routers
from apps.meal_delivery.views import ProfilePageView, IndexView, DeliveryWindowView, ViewMealView

urlpatterns = [
    path('', IndexView.as_view(), name='md_index'),
    path('profile/', ProfilePageView.as_view(), name='md_profile'),
    path('delivery_window/<int:window_id>', DeliveryWindowView.as_view(), name='delivery_window'),
    path('view_meal/<int:meal_id>', ViewMealView.as_view(), name='view_meal')
]