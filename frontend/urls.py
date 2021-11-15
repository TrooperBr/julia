
from django.urls import path
from .views import ProdutsList, ProductDetail
urlpatterns = [
	path('<pk>',ProductDetail.as_view(), name='product-detail'),
	path('',ProdutsList.as_view(),name='products')
]