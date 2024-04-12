from django.urls import path
# urls.py가 있는 곳고 같은 위치에서 가져올거야
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('data-throw/', views.data_throw),
    path('data-catch/', views.data_catch),
]
