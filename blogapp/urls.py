from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.About, name='about'),
    path('post', views.PostView.as_view(), name='post'),
    path('post_detail/<int:pk>', views.PostDetailsView.as_view(), name='post_detail'),

]