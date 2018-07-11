from django.urls import path
from . import views

urlpatterns = [
    path('login_for_medal/', views.login_for_medal, name='login_for_medal'),
    path('login/',views.user_login,name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('user_info/',views.user_info,name='user_info'),    # 个人资料
    path('change_nickname/',views.change_nickname,name='change_nickname'), # 修改用户昵称
]
