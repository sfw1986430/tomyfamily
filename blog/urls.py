#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('post/<int:post_id>/', views.blogDetailView, name='post_detail'),
    path('post/new/', views.blogCreatNewView, name='post_new'),
    path('post/<int:post_id>/edit/', views.blogPostUpdateView, name='post_edit'),
    path('post/<int:post_id>/delete/', views.blogPostDeleteView, name='post_delete'),

]