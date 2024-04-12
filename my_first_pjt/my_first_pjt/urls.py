"""
URL configuration for my_first_pjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from articles import views

# 프로젝트의 urls
# 여기에 articles, users의 urls.py를 포함시켜야 함
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    # 여기서 적어준 url은 spring에서 @RequestMapping("~~")에서 처리한 공통의 URL 주소
    path('articles/', include('articles.urls')),
    path('users/', include('users.urls')),
]
