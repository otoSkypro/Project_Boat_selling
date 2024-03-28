from django.urls import path

from boat.views import BoatListView, BoatDetailView
from order.views import OrderCreateView
from order.apps import OrderConfig

app_name = OrderConfig.name

urlpatterns = [
    path('create/<int:pk>', OrderCreateView.as_view(), name='create'),
]
