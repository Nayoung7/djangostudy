from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# /polls/ : 뒤에 아무것도 안붙으면 view.index라는 view 내부로 연결시켜주는 것