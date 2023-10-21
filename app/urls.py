from django.urls import path
from .views import Products
from .services.ctgview import CategoryView, SubCategoryView
from app.services.mainview import MainView
from app.services.partners_view import PartnersView
from app.services.productview import ProductView

urlpatterns = [
    path('pro/', Products.as_view()),

    path('ctg/', CategoryView.as_view()),
    path('ctg/<int:pk>/', CategoryView.as_view()),

    path('subctg/', SubCategoryView.as_view()),
    path('subctg/<int:pk>/', SubCategoryView.as_view()),

    path('main/', MainView.as_view()),
    path('main/<int:pk>/', MainView.as_view()),

    path('part/', PartnersView.as_view()),
    path('part/<int:pk>/', PartnersView.as_view()),

    path('prod/', ProductView.as_view()),
    path('prod/<int:pk>/', ProductView.as_view()),


]