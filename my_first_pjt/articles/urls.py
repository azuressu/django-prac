from django.urls import path
# urls.py가 있는 곳고 같은 위치에서 가져올거야
from . import views

urlpatterns = [
    path("", views.articles, name = "articles"),
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path('data-throw/', views.data_throw, name = "data-throw"),
    path('data-catch/', views.data_catch, name = "data-catch"),
]
