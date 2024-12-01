from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<str:pk>', views.post, name="post"),
    path('myblog/post/<str:pk>', views.post, name="post"),
    path('add', views.add, name="add"),
    path('myblog/add', views.add, name="add"),
    path('myblog/delete/<str:delete_post>',views.delete,name='delete'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('myblog/<str:user_id>',views.myblog,name="myblog"),
    path('logout',views.logout,name="logout")
]
