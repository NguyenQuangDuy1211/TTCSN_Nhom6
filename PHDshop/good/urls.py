from django.urls import path
from .views import GoodListView


urlpatterns = [
    path('api/goods/list', GoodListView.as_view(), name='good-list'),
]