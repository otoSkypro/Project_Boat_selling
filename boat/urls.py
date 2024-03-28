from django.urls import path

from boat.apps import BoatConfig
from boat.views import BoatListView, BoatDetailView
from order.views import OrderCreateView

app_name = BoatConfig.name

urlpatterns = [
    path('', BoatListView.as_view(), name='boat_list'),
    path('<int:pk>/', BoatDetailView.as_view(), name='boat_view'),
    path('create/<int:pk>', OrderCreateView.as_view(), name='create'),
]
