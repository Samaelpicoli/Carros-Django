from django.urls import path

from cars import views

urlpatterns = [
    path('', views.CarsListView.as_view(), name='car_list'),
    path('new-car/', views.CreateCarView.as_view(), name='new_car'),
    path('detail/<int:pk>/', views.DetailCarView.as_view(), name='car_detail'),
    path('update/<int:pk>/', views.UpdateCarView.as_view(), name='car_update'),
    path('delete/<int:pk>/', views.DeleteCarView.as_view(), name='car_delete'),
]
