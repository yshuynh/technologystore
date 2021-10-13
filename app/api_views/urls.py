from django.urls import path
from .api import *

urlpatterns = [
    path('categories', CategoryListAPI.as_view(), name='category_list'),
    path('products', ProductListAPI.as_view(), name='product_list'),
    # path('single/<str:pk>', CategoryDetailAPI.as_view(), name='category_detail'),
    # path('<str:pk>', PostOfCategoryAPI.as_view(), name='store_search'),
]
