from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.index, name='index'),
    path('api/', views.StockList.as_view(), name='api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
