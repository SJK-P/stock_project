from django.urls import path
from . import views

app_name = 'stock'
urlpatterns = [
    path('', views.overview, name='overview'),
    path('earning/', views.earning, name='earning'),
]