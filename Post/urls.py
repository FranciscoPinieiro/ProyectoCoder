from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Post import views

urlpatterns = [
    path('',views.posts, name='Post'),
    path('showPost/<id>',views.showPost, name='ShowPost'),
    path('comment/<id>',views.comment, name='Comment'),
]