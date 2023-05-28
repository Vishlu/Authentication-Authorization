from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', views.register, name='register'),
    path('', views.login_form, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logoutform'),
    path('change_pas/', views.change_password, name='change-pas'),
    path('change_pas2/', views.change_password2, name='change2pas'),
    path('userdetail/<int:id>', views.user_detail, name='userdetail'),
    
]
