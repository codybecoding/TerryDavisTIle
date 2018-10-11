from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.portfolio_index, name='portfolio'),
    path('flooring/', views.floor_index, name='flooring'),
    path('showers/', views.shower_index, name='showers'),
    path('kitchens/', views.kitchen_index, name='kitchens'),
    path('bathtubs/', views.bathtub_index, name='bathtubs'),
    path('fireplaces/', views.fireplace_index, name='fireplaces'),
    path('countertops/', views.countertop_index, name='countertops'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
