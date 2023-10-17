from django.urls import path
from .views import Products
urlpatterns = [
    path('pro/', Products.as_view())
]