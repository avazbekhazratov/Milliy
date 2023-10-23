from django.urls import path

from .services.auth import AuthorizationView, LoginView
from .views import Products
from .services.ctgview import CategoryView, SubCategoryView
from app.services.mainview import MainView
from app.services.partners_view import PartnersView
from app.services.productview import ProductView
from app.services.savol_javob import Savol_View

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

    path('savol/', Savol_View.as_view()),
    path('savol/<int:pk>/', Savol_View.as_view()),

    path('regis/',AuthorizationView.as_view()),
    path('login/', LoginView.as_view()),

]
