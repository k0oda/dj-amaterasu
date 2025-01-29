from django.contrib import admin
from django.urls import path

from wwwdj import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('rent/', views.rent, name='rent'),
    path('signup/', views.sign_up, name='signup'),
    path('signin/', views.sign_in, name='signin'),
    path('logout/', views.logout_view, name='logout'),
]
