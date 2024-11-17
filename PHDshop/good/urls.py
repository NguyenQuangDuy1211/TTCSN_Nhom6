from django.urls import path
from .views import GoodListView, GetDetailFromID, GetListViewFromCategory, GetListViewFromBrand

urlpatterns = [
    path('list', GoodListView.as_view(), name='good-list'),
    path('<int:pk>/detail', GetDetailFromID.as_view(), name='good-detail'),
    path('<int:category_id>/getByCategoryId', GetListViewFromCategory.as_view(), name='good-by-category'),
    path('<int:brand_id>/getByBrandId', GetListViewFromBrand.as_view(), name='good-by-brand')
]