#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('post/<int:post_id>/', views.blogDetailView, name='post_detail'),

]