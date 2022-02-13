from django.urls import path
# from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('crops/', views.CropList.as_view(), name='crop_list'),
    path('crop/<int:pk>',
         views.CropDetail.as_view(), name='crop_detail'),
    path('varieties/', views.VarietyList.as_view(), name='variety_list'),
    path('varieties/<int:pk>', views.VarieyDetail.as_view(), name='variety_detail'),
    path('plantings/', views.PlantingList.as_view(), name='planting_list'),
    path('plantings/<int:pk>', views.PlantingDetail.as_view(), name='planting_detail'),
]