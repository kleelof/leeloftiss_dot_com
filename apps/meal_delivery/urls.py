from django.urls import path
from rest_framework import routers
from apps.meal_delivery.views import ProfilePageView, IndexView, DeliveryWindowView, ViewMealView, AppendToOrder, \
    logout, MyOrdersView, RemoveOrder

urlpatterns = [
    path('', IndexView.as_view(), name='md_index'),
    path('profile/', ProfilePageView.as_view(), name='md_profile'),
    path('delivery_window/<int:window_id>', DeliveryWindowView.as_view(), name='md_delivery_window'),
    path('view_meal/<int:meal_id>/<int:window_id>', ViewMealView.as_view(), name='md_view_meal_by_window'),
    path('view_meal/<int:meal_id>', ViewMealView.as_view(), name='md_view_meal'),
    path('append_to_order/', AppendToOrder.as_view(), name='md_append_to_order'),
    path('logout/', logout, name='md_logout'),
    path('my_orders/', MyOrdersView.as_view(), name='md_my_orders'),
    path('remove_order/<int:order_id>', RemoveOrder.as_view(), name='md_remove_order'),
]