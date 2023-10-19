from django.urls import path
from .views import Products
from .services.ctgview import CategoryView, SubCategoryView
urlpatterns = [
    path('pro/', Products.as_view()),

    path('ctg/', CategoryView.as_view()),
    path('ctg/<int:pk>/', CategoryView.as_view()),

    path('subctg/', SubCategoryView.as_view()),
    path('subctg/<int:pk>/', SubCategoryView.as_view())
]