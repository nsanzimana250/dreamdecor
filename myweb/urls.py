from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('product/<int:id>/', views.product, name='product'),
    path('Bedroom_Furniture/', views.Bedroom_Furniture, name='Bedroom_Furniture'),
    path('Kitchen_Furniture/', views.Kitchen_Furniture, name='Kitchen_Furniture'),
    path('Living_Room_Furniture/', views.Living_Room_Furniture, name='Living_Room_Furniture'),
    path('office_furnitures/', views.office_furnitures, name='office_furnitures'),
    path('campany/', views.campany, name='campany'),
    path('dashboald/', views.dashboald, name='dashboald'),
        

        # campany
]
