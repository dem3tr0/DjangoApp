from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, kwargs={'name': 'Tom', 'age': 38}),
    re_path(r'^contacts/', views.contacts),
    re_path(r'^user/(?P<name>\D+)/(?P<age>\d+)/', views.user),
    re_path(r'^user/(?P<name>\D+)/', views.user),
    re_path(r'^user/', views.user),
]
