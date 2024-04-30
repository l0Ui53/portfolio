from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio_index'),
    path('details/', views.details, name='portfolio_details'),
    path('search/', views.search_results, name='search_results'),
    path('profile/', views.show_profile, name='portfolio_profile'),
]