from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import (
    all_programs,
    program_section,
    WeightLossAnalysisForm,
    all_products,
    one_program,
    ProductDetailView
)

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('programs/', views.all_programs, name='#program_section'),
    path('program/', views.one_program, name='program'),
    path('products/', views.all_products, name='products'),
    path('weight_loss/', views.WeightLossAnalysis, name='weight_loss'),
    path('product/<int:pk>/',
         ProductDetailView.as_view(), name='product-detail'),
]
