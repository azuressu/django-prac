from django.urls import path
# urls.py가 있는 곳고 같은 위치에서 가져올거야
from . import views

urlpatterns = [
    # 현재 users 함수가 없는데 요청하고 있어서 발생한 에러
    # File "/Users/suyeon/Desktop/django/my_first_pjt/users/urls.py", line 6, in <module>
    # path('', views.users),
    # AttributeError: module 'users.views' has no attribute 'users'
    # path('', views.users),
    path('<str:username>/', views.profile),
]