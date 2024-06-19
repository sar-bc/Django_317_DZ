from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('show_post/<int:id>/', views.show_post, name='show_post'),

]
