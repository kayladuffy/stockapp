from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('deletestock.html', views.about, name="deletestock"),
    path('add_stock.html', views.add_stock, name="add_stock"),
    path('delete/<stock_id>', views.delete, name="delete"),
]