from django.urls import path
from .views import CategoryApiView, ProductApiView, ProductByCategoryApiView, ProductByDatabase

urlpatterns = [
    path('category/<str:database>', CategoryApiView.as_view()),
    path('product/<str:database>', ProductApiView.as_view()),
    path('product-by-database', ProductByDatabase.as_view()),
    path('product-group/<str:database>', ProductByCategoryApiView.as_view()),
]