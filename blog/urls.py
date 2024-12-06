from django.urls import path, include
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='home'),

]