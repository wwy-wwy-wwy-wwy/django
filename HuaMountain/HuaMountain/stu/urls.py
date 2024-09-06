
#coding=utf-8
from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.index_view),
    path('test/',views.test_view),
    path('weather/', views.weather_view),
    path('temp/',views.temp_view),
    # path('caogao/',views.caogao_view)
]