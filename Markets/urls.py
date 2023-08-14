from django.urls import path
from Markets import views

urlpatterns = [
    path('', views.MarketsIndex, name="markets_index"),
    path('DetailInfoStock/', views.DetailStockInfo, name='detailinfostock'),
]